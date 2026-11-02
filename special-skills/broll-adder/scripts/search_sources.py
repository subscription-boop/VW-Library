#!/usr/bin/env python3
"""Search every enabled source in sources.yaml (in priority order) and print JSON.

Usage:
  python search_sources.py --query "elon musk tesla factory" [--query "..."] \
      --sources ../sources.yaml [--max 8] [--min-seconds 0]

Output: {"sliceable": [...], "full": [...], "errors": [...]}
Each item: source, kind, title, url, page, duration (seconds or null), license, extra
"""
import argparse
import json
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

UA = "broll-adder/1.0 (B-roll research script)"


def http_json(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def ytdlp_cmd():
    exe = shutil.which("yt-dlp")
    return [exe] if exe else [sys.executable, "-m", "yt_dlp"]


# ---------------------------------------------------------------- engines

def search_youtube(query, cfg):
    n = int(cfg.get("max_results", 8))
    max_min = cfg.get("max_video_minutes")
    cmd = ytdlp_cmd() + ["--flat-playlist", "--dump-json", "--no-warnings", f"ytsearch{n}:{query}"]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if out.returncode != 0 and not out.stdout:
        raise RuntimeError(out.stderr.strip()[-400:])
    items = []
    for line in out.stdout.splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        dur = d.get("duration")
        if max_min and dur and dur > max_min * 60:
            continue
        vid = d.get("id")
        items.append({
            "title": d.get("title"),
            "url": f"https://www.youtube.com/watch?v={vid}",
            "page": f"https://www.youtube.com/watch?v={vid}",
            "duration": dur,
            "license": "YouTube (copyrighted unless stated)",
            "extra": {"channel": d.get("channel") or d.get("uploader"), "views": d.get("view_count")},
        })
    return items


def search_archive_org(query, cfg):
    n = int(cfg.get("max_results", 6))
    q = f"({query}) AND mediatype:(movies)"
    cols = cfg.get("collections") or []
    if cols:
        q += " AND collection:(" + " OR ".join(cols) + ")"
    params = [("q", q), ("rows", str(n)), ("output", "json"), ("sort[]", "downloads desc")]
    for f in ("identifier", "title", "licenseurl", "runtime", "year"):
        params.append(("fl[]", f))
    data = http_json("https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(params))
    items = []
    for doc in data.get("response", {}).get("docs", []):
        ident = doc["identifier"]
        file_url, dur = None, None
        try:
            meta = http_json(f"https://archive.org/metadata/{ident}")
            vids = [f for f in meta.get("files", []) if f.get("name", "").lower().endswith((".mp4", ".mov", ".mpeg4", ".m4v", ".webm", ".ogv"))]
            # prefer mp4 originals, then largest
            vids.sort(key=lambda f: (not f["name"].lower().endswith(".mp4"), f.get("source") != "original", -int(f.get("size", 0) or 0)))
            if vids:
                file_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(vids[0]['name'])}"
                try:
                    dur = to_seconds(vids[0].get("length"))
                except (TypeError, ValueError):
                    dur = None
        except Exception:
            pass
        if not file_url:
            continue
        title = doc.get("title")
        if isinstance(title, list):
            title = title[0]
        items.append({
            "title": title,
            "url": file_url,
            "page": f"https://archive.org/details/{ident}",
            "duration": dur,
            "license": doc.get("licenseurl") or "see page (often public domain)",
            "extra": {"year": doc.get("year")},
        })
    return items


def search_wikimedia(query, cfg):
    n = int(cfg.get("max_results", 6))
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"{query} filetype:video", "gsrnamespace": "6", "gsrlimit": str(n),
        "prop": "imageinfo", "iiprop": "url|extmetadata|mediatype|size",
    }
    data = http_json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params))
    items = []
    for page in (data.get("query", {}).get("pages", {}) or {}).values():
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata", {})
        items.append({
            "title": page.get("title", "").replace("File:", "").rsplit(".", 1)[0],
            "url": info.get("url"),
            "page": info.get("descriptionurl"),
            "duration": info.get("duration"),
            "license": (meta.get("LicenseShortName") or {}).get("value", "see page"),
            "extra": {"credit": (meta.get("Artist") or {}).get("value", "")[:120]},
        })
    return items


ENGINES = {"youtube": search_youtube, "archive_org": search_archive_org, "wikimedia": search_wikimedia}


def to_seconds(t):
    if t is None:
        return None
    parts = [float(p) for p in str(t).split(":")]
    s = 0.0
    for p in parts:
        s = s * 60 + p
    return s


def load_sources(path):
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML missing: run  python -m pip install pyyaml")
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    srcs = [s for s in cfg.get("sources", []) if s.get("enabled", True)]
    return sorted(srcs, key=lambda s: s.get("priority", 99))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", action="append", required=True)
    ap.add_argument("--sources", default="sources.yaml")
    ap.add_argument("--max", type=int, default=None, help="override max_results per source per query")
    args = ap.parse_args()

    result = {"sliceable": [], "full": [], "errors": []}
    seen = set()
    for src in load_sources(args.sources):
        if src.get("engine") == "web":
            continue  # searched by Claude with WebSearch, not by this script
        eng = ENGINES.get(src.get("engine"))
        if not eng:
            result["errors"].append(f"{src.get('name')}: unknown engine {src.get('engine')}")
            continue
        if args.max:
            src = {**src, "max_results": args.max}
        for q in args.query:
            try:
                found = eng(q, src)
            except Exception as e:
                result["errors"].append(f"{src['name']} / '{q}': {e}")
                continue
            for it in found:
                if not it.get("url") or it["url"] in seen:
                    continue
                seen.add(it["url"])
                it.update({"source": src["name"], "kind": src.get("kind", "full"), "query": q})
                result["sliceable" if it["kind"] == "sliceable" else "full"].append(it)

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()

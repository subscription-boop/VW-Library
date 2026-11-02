#!/usr/bin/env python3
"""Propose exact B-roll slices inside a YouTube video using its subtitles and chapters.

Usage:
  python find_moments.py --url https://www.youtube.com/watch?v=XXXX --keywords "tesla,factory" \
      [--min 3] [--max 8] [--top 2] [--lang en]
  python find_moments.py --subs-file captions.json3 --keywords "..."   (offline test)

Output JSON: {"url", "title", "duration", "method", "moments": [{"start","end","seconds","score","why"}]}
method = subtitles | chapters | none
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile


def ytdlp_cmd():
    exe = shutil.which("yt-dlp")
    return [exe] if exe else [sys.executable, "-m", "yt_dlp"]


def fmt(t):
    t = max(0, int(round(t)))
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


# ------------------------------------------------------------ subtitles

def parse_json3(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    segs = []
    for ev in data.get("events", []):
        if "segs" not in ev:
            continue
        text = "".join(s.get("utf8", "") for s in ev["segs"]).replace("\n", " ").strip()
        if not text:
            continue
        start = ev.get("tStartMs", 0) / 1000
        dur = ev.get("dDurationMs", 2000) / 1000
        segs.append((start, start + dur, text))
    return segs


def parse_vtt(path):
    segs = []
    ts = re.compile(r"(\d+):(\d+):(\d+(?:\.\d+)?)\s+-->\s+(\d+):(\d+):(\d+(?:\.\d+)?)")
    cur = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = ts.search(line)
            if m:
                g = [float(x) for x in m.groups()]
                cur = [g[0] * 3600 + g[1] * 60 + g[2], g[3] * 3600 + g[4] * 60 + g[5], ""]
                segs.append(cur)
            elif cur is not None and line.strip():
                cur[2] += " " + re.sub(r"<[^>]+>", "", line.strip())
    # auto-subs repeat lines; de-dup consecutive identical text
    out, last = [], None
    for s, e, t in segs:
        t = t.strip()
        if t and t != last:
            out.append((s, e, t))
            last = t
    return out


def load_subs(path):
    return parse_json3(path) if path.endswith(".json3") else parse_vtt(path)


def fetch_info_and_subs(url, lang):
    tmp = tempfile.mkdtemp(prefix="broll_subs_")
    cmd = ytdlp_cmd() + [
        "--skip-download", "--write-subs", "--write-auto-subs",
        "--sub-langs", f"{lang}.*,{lang}", "--sub-format", "json3/vtt/best",
        "--write-info-json", "--no-warnings", "-o", os.path.join(tmp, "v.%(ext)s"), url,
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    info = {}
    infos = glob.glob(os.path.join(tmp, "*.info.json"))
    if infos:
        with open(infos[0], encoding="utf-8") as f:
            info = json.load(f)
    subs = sorted(glob.glob(os.path.join(tmp, "*.json3")) + glob.glob(os.path.join(tmp, "*.vtt")))
    # prefer manual subs (no "-orig"/auto marker is not exposed in name; just take first json3)
    return info, (subs[0] if subs else None)


# ------------------------------------------------------------ scoring

def keyword_hits(text, kws):
    low = text.lower()
    return sum(1 for k in kws if k and k in low)


def moments_from_subs(segs, kws, mn, mx, top, duration):
    scored = []
    for i, (s, e, t) in enumerate(segs):
        hits = keyword_hits(t, kws)
        if not hits:
            continue
        # grow window forward over following segments until min length, cap at max
        start = max(0.0, s - 0.3)
        end = e
        text = t
        j = i + 1
        while end - start < mn and j < len(segs):
            end = segs[j][1]
            text += " " + segs[j][2]
            hits += keyword_hits(segs[j][2], kws) * 0.5
            j += 1
        end = min(end, start + mx)
        if end - start < mn:
            end = start + mn
        if duration:
            end = min(end, duration)
        scored.append({"start": start, "end": end, "score": round(hits, 2), "why": text[:140]})
    scored.sort(key=lambda m: (-m["score"], m["start"]))
    picked = []
    for m in scored:
        if all(m["end"] <= p["start"] or m["start"] >= p["end"] for p in picked):
            picked.append(m)
        if len(picked) >= top:
            break
    return picked


def moments_from_chapters(chapters, kws, mn, mx, top):
    out = []
    for c in chapters or []:
        hits = keyword_hits(c.get("title", ""), kws)
        if hits:
            s = c["start_time"] + 1
            e = min(c.get("end_time", s + mx), s + mx)
            out.append({"start": s, "end": max(e, s + mn), "score": hits, "why": "chapter: " + c.get("title", "")})
    out.sort(key=lambda m: -m["score"])
    return out[:top]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url")
    ap.add_argument("--subs-file")
    ap.add_argument("--keywords", required=True)
    ap.add_argument("--min", type=float, default=3)
    ap.add_argument("--max", type=float, default=8)
    ap.add_argument("--top", type=int, default=2)
    ap.add_argument("--lang", default="en")
    a = ap.parse_args()
    kws = [k.strip().lower() for k in a.keywords.split(",") if k.strip()]

    info, subs_path = ({}, a.subs_file) if a.subs_file else fetch_info_and_subs(a.url, a.lang)
    duration = info.get("duration")
    result = {"url": a.url, "title": info.get("title"), "duration": duration, "method": "none", "moments": []}

    if subs_path:
        ms = moments_from_subs(load_subs(subs_path), kws, a.min, a.max, a.top, duration)
        if ms:
            result["method"], result["moments"] = "subtitles", ms
    if not result["moments"]:
        ms = moments_from_chapters(info.get("chapters"), kws, a.min, a.max, a.top)
        if ms:
            result["method"], result["moments"] = "chapters", ms

    for m in result["moments"]:
        m["seconds"] = round(m["end"] - m["start"], 1)
        m["link"] = f"{a.url}&t={int(m['start'])}s" if a.url else None
        m["start"], m["end"] = fmt(m["start"]), fmt(m["end"])

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Download the B-roll picks into a broll folder with clean names.

Usage:
  python download.py --picks picks.json --out "D:/Projects/Tesla/broll" [--max-height 1080]

picks.json:
[
  {"code":"Y1","type":"slice","url":"https://www.youtube.com/watch?v=...","start":"01:24","end":"01:31","title":"..."},
  {"code":"A2","type":"full","url":"https://archive.org/download/.../x.mp4","title":"...","trim_start":"00:00","trim_end":"00:05"}
]
Prints a JSON report: [{"code","ok","file","seconds","resolution","error"}]
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import urllib.request

UA = "broll-adder/1.0 (B-roll research script)"


def ytdlp_cmd():
    exe = shutil.which("yt-dlp")
    return [exe] if exe else [sys.executable, "-m", "yt_dlp"]


def ffmpeg_exe():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("ffmpeg not found — run scripts/check_deps.py")


def secs(t):
    if t is None or t == "":
        return None
    s = 0.0
    for p in str(t).strip().split(":"):
        s = s * 60 + float(p)
    return s


def tag(t):
    t = int(round(t))
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{h}h{m:02d}m{s:02d}s" if h else f"{m:02d}m{s:02d}s"


def slug(text, maxlen=45):
    text = unicodedata.normalize("NFKD", text or "clip").encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    text = text[:maxlen].rstrip("-")
    return text or "clip"


def unique(path):
    base, ext = os.path.splitext(path)
    n, p = 2, path
    while os.path.exists(p):
        p = f"{base}_{n}{ext}"
        n += 1
    return p


def probe(path):
    """Return (seconds, 'WxH') using ffmpeg's stderr (no ffprobe needed)."""
    r = subprocess.run([ffmpeg_exe(), "-hide_banner", "-i", path], capture_output=True, text=True)
    dur = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", r.stderr)
    res = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", r.stderr)
    seconds = round(int(dur.group(1)) * 3600 + int(dur.group(2)) * 60 + float(dur.group(3)), 1) if dur else None
    return seconds, (f"{res.group(1)}x{res.group(2)}" if res else None)


def trim(src, dst, start, end):
    cmd = [ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y"]
    if start:
        cmd += ["-ss", str(start)]
    cmd += ["-i", src]
    if end is not None:
        cmd += ["-t", str(end - (start or 0))]
    cmd += ["-c:v", "libx264", "-preset", "fast", "-crf", "16", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", dst]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[-400:])


def do_slice(p, out_dir, max_h):
    s, e = secs(p["start"]), secs(p["end"])
    if s is None or e is None or e <= s:
        raise ValueError("slice needs start < end")
    final = unique(os.path.join(out_dir, f"{p['code']}_{slug(p.get('title'))}_{tag(s)}-{tag(e)}.mp4"))
    tmp = tempfile.mkdtemp(prefix="broll_dl_")
    loc = [] if shutil.which("ffmpeg") else ["--ffmpeg-location", ffmpeg_exe()]
    cmd = ytdlp_cmd() + loc + [
        "--no-warnings", "--no-playlist",
        "-f", f"bv*[height<={max_h}][ext=mp4]+ba[ext=m4a]/bv*[height<={max_h}]+ba/b[height<={max_h}]/b",
        "--download-sections", f"*{s}-{e}", "--force-keyframes-at-cuts",
        "--merge-output-format", "mp4",
        "-o", os.path.join(tmp, "clip.%(ext)s"), p["url"],
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    files = [f for f in os.listdir(tmp) if not f.endswith(".part")]
    if r.returncode != 0 or not files:
        raise RuntimeError((r.stderr or r.stdout).strip()[-400:] or "yt-dlp failed")
    got = os.path.join(tmp, files[0])
    if got.lower().endswith(".mp4"):
        shutil.move(got, final)
    else:
        trim(got, final, None, None)  # re-encode to mp4
    shutil.rmtree(tmp, ignore_errors=True)
    return final


BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def download_file(url, dst):
    ua = BROWSER_UA if "pexels.com" in url else UA  # Pexels refuses non-browser agents
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=60) as r, open(dst, "wb") as f:
        shutil.copyfileobj(r, f, 1024 * 1024)


def do_full(p, out_dir, max_h):
    ts, te = secs(p.get("trim_start")), secs(p.get("trim_end"))
    ext = os.path.splitext(p["url"].split("?")[0])[1].lower() or ".mp4"
    tmp = tempfile.mkdtemp(prefix="broll_dl_")
    raw = os.path.join(tmp, "raw" + ext)
    try:
        download_file(p["url"], raw)
    except Exception:
        # page URL instead of direct file? let yt-dlp try
        r = subprocess.run(ytdlp_cmd() + ["--no-warnings", "-f", f"b[height<={max_h}]/b",
                                          "-o", os.path.join(tmp, "raw.%(ext)s"), p["url"]],
                           capture_output=True, text=True, timeout=900)
        cands = [f for f in os.listdir(tmp) if f.startswith("raw") and not f.endswith(".part")]
        if r.returncode != 0 or not cands:
            raise RuntimeError((r.stderr or "download failed").strip()[-400:])
        raw = os.path.join(tmp, cands[0])
        ext = os.path.splitext(raw)[1].lower()

    suffix = f"_{tag(ts or 0)}-{tag(te)}" if (ts or te) and te else ""
    final = unique(os.path.join(out_dir, f"{p['code']}_{slug(p.get('title'))}{suffix}.mp4"))
    if ts or te or ext != ".mp4":
        trim(raw, final, ts, te)  # trims and/or converts webm/ogv/mov to editor-friendly mp4
    else:
        shutil.move(raw, final)
    shutil.rmtree(tmp, ignore_errors=True)
    return final


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--picks", required=True)
    ap.add_argument("--out", default="broll")
    ap.add_argument("--max-height", type=int, default=1080)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    with open(a.picks, encoding="utf-8") as f:
        picks = json.load(f)

    report = []
    for p in picks:
        item = {"code": p.get("code"), "ok": False}
        try:
            path = do_slice(p, a.out, a.max_height) if p.get("type") == "slice" else do_full(p, a.out, a.max_height)
            s, res = probe(path)
            item.update(ok=True, file=os.path.abspath(path), seconds=s, resolution=res)
        except Exception as e:
            item["error"] = str(e)
        report.append(item)
        print(f"{'OK ' if item['ok'] else 'ERR'} {item['code']}: {item.get('file') or item.get('error')}", file=sys.stderr)

    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    print()
    sys.exit(0 if all(r["ok"] for r in report) else 2)


if __name__ == "__main__":
    main()

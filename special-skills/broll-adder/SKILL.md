---
name: broll-adder
description: Finds and downloads B-roll for the user's videos. Given a topic or a line of script (e.g. "Elon Musk talking about Tesla", 3–8s), it searches YouTube first and proposes exact slices (01:24–01:31), then Archive.org and Wikimedia Commons for full clips, shows everything with codes (Y1, A1…), waits for the user to pick, then downloads only the picks — YouTube as trimmed slices — into the project's `broll` folder with clean names. Use whenever the user asks for B-roll, stock/archive footage, "find me a clip of X", "بی‌رول", "فوتیج", "یه کلیپ از … پیدا کن", cutaways or inserts for a script line, even if the user never says "B-roll".
---

# broll-adder

Turn a script line into ready-to-edit B-roll clips: search → show with codes → the user picks → download only the picks into `broll/`.

## Mode — show first, download after (default)

The user wants control so nothing gets redone. Default order is always: **search → show → the user picks (and sets the seconds) → download only the picks.**

- **Never guess a timestamp.** Give an exact slice only when it has a real basis (subtitles/chapters read by `find_moments.py`, or you actually watched the footage). If you have no basis, don't mark it «تخمینی» either: give the plain video link and ask the user to name the seconds, e.g. «ثانیه‌اش رو خودت بگو». The user replies like `Y2 از 01:20 تا 01:26`.
- **«اتومات» mode** — only when the user says «اتومات» (or clearly "you choose, I'm short on time"): you decide everything yourself. Download the candidates first, watch them (contact sheets / frames), pick exact moments, download/cut the picks and carry on with the edit. Tell the user in one line what you picked and why.
- **«برعکس کن»** — download candidates first, watch them, then show the user the list with exact (watched) seconds and let the user pick. Use this only when the user asks for it.

Talk to the user in their language (`settings.json` → `language` in the system folder: `fa` Persian, `en` English), short, simple, non-technical. Titles, links and file names stay as they are.

Bundled files (paths relative to this skill folder):
- `sources.yaml` — sources in priority order. Read it every run; never hardcode the list.
- `scripts/check_deps.py` — checks yt-dlp, ffmpeg, PyYAML.
- `scripts/search_sources.py` — searches every enabled source, returns JSON.
- `scripts/find_moments.py` — reads a YouTube video's subtitles/chapters and proposes exact slices.
- `scripts/download.py` — downloads the picks (slice or full + trim) with clean names.

All scripts are plain Python 3 and work on Windows, macOS and Linux.

## Where to run

1. **A shell on the user's computer** (`device_bash` tool) is the first choice — the user's internet reaches YouTube and files land straight in the user's project folder.
2. **No shell in this chat?** Ask the user for terminal access to the user's computer at the start, in one line (in the user's language), so the work moves fast inside this chat: «برای اجرای دانلود روی کامپیوترت دسترسی ترمینال لازم دارم، اجازه می‌دی؟». If the chat offers a permission request for the shell, use it. Don't keep asking if it doesn't appear.
3. **Still no shell** → the workspace can't reach YouTube/Archive (network allowlist); don't retry another way. Search with WebSearch/WebFetch instead, and run the downloads on the user's computer with the **one-click .bat** below.

### One-click .bat (when there is no shell on the user's computer)

Write `picks.json` (or a candidates list) plus a small `.bat` into `<project>\broll\` with the file tools (SendUserFile → device_commit_files, Windows line endings `\r\n`), then tell the user: «روی `download_broll.bat` دوبار کلیک کن، آخرش بنویس done». Template:
```
@echo off
cd /d "%~dp0"
python -m pip install -q -U yt-dlp imageio-ffmpeg pyyaml > "%~dp0download_log.txt" 2>&1
python "<skill folder>\scripts\download.py" --picks "%~dp0picks.json" --out "%~dp0." >> "%~dp0download_log.txt" 2>&1
echo DONE. Go back to Claude and write: done
pause
```
After «done», check `download_log.txt` and the files with device_list_dir, then stage what you need.

## Step 0 — Dependencies (first run only)

Run `python scripts/check_deps.py`. If anything is missing, it prints the install commands for that OS. **Ask the user before installing** (one line: what's missing + "نصب کنم؟"). On yes, run the printed commands, then re-check. If `yt-dlp` is old, `python -m pip install -U yt-dlp` (YouTube breaks old versions).

## Step 1 — Get the brief

Pull from what the user already said; ask only for what's truly missing, in one short message:
- **Topic / script line** (e.g. «ایلان ماسک در حال صحبت درباره تسلا»)
- **Length range** per clip (default 3–8s if the user doesn't say)
- **Extras** — orientation (9:16 vs 16:9), era, "no talking head", "no logos", quality, how many options
- **Project folder** — where `broll/` should go. Default: the connected project folder; else `./broll` in the workspace.

Then turn the topic into 2–4 English search queries (YouTube and archives are mostly English) plus a few **moment keywords** that would be spoken at the right moment (e.g. `tesla, factory, model 3`).

## Step 2 — Search (in `sources.yaml` order)

```
python scripts/search_sources.py --query "elon musk tesla factory tour" --query "elon musk interview tesla" --sources sources.yaml --max 8 > results.json
```

**Sliceable sources (YouTube)** — for the best 4–6 candidates, find the exact moment:
```
python scripts/find_moments.py --url <video_url> --keywords "tesla,factory" --min 3 --max 8 --top 2
```
It reads subtitles + chapters and returns ranked windows with `start`/`end`. Pick the best window per video. If a video has no subtitles, use chapters or the description timestamps; if nothing, propose a sensible slice and say it's a guess («تخمینی»). Never invent a precise-looking timestamp without a basis.

**Full-download sources (Archive.org, Wikimedia Commons, anything added later)** — take title, duration, license and direct file URL from the search output. Skip clips far longer than useful unless they're clearly the best match (note "needs trim").

**Look beyond `sources.yaml` too.** If the brief needs something the listed sources do badly (e.g. happy people using a phone/laptop → free stock like Pexels; a product launch → the brand's official channel), search for it with WebSearch and include it. When a new source turns out useful, **add it to `sources.yaml`** (with a note on how to search and download it) so it's there next time, and say so in one line.

Drop junk: reaction videos, compilations with watermarks over everything, AI-slop thumbnails, clips that don't show the thing. Prefer real footage, higher resolution, the right orientation.

## Step 3 — Show results (in the user's language, this exact layout)

Full details first, then a compact pick list as the **last thing in the message**.

```
=== یوتیوب (قابل اسلایس) ===
[Y1] عنوان ویدیو
     بازه پیشنهادی: 01:24 – 01:31 (۷ ثانیه)
     لینک: https://www.youtube.com/watch?v=...&t=84s
     دلیل پیشنهاد: کوتاه، یک خط

[Y2] ...

=== آرشیو و سایر منابع (دانلود کامل) ===
[A1] عنوان کلیپ
     منبع: Archive.org
     مدت تقریبی: ۱۲ ثانیه
     لایسنس: Public Domain
     لینک: ...

[A2] ...

کدام‌ها را می‌خواهی؟ فقط شماره‌ها را بنویس:

Y1 - Elon Musk Tesla Factory Tour
Y2 - Elon Musk Interview 2024
A1 - Tesla Assembly Line 2018
A2 - Electric Car Production Archive
```

Rules: codes `Y1…` for sliceable, `A1…` for full-download (all non-YouTube sources share the A series, source named on each item). Put `&t=<seconds>s` on YouTube links so the user can check the moment in one click — only when the seconds have a real basis. With no basis, write «بازه: خودت بگو» instead of a range and give the plain link. Short titles in the pick list (≤ 6 words). Keep the list to ~5 Y + ~5 A unless the user asked for more. Save the full result set (code → url, start, end, title, source) to `broll_candidates.json` so Step 5 doesn't depend on re-reading the chat.

Then **stop and wait** for the user's pick.

## Step 4 — The user's pick

The user replies with codes like `Y1, A2, A3` (any separator, Farsi digits OK), often with the user's own seconds or links with `?t=` (use those exactly). The user may also adjust: `Y1 از 01:20 تا 01:30`, `A2 فقط ۵ ثانیه اول`. Apply adjustments; ignore unknown codes and say so in one line.

## Step 5 — Download

Write the picks to `picks.json` and run:
```
python scripts/download.py --picks picks.json --out "<project>/broll"
```
`picks.json` format:
```json
[
  {"code": "Y1", "type": "slice", "url": "https://www.youtube.com/watch?v=...", "start": "01:24", "end": "01:31", "title": "Elon Musk Tesla Factory Tour"},
  {"code": "A2", "type": "full", "url": "https://archive.org/download/.../file.mp4", "title": "Electric Car Production", "trim_start": "00:00", "trim_end": "00:05"}
]
```
- `slice` → downloads only that section (≤1080p, mp4, cut at clean frames).
- `full` → downloads the whole file; trims only if `trim_start`/`trim_end` given.
- Names: `Y1_elon-musk-tesla-factory-tour_01m24s-01m31s.mp4`, `A2_electric-car-production.mp4`. Never overwrites — adds `_2`.
- On a failed item, the script keeps going and reports it. Retry a failed YouTube slice once after `pip install -U yt-dlp`; then report it.

## Step 6 — Final report (user's language, short)

```
✅ دانلود شد (۳ فایل) → D:\Projects\Tesla\broll
- Y1_elon-musk-tesla-factory-tour_01m24s-01m31s.mp4 (۷ ثانیه، 1080p)
- A2_electric-car-production.mp4 (۵ ثانیه)
❌ A3 — منبع در دسترس نبود
آماده‌ان برای گذاشتن تو تایم‌لاین.
```

If files were made in the workspace (not on the user's computer), send them with SendUserFile.

## Rights (one line, only when it matters)

YouTube clips are usually copyrighted: fine for drafts/internal cuts; for client or monetized work, mention once that the clip needs a license or fair-use judgment. Archive/Wikimedia: show the license in Step 3; flag CC-BY (needs credit) and anything non-commercial.

## Adding a source

the user can say «Pexels رو هم اضافه کن», and you add useful new sources yourself (see Step 2). Add an entry to `sources.yaml` (see its comments). If it's a new site type, add a small search function to `search_sources.py` matching the existing ones (return `title, url, page, duration, license, source`).

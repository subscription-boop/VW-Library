#!/usr/bin/env python3
"""Check broll-adder dependencies (yt-dlp, ffmpeg, PyYAML) and print install commands for this OS.

Exit code 0 = all good, 1 = something missing.
"""
import importlib.util
import platform
import shutil
import subprocess
import sys


def ytdlp_version():
    exe = shutil.which("yt-dlp")
    if exe:
        cmd = [exe, "--version"]
    elif importlib.util.find_spec("yt_dlp"):
        cmd = [sys.executable, "-m", "yt_dlp", "--version"]
    else:
        return None
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip() or "?"
    except Exception:
        return None


def main():
    osname = platform.system()
    missing = []

    v = ytdlp_version()
    print(f"yt-dlp : {'OK ' + v if v else 'MISSING'}")
    if not v:
        missing.append("yt-dlp")

    ff = shutil.which("ffmpeg")
    print(f"ffmpeg : {'OK ' + ff if ff else 'MISSING'}")
    if not ff:
        missing.append("ffmpeg")

    has_yaml = importlib.util.find_spec("yaml") is not None
    print(f"PyYAML : {'OK' if has_yaml else 'MISSING'}")
    if not has_yaml:
        missing.append("pyyaml")

    if not missing:
        print("\nALL_OK")
        return 0

    pip = f'"{sys.executable}" -m pip install -U'
    if osname == "Linux":
        pip += " --break-system-packages"
    print("\nINSTALL COMMANDS:")
    py_pkgs = [m for m in missing if m in ("yt-dlp", "pyyaml")]
    if py_pkgs:
        print(f"{pip} {' '.join(py_pkgs)}")
    if "ffmpeg" in missing:
        if osname == "Windows":
            print("winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements")
            print("(then close and reopen the terminal so ffmpeg is on PATH)")
        elif osname == "Darwin":
            print("brew install ffmpeg")
        else:
            print("sudo apt-get install -y ffmpeg  ||  pip install imageio-ffmpeg (fallback)")
    return 1


if __name__ == "__main__":
    sys.exit(main())

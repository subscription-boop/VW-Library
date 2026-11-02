#!/usr/bin/env python3
"""Processed index of the SFX library folder (the sfx/ folder of the system folder).

Builds or updates `_index/sfx_index.json` with acoustic features for every sound file, so new sounds
(e.g. events heard in a reference video) can be compared without listening again.

Usage:
  python sfx_index.py <SFX root>            # add new/changed files, drop removed ones (incremental, by size+mtime)
  python sfx_index.py <SFX root> --rebuild  # recompute everything
  python sfx_index.py <SFX root> --match clip.wav [--t0 1.2 --t1 1.6]   # rank library sounds against a clip

Needs: numpy, soundfile, librosa (pip install numpy soundfile librosa). ffmpeg on PATH for mp3 if soundfile cannot read it.
"""
import json, os, sys, subprocess, hashlib
import numpy as np

AUDIO = ('.wav', '.mp3', '.aif', '.aiff', '.flac', '.ogg', '.m4a')
SR = 48000
BANDS = [(20, 80), (80, 200), (200, 500), (500, 1000), (1000, 2000), (2000, 4000), (4000, 8000), (8000, 16000), (16000, 24000)]
VERSION = 2

def load(path, t0=None, t1=None):
    import soundfile as sf
    try:
        y, sr = sf.read(path, always_2d=True, dtype='float32'); y = y.mean(1)
        if sr != SR:
            import librosa; y = librosa.resample(y, orig_sr=sr, target_sr=SR)
    except Exception:
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
        y = np.frombuffer(raw, np.float32).copy()
    if t0 is not None: y = y[int(t0 * SR):int(t1 * SR) if t1 else None]
    return y

def features(y):
    import librosa
    y = y.astype(np.float32)
    peak = float(np.abs(y).max() + 1e-9)
    hop = 240  # 5 ms
    env = librosa.feature.rms(y=y, frame_length=960, hop_length=hop)[0] + 1e-9
    envdb = 20 * np.log10(env / env.max())
    act = np.where(envdb > -40)[0]
    a0, a1 = (act[0], act[-1]) if len(act) else (0, len(env) - 1)
    pk = int(np.argmax(env))
    dur_active = (a1 - a0 + 1) * hop / SR
    attack = max(pk - a0, 0) * hop / SR
    after = envdb[pk:a1 + 1]
    decay20 = (np.argmax(after < -20) if (after < -20).any() else len(after)) * hop / SR
    seg = y[a0 * hop:(a1 + 1) * hop + 960] if a1 > a0 else y
    S = np.abs(librosa.stft(seg, n_fft=2048, hop_length=512)) ** 2 + 1e-12
    f = librosa.fft_frequencies(sr=SR, n_fft=2048)
    tot = S.sum()
    bands = [float(10 * np.log10(S[(f >= lo) & (f < hi)].sum() / tot + 1e-12)) for lo, hi in BANDS]
    cen = librosa.feature.spectral_centroid(S=np.sqrt(S), sr=SR)[0]
    flat = librosa.feature.spectral_flatness(S=np.sqrt(S))[0]
    mf = librosa.feature.mfcc(S=librosa.power_to_db(librosa.feature.melspectrogram(S=S, sr=SR, n_mels=64)), n_mfcc=20)
    # centroid trend: rising (riser/whoosh-in), falling (drop), flat
    n = len(cen); third = max(n // 3, 1)
    trend = float(np.log2((np.median(cen[-third:]) + 1) / (np.median(cen[:third]) + 1)))
    shape = np.interp(np.linspace(0, len(envdb[a0:a1 + 1]) - 1, 32), np.arange(len(envdb[a0:a1 + 1])), envdb[a0:a1 + 1]).round(1).tolist() if a1 > a0 else [0.0] * 32
    # separate hits (keyboard / clicks): onsets
    on = librosa.onset.onset_detect(y=seg, sr=SR, hop_length=256, units='time', backtrack=True)
    loud = float(20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9))
    return dict(duration_file=round(len(y) / SR, 3), duration_active=round(dur_active, 3), attack_s=round(attack, 3), decay20_s=round(decay20, 3),
                peak_dbfs=round(20 * np.log10(peak), 1), rms_dbfs=round(loud, 1),
                centroid_hz=round(float(np.median(cen)), 0), centroid_trend_oct=round(trend, 2), flatness=round(float(np.median(flat)), 3),
                bands_db=[round(b, 1) for b in bands], mfcc_mean=mf.mean(1).round(2).tolist(), mfcc_std=mf.std(1).round(2).tolist(),
                env_shape_db=shape, onsets=len(on), onset_times=[round(float(x) + a0 * hop / SR, 3) for x in on[:400]])

def classify(F):
    d, at, cen, fl, tr, on = F['duration_active'], F['attack_s'], F['centroid_hz'], F['flatness'], F['centroid_trend_oct'], F['onsets']
    low = F['bands_db'][0] + 0 > -12 or F['bands_db'][1] > -8
    if on >= 6 and d > 1.0 and cen > 1500: return 'multi-hit clicks (keys/typing/clicks)'
    if d < 0.25 and at < 0.02: return 'click / tick' if cen > 1500 else 'short thump'
    if tr > 0.7 and d > 0.8: return 'riser / rising sweep'
    if low and at < 0.05 and d > 0.5: return 'hit / impact (low end)' if tr > -0.6 else 'sub drop / falling impact'
    if at >= 0.05 and fl > 0.02 and d < 2.5: return 'whoosh (noise swell)'
    if at < 0.03: return 'hit / impact'
    return 'texture / other'


def write_md(idx, root):
    F = idx['files']
    L = ['# SFX library index', '', 'Processed index of this SFX library folder (`settings.json` -> `paths.sfx` in the video system) so sounds can be compared without listening again. Machine data: `sfx_index.json` (features per file). Update: `python sfx_index.py "<SFX folder>"` (incremental) after adding files; Claude also updates it in the cloud and writes it back. Overview picture: `spectrograms.png`.', '',
         'Columns: active length, attack (time to peak), brightness (spectral centroid). `from-references/` holds sounds extracted from reference videos (source in the Source column). `_index/cuts/` holds ready single hits cut from long multi-hit files.', '',
         '| File | Type | Description | Active | Attack | Brightness | Tags | Source |', '| :- | :- | :- | -: | -: | -: | :- | :- |']
    for k, e in sorted(F.items()):
        L.append(f"| {k} | {e.get('class_manual', e['class'])} | {e.get('notes', '')} | {e['duration_active']:.2f} s | {e['attack_s']:.2f} s | {e['centroid_hz']:.0f} Hz | {', '.join(e.get('tags', []))} | {e.get('source', 'library')} |")
    cuts = [(k, c) for k, e in sorted(F.items()) for c in e.get('cuts', [])]
    if cuts:
        L += ['', '## Ready cuts', '', '| Cut | From | Note |', '| :- | :- | :- |']
        for k, c in cuts:
            L.append(f"| {c['file']} | {k} @ {c['src_time']} s | spectral distance to the src-003 typing click: {c.get('dist_to_src003_click', '-')} (lower = closer) |")
    open(os.path.join(root, '_index', 'INDEX.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')

def key(path):
    st = os.stat(path); return f'{st.st_size}-{int(st.st_mtime)}'

def scan(root):
    out = []
    for dp, dn, fn in os.walk(root):
        if '_index' in dp.split(os.sep): continue
        for f in fn:
            if f.lower().endswith(AUDIO): out.append(os.path.join(dp, f))
    return sorted(out)

def update(root, rebuild=False):
    ip = os.path.join(root, '_index', 'sfx_index.json')
    idx = json.load(open(ip)) if (os.path.exists(ip) and not rebuild) else {'version': VERSION, 'files': {}}
    files = scan(root); seen = set(); changed = 0
    for p in files:
        rel = os.path.relpath(p, root).replace('\\', '/'); seen.add(rel)
        k = key(p); e = idx['files'].get(rel)
        if e and e.get('key') == k and idx.get('version') == VERSION: continue
        F = features(load(p)); F['class'] = classify(F); F['key'] = k
        if e:  # keep human notes
            for kk in ('notes', 'tags', 'source', 'class_manual', 'cuts'): 
                if kk in e: F[kk] = e[kk]
        idx['files'][rel] = F; changed += 1; print('indexed', rel, F['class'])
    for rel in list(idx['files']):
        if rel not in seen: del idx['files'][rel]; print('removed', rel)
    idx['version'] = VERSION
    os.makedirs(os.path.dirname(ip), exist_ok=True); json.dump(idx, open(ip, 'w'), indent=1)
    write_md(idx, root)
    print(f'{len(files)} files, {changed} (re)indexed')
    return idx

def vec(F):
    return np.array(F['bands_db'] + [x / 10 for x in F['mfcc_mean'][1:13]] + [np.log2(F['duration_active'] + 0.02) * 3, np.log2(F['attack_s'] + 0.005) * 2,
                    np.log2(F['centroid_hz'] + 50) * 2, F['centroid_trend_oct'] * 3, F['flatness'] * 20] + [x / 10 for x in F['env_shape_db'][::4]], np.float32)

def match(idx, F, top=8):
    v = vec(F); res = []
    for rel, e in idx['files'].items():
        res.append((float(np.linalg.norm(vec(e) - v)), rel, e.get('class_manual') or e['class']))
    return sorted(res)[:top]

if __name__ == '__main__':
    root = sys.argv[1]
    if '--match' in sys.argv:
        clip = sys.argv[sys.argv.index('--match') + 1]
        t0 = float(sys.argv[sys.argv.index('--t0') + 1]) if '--t0' in sys.argv else None
        t1 = float(sys.argv[sys.argv.index('--t1') + 1]) if '--t1' in sys.argv else None
        idx = json.load(open(os.path.join(root, '_index', 'sfx_index.json')))
        F = features(load(clip, t0, t1))
        for d, rel, c in match(idx, F): print(f'{d:6.2f}  {rel}  [{c}]')
    else:
        update(root, '--rebuild' in sys.argv)

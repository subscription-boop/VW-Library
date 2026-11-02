# per-frame tracking from the rough cut + person matte:
#   head top / centre (for chest captions and the colour ripple origin)
#   table edge line (the wall colour must stop at the white desk)
import numpy as np, subprocess, json, cv2
W,H=1080,1920
def frames(path,pix,ch):
    p=subprocess.Popen(['ffmpeg','-v','error','-i',path,'-f','rawvideo','-pix_fmt',pix,'-'],stdout=subprocess.PIPE)
    n=W*H*ch
    while True:
        b=p.stdout.read(n)
        if len(b)<n: break
        yield np.frombuffer(b,np.uint8).reshape(H,W,ch) if ch>1 else np.frombuffer(b,np.uint8).reshape(H,W)
cuts=sorted({round(c['out0']*25) for c in json.load(open('cutlist_rc.json'))})
out=[]
for i,(rgb,al) in enumerate(zip(frames('roughcut.mp4','rgb24',3),frames('matte.mp4','gray',1))):
    a=al>128
    rows=np.where(a[:,200:900].sum(1)>25)[0]
    top=int(rows[0]) if len(rows) else 600
    band=a[top:top+220]
    xs=np.where(band.any(0))[0]
    cx=float(np.mean(np.where(band)[1])) if band.any() else W/2
    # desk far edge: on columns left of the person, the strongest dark->bright step going down (wall -> white desk)
    lum=cv2.GaussianBlur(rgb[...,1].astype(np.float32),(0,0),3)
    cols=np.where(a[1150:1750].any(0))[0]
    left=int(cols[0]) if len(cols) else W
    pts=[]
    for x in range(8,max(8,left-30),12):
        col=lum[1250:1750,x]; gr=col[6:]-col[:-6]
        j=int(np.argmax(gr))
        if gr[j]>12 and col[j+6:j+40].mean()>185: pts.append((x,1250+j+3))
    out.append(dict(top=top,cx=cx,pts=pts))
print('frames',len(out))
# fit table line per frame (robust), then smooth inside each shot
def fit(pts):
    if len(pts)<4: return None
    p=np.array(pts,float)
    for _ in range(3):
        k,b=np.polyfit(p[:,0],p[:,1],1); r=np.abs(p[:,1]-(k*p[:,0]+b))
        keep=r<max(12,np.median(r)*2.5)
        if keep.sum()<4: break
        p=p[keep]
    return k,b
bounds=cuts+[len(out)]
res=[]
for s_,e_ in zip(bounds[:-1],bounds[1:]):
    P=[p for o in out[s_:e_] for p in o['pts']]
    f=fit(P)
    if f is None: k,b=-0.1,1420
    else:
        k,b=f
        if not -0.25<=k<=0.05:   # keep the slope sane, re-anchor at the mean point
            pm=np.array(P,float).mean(0); k=float(np.clip(k,-0.25,0.05)); b=pm[1]-k*pm[0]
    s,e=s_,e_
    tops=np.array([o['top'] for o in out[s:e]],float); cxs=np.array([o['cx'] for o in out[s:e]],float)
    def sm(v,r=4):
        return np.array([np.median(v[max(0,j-r):j+r+1]) for j in range(len(v))])
    tops,cxs=sm(tops),sm(cxs)
    for j in range(e-s): res.append(dict(top=float(tops[j]),cx=float(cxs[j]),k=float(k),b=float(b)))
json.dump(res,open('track.json','w'))
for s in bounds[:-1]: print(s,res[s])

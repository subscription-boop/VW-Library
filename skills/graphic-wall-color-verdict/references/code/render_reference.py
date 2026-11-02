# Img 0097 - green flag / red flag: wall turns green (chime) or red (buzz) on each answer
import numpy as np, cv2, json, subprocess, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,25
BF='/home/claude/brand/astroshot/fonts/'
GREEN=np.array([1,241,124],np.float32); RED=np.array([255,52,62],np.float32)
WHITE=(255,255,255)
EV=json.load(open('events.json'))          # answers, intro flashes, question onsets
WORDS=json.load(open('captions.json'))     # chest captions + keyword stacks
TR=json.load(open('track.json'))
# ---- grade C (grade-soft-warm-natural), speaker footage only
_G=np.linspace(0,1,256,dtype=np.float32)**2.2
def _s(x,a): return np.where(x<.5,.5*(2*x)**a,1-.5*(2*(1-x))**a)
LUT=np.stack([_s(np.clip(_G*k*1.06,0,1)**(1/2.2),1.06) for k in (1.05,1.0,0.92)],1).astype(np.float32)
def grade(rgb):
    x=np.stack([LUT[rgb[...,c],c] for c in range(3)],-1); g=x.mean(2,keepdims=True)
    return np.clip(g+(x-g)*1.03,0,1)*255
def eo(u): u=min(max(u,0.0),1.0); return 1-(1-u)**3
YY,XX=np.mgrid[0:H,0:W].astype(np.float32)
# ---- wall colour state at time t
def wall_state(t):
    """returns (colour, amount 0..1, reveal radius px or None, ring list, shake px, zoom)"""
    for e in EV['looks']:
        if e['t0']-0.001<=t<e['t1']:
            u=t-e['t0']; fade=1.0
            if t>e['t1']-e['fade']: fade=max(0.0,(e['t1']-t)/e['fade'])
            col=GREEN if e['c']=='g' else RED
            amt=e['amt']*fade
            rings=[]; shake=0.0; zoom=1.0; rad=None
            if e['c']=='g':
                # chime: note 1 = colour floods out from behind the head; note 2 (+0.12 s) = second ripple
                rad=eo(u/0.30)*2300
                for d in (0.0,0.12):
                    v=u-d
                    if 0<=v<0.45: rings.append((eo(v/0.45)*2400, (1-v/0.45)))
                if e.get('pop',1): zoom=1+0.022*math.exp(-u/0.16)*min(1,u/0.04)
            else:
                # buzz: colour slams in, flickers with the buzz and the frame judders, decaying over ~0.5 s
                if e.get('pop',1):
                    dec=math.exp(-u/0.20)
                    amt*=1-0.22*dec*(1 if int(u*25)%2==0 else 0)
                    shake=11*dec*math.sin(2*math.pi*12.5*u+0.6)
                    zoom=1.02
            return col,amt,rad,rings,shake,zoom
    return None,0,None,[],0.0,1.0
def wall_mask(rgb_src,alpha,tr):
    m=1-alpha
    edge=tr['k']*XX+tr['b']                      # desk edge line
    m*=np.clip((edge-6-YY)/10,0,1)
    lum=rgb_src[...,1]
    m*=np.clip((lum-95)/40,0,1)                  # keep the laptop and dark things out
    return m
# ---- text
FCAP=ImageFont.truetype(BF+'Montserrat-ExtraBold.ttf',80)
FSTK=ImageFont.truetype(BF+'Montserrat-Black.ttf',210)
_C={}
def layer(txt,font,fill):
    k=(txt,font.size,fill)
    if k in _C: return _C[k]
    bb=font.getbbox(txt); pad=40
    im=Image.new('RGBA',(bb[2]-bb[0]+2*pad,bb[3]-bb[1]+2*pad),(0,0,0,0))
    d=ImageDraw.Draw(im);
    sh=Image.new('L',im.size,0); ImageDraw.Draw(sh).text((pad-bb[0],pad-bb[1]+4),txt,font=font,fill=150)
    sh=sh.filter(ImageFilter.GaussianBlur(9)); im.paste((0,0,0,255),(0,0),sh)
    d.text((pad-bb[0],pad-bb[1]),txt,font=font,fill=fill+(255,))
    _C[k]=(im,pad,bb); return _C[k]
def track_word(img,t,fr):
    """chest captions or keyword stack"""
    tr=TR[min(fr,len(TR)-1)]
    cy=tr['top']+0.170*H; cx=tr['cx']
    cur=None
    for w in WORDS:
        if w['s']<=t<w['e']: cur=w
    if not cur: return
    if cur['kind']=='cap':
        im,pad,bb=layer(cur['txt'],FCAP,WHITE)
        img.alpha_composite(im,(int(cx-im.width/2),int(cy-im.height/2)))
    else:
        lines=[l for l in cur['lines'] if l['s']<=t]
        y=cy-15
        ws=[]
        for l in lines:
            im,pad,bb=layer(l['txt'],FSTK,tuple(l.get('rgb',WHITE)))
            ws.append(im.width-2*pad)
        sc=min(1.0,0.75*W/max(ws)) if ws else 1
        for l in lines:
            im,pad,bb=layer(l['txt'],FSTK,tuple(l.get('rgb',WHITE)))
            if sc<1: im=im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS); pad=int(pad*sc)
            x=int(max(36,min(W-36-(im.width-2*pad),cx-(im.width-2*pad)/2))-pad)
            img.alpha_composite(im,(x,int(y-pad)))
            y+=FSTK.size*0.88*sc
def frames(path,pix,ch):
    p=subprocess.Popen(['ffmpeg','-v','error','-i',path,'-f','rawvideo','-pix_fmt',pix,'-'],stdout=subprocess.PIPE)
    n=W*H*ch
    while True:
        b=p.stdout.read(n)
        if len(b)<n: break
        yield np.frombuffer(b,np.uint8).reshape((H,W,ch) if ch>1 else (H,W))
def render_frame(rgb,al,fr):
    t=fr/FPS; tr=TR[min(fr,len(TR)-1)]
    src=rgb.astype(np.float32); g=grade(rgb)
    col,amt,rad,rings,shake,zoom=wall_state(t)
    if col is not None and amt>0.001:
        a=al.astype(np.float32)/255   # v002: matte from RVM ResNet50 (keeps the chair out of the person, so it takes the full wall colour)
        m=wall_mask(src,a,tr)
        ox,oy=tr['cx'],tr['top']+120
        if rad is not None or rings:
            dist=np.sqrt((XX-ox)**2+(YY-oy)**2)
        if rad is not None and rad<2600:
            m=m*np.clip((rad-dist)/160,0,1)
        lum=g.mean(2,keepdims=True)
        ref=np.median(lum[m>0.5]) if (m>0.5).sum()>500 else 180
        shade=np.clip(lum/ref,0.55,1.25)
        paint=col[None,None,:]*shade*0.97
        for r,s in rings:   # bright ripple fronts
            band=np.exp(-((dist-r)/70)**2)*0.35*s
            paint=paint+band[...,None]*255
        paint=np.clip(paint,0,255)
        k=(m*amt)[...,None]
        g=g*(1-k)+paint*k
    out=Image.fromarray(np.clip(g+.5,0,255).astype(np.uint8)).convert('RGBA')
    track_word(out,t,fr)
    o=np.asarray(out.convert('RGB'))
    if abs(shake)>0.05 or abs(zoom-1)>1e-4:
        M=cv2.getRotationMatrix2D((W/2,H*0.45),0,zoom); M[0,2]+=shake
        o=cv2.warpAffine(o,M,(W,H),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
    return o
if __name__=='__main__':
    only=[int(x) for x in sys.argv[1:]]
    if only:
        fs=set(only)
        for fr,(rgb,al) in enumerate(zip(frames('roughcut.mp4','rgb24',3),frames('matte.mp4','gray',1))):
            if fr in fs: Image.fromarray(render_frame(rgb,al,fr)).save(f'../previews/r_{fr:04d}.jpg',quality=88)
            if fr>max(fs): break
        sys.exit()
    wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-c:v','libx264','-preset','medium','-crf','16','-pix_fmt','yuv420p','pic.mp4'],stdin=subprocess.PIPE)
    n=0
    for fr,(rgb,al) in enumerate(zip(frames('roughcut.mp4','rgb24',3),frames('matte.mp4','gray',1))):
        wr.stdin.write(render_frame(rgb,al,fr).tobytes()); n+=1
        if n%100==0: print(n,flush=True)
    wr.stdin.close(); wr.wait(); print('done',n)

"""grade-warm-bright: reference implementation (8-bit RGB frame in, 8-bit RGB frame out).
One way to reproduce the look; any tool may be used as long as the result matches references/before-after.jpg."""
import numpy as np
_G=np.linspace(0,1,256,dtype=np.float32)**2.2
def _mask_soft(h,w,cx=0.5,cy=0.40):
    yy,xx=np.mgrid[0:h,0:w].astype(np.float32)
    d=np.sqrt(((xx/w-cx)/0.70)**2+((yy/h-cy)/0.70)**2)
    return np.clip(1-0.14*np.clip((d-0.45)/0.75,0,1)**1.6,0.86,1).astype(np.float32)
def _curve_soft(x):
    s=np.where(x<0.5,0.5*(2*x)**1.12,1-0.5*(2*(1-x))**1.10)
    return 0.025+s*0.965
def grade(rgb):
    """warm & bright: ~+1000K warmer, +6% exposure with a very soft centre-weighted falloff,
    gentle S-curve with lifted blacks, +6% saturation, warm-brown shadows, golden highlights"""
    lin=_G[rgb].copy()
    lin[...,0]*=1.12; lin[...,1]*=1.025; lin[...,2]*=0.82
    lin*=(1.06*_mask_soft(*rgb.shape[:2]))[...,None]
    out=np.clip(lin,0,1)**(1/2.2)
    out=_curve_soft(out)
    g=out.mean(2,keepdims=True); out=g+(out-g)*1.06
    lum=out.mean(2,keepdims=True)
    out=out+np.clip(1-lum*2.2,0,1)*np.array([0.020,0.010,-0.006],np.float32)
    out=out+np.clip((lum-0.55)*2,0,1)*np.array([0.012,0.006,-0.012],np.float32)
    return (np.clip(out,0,1)*255+0.5).astype(np.uint8)

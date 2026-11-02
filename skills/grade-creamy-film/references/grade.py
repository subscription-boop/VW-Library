"""grade-creamy-film: reference implementation (8-bit RGB frame in, 8-bit RGB frame out).
One way to reproduce the look; any tool may be used as long as the result matches references/before-after.jpg."""
import numpy as np
_G=np.linspace(0,1,256,dtype=np.float32)**2.2
def _wb(rgb,r,g,b):
    l=_G[rgb].copy(); l[...,0]*=r; l[...,1]*=g; l[...,2]*=b; return l
def _enc(l): return np.clip(l,0,1)**(1/2.2)
def _out(x): return (np.clip(x,0,1)*255+.5).astype(np.uint8)
def _sat(x,k): g=x.mean(2,keepdims=True); return g+(x-g)*k
def _s(x,a): return np.where(x<.5,.5*(2*x)**a,1-.5*(2*(1-x))**a)
def _tone(x,lift=0,gain=1): return lift+x*(gain-lift)
def _lum(x): return x.mean(2,keepdims=True)

def grade(rgb):      # F
    x=_enc(_wb(rgb,1.08,1.02,0.88)*1.08); x=_tone(x,0.06,0.97); x=_s(x,1.04); x=_sat(x,0.85)
    return _out(x+np.clip(0.5-_lum(x),0,1)*np.array([0.02,0.01,0.0]))

# Robust Video Matting -> alpha as grayscale mp4 (same fps/size as input)
import onnxruntime as ort, numpy as np, subprocess, sys
src,dst=sys.argv[1],sys.argv[2]
W,H=1080,1920
sess=ort.InferenceSession('/home/claude/models/rvm_resnet50_fp32.onnx',providers=['CPUExecutionProvider'])
rec=[np.zeros([1,1,1,1],np.float32)]*4
dr=np.array([0.25],np.float32)
rd=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
wr=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','gray','-s',f'{W}x{H}','-r','25','-i','-','-c:v','libx264','-crf','12','-pix_fmt','yuv420p',dst],stdin=subprocess.PIPE)
import json
cuts={round(c['out0']*25) for c in json.load(open('cutlist_rc.json'))}
n=0
while True:
    b=rd.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    if n in cuts: rec=[np.zeros([1,1,1,1],np.float32)]*4
    x=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.float32).transpose(2,0,1)[None]/255
    fgr,pha,*rec=sess.run(None,{'src':x,'r1i':rec[0],'r2i':rec[1],'r3i':rec[2],'r4i':rec[3],'downsample_ratio':dr})
    wr.stdin.write((pha[0,0]*255).clip(0,255).astype(np.uint8).tobytes()); n+=1
wr.stdin.close(); wr.wait(); print('frames',n)

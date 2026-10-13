import sys
from PIL import Image, ImageFilter, ImageDraw
import numpy as np
from collections import deque
def cut(src,dst,thr=235):
    im=Image.open(src).convert('RGB'); a=np.array(im).astype(int)
    h,w,_=a.shape
    white=(a.min(axis=2)>=thr)
    mask=np.zeros((h,w),bool); q=deque()
    for x in range(w):
        for y in (0,h-1):
            if white[y,x]: mask[y,x]=True; q.append((y,x))
    for y in range(h):
        for x in (0,w-1):
            if white[y,x] and not mask[y,x]: mask[y,x]=True; q.append((y,x))
    while q:
        y,x=q.popleft()
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and white[ny,nx] and not mask[ny,nx]:
                mask[ny,nx]=True; q.append((ny,nx))
    alpha=Image.fromarray(((~mask)*255).astype('uint8')).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
    out=im.convert('RGBA'); out.putalpha(alpha); out.save(dst)
    print(dst, (~mask).mean())
cut(sys.argv[1],sys.argv[2],int(sys.argv[3]))

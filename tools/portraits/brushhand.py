import numpy as np, os, json, sys
from PIL import Image
from skimage.morphology import skeletonize
from scipy.ndimage import distance_transform_edt, gaussian_filter
sys.path.insert(0, os.path.dirname(__file__))
from marks2 import brush
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=os.path.join(B,'hand2'); OUT=os.path.join(B,'hand3'); os.makedirs(OUT,exist_ok=True)
N8=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def trace(sk):
    pts=set(zip(*np.nonzero(sk)))
    nb=lambda p:[(p[0]+a,p[1]+b) for a,b in N8 if (p[0]+a,p[1]+b) in pts]
    deg={p:len(nb(p)) for p in pts}
    nodes={p for p in pts if deg[p]!=2}
    used=set(); paths=[]
    def walk(s,n):
        path=[s,n]; used.add(frozenset((s,n))); prev,cur=s,n
        while cur not in nodes:
            nxt=[q for q in nb(cur) if q!=prev and frozenset((cur,q)) not in used]
            if not nxt: break
            q=nxt[0]; used.add(frozenset((cur,q))); path.append(q); prev,cur=cur,q
            if cur==s: break
        return path
    for s in nodes:
        for n in nb(s):
            if frozenset((s,n)) not in used: paths.append(walk(s,n))
    for s in pts:  # loops
        for n in nb(s):
            if frozenset((s,n)) not in used: paths.append(walk(s,n))
    return paths
def merge_short(paths, minlen=6): return [p for p in paths if len(p)>=minlen]
meta={}
for f in sorted(os.listdir(SRC)):
    if not f.endswith('.png') or f in('ink.png','prev.png'): continue
    k=f[:-4]; m=np.asarray(Image.open(os.path.join(SRC,f)).split()[-1],float)/255
    mb=gaussian_filter(m,1.2)>0.35
    sk=skeletonize(mb); dt=distance_transform_edt(mb)
    th=float(np.median(dt[sk]))*2
    pad=int(th*2.2)+10
    H,W=m.shape; size=(W+2*pad,H+2*pad)
    acc=np.zeros((size[1],size[0]))
    paths=merge_short(trace(sk))
    for i,p in enumerate(paths):
        P=np.array([(x+pad,y+pad) for y,x in p],float)
        # thin to every 3rd point and smooth lightly
        if len(P)>8: P=P[::3]
        if len(P)<3: P=np.vstack([P[0],(P[0]+P[-1])/2,P[-1]])
        w=th*1.15
        L=np.sum(np.hypot(*np.diff(P,axis=0).T))
        im=brush(P,w,size,seed=hash((k,i))%10**6,dry=0.3 if L>60 else 0.05,ss=2,pool=False,splat=False)
        acc=np.maximum(acc,np.asarray(im,float)/255)
    a=(np.clip(acc,0,1)*255).astype(np.uint8)
    img=Image.fromarray(a); bb=img.getbbox(); img=img.crop(bb)
    Image.merge('RGBA',[Image.new('L',img.size,255)]*3+[img]).save(os.path.join(OUT,f),optimize=True)
    meta[k]=list(img.size); print(k,img.size,len(paths),round(th,1))
json.dump(meta,open(os.path.join(OUT,'meta.json'),'w'))

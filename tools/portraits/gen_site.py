import json, os, re, shutil, sys
sys.argv=[sys.argv[0]]
import gen29 as G
from PIL import Image
B=G.B; REPO='/home/claude/kilianamrehn.com'
PUB=os.path.join(REPO,'public/media/portraits'); os.makedirs(PUB,exist_ok=True)
used=set()
def T(name):
    if name.startswith('G_'): src=os.path.join(B,'..','hand3',name[2:]+'.png'); out='h-'+name[2:]+'.png'
    elif name.startswith('M_'): src=os.path.join(B,'marks2',name[2:]+'.png'); out=name[2:]+'.png'
    else:
        src=os.path.join(B,'tex2' if name in G.meta2 else 'tex',name+'.png'); out=name+'.png'
    if out not in used: shutil.copy(src,os.path.join(PUB,out)); used.add(out)
    return '__B__media/portraits/'+out
G.T=T
slugs={x['fid']:x['slug'] for x in json.load(open(os.path.join(B,'..','r20','slugs.json')))}
PX=re.compile(r'(-?\d*\.?\d+)px')
def cv(s): return PX.sub(lambda m: f'calc({m.group(1)}*var(--u))', s)
def conv(sheet):
    imgs=[]
    for i in sheet['imgs']:
        f=i['fid']; slug=slugs[f if f in slugs else f]
        im=Image.open(os.path.join(REPO,'src/assets/img',slug+'.jpg'))
        m=re.search(r'width:([\d.]+)px;height:([\d.]+)px',i['is_']); w,h=float(m.group(1)),float(m.group(2))
        r1=im.width/im.height; r2=w/h
        if abs(r1/r2-1)>0.02: print('RATIO',slug,round(r1,3),round(r2,3))
        imgs.append({'slug':slug,'video':bool(i['vsrc']),'wrap':cv('top:%spx;'%i['lt']+i['wrap']),'is':cv(i['is_']),'s1':cv(i['s1']),'t1':i['t1'],'s2':cv(i['s2']),'t2':i['t2'],
                     'nm':i['nm'],'cat':i['cat'],'named':i['named'],'year':i['year'],'e':i['e1'],'fnum':i['fnum'],'cap':i['cap']})
    dd=lambda L:[{'s':cv('top:%spx;'%d['lt']+d['s']),'t':d['t']} for d in L]
    return {'h':sheet['h'],'imgs':imgs,'back':dd(sheet['back']),'front':dd(sheet['front'])}
D=G.build(5,False); M=G.build(5,True)
def slugify(s):
    s=s.lower().replace('é','e').replace('ü','ue').replace('ö','oe').replace('ä','ae')
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
out=[]
for d,m in zip(D,M):
    anchors=[]
    for i in d['imgs']:
        if i['named']:
            a=slugify(i['nm'])
            if a not in anchors: anchors.append(a)
    out.append({'top':d['top'],'bg':d['bg'],'anchors':anchors,'d':conv(d),'m':conv(m)})
json.dump(out,open(os.path.join(REPO,'src/data/portraits.json'),'w'),ensure_ascii=False)
print(len(out),[s['anchors'] for s in out], sorted(used)[:5], len(used))

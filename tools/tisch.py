# Tisch-Layouts für Arbeiten und Flashes: Bilder in Rahmen (Polaroid, Negativ, Abzug, gerissen, ohne)
# auf farbigen Papierbögen, dahinter einzeln gemalte Pinselspuren (jede pro Seite nur einmal).
# Ausgabe: src/data/tisch/*.json. Alle Maße in u (1u = 1px bei 1440 bzw. 390 Breite).
# Aufruf: python3 tools/tisch.py
import json, os, random, math, colorsys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(R, *p)
IM = json.load(open(D('src/data/imgmeta.json')))
VM = json.load(open(D('src/data/vidmeta.json')))
COL = json.load(open(D('src/data/imgcolor.json')))
MM = json.load(open(D('tools/marks_meta.json')))
OUT = D('src/data/tisch'); os.makedirs(OUT, exist_ok=True)

FR = {'polaroid': (18, 18, 74), 'border': (12, 12, 12), 'negative': (16, 40, 40), 'torn': (16, 16, 16), 'plain': (0, 0, 0)}
SHADOW = "box-shadow:0 1px 1px rgba(0,0,0,0.28),0 4px 8px rgba(0,0,0,0.16),0 18px 34px -12px rgba(0,0,0,0.45);"
PAPERS = [(15, '#3b1515'), (35, '#4a2514'), (55, '#4a3a17'), (90, '#30351a'), (160, '#17321f'), (190, '#123333'), (215, '#14293b'), (260, '#181d3a'), (340, '#301930'), (361, '#3b1515')]
CHAR = '#1f1d1b'
KI = {'untamed-ki-1', 'untamed-ki-2', 'untamed-ki-3', 'untamed-ki-4', 'jeremiah-ki-1', 'jeremiah-ki-2', 'jeremiah-ki-3'}

def hsl(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h % 1, l, s)
    return '#%02x%02x%02x' % tuple(round(v * 255) for v in (r, g, b))
def paper_for(h):
    d = (h * 360) % 360
    for lim, c in PAPERS:
        if d < lim: return c
def size(name):
    if name in IM: return IM[name][0], IM[name][1]
    return VM[name][0], VM[name][1]
def hue(name): return COL.get(name, {}).get('h')
def isbw(name): return COL.get(name, {}).get('bw', False)

def torn_clip(rnd, n=34, depth=1.1):
    pts = []
    for side in range(4):
        for i in range(n):
            t = i / n * 100; j = rnd.uniform(0, depth)
            pts.append([(t, j), (100 - j, t), (100 - t, 100 - j), (j, 100 - t)][side])
    return 'polygon(' + ','.join('%.1f%% %.1f%%' % p for p in pts) + ')'

def mask(url, color, x, y, w, h, z, extra=''):
    return {'lt': round(y), 's': f"position:absolute;left:{x:.0f}px;width:{w:.0f}px;height:{h:.0f}px;background:{color};-webkit-mask-image:url(__B__media/marks/{url});mask-image:url(__B__media/marks/{url});-webkit-mask-size:100% 100%;mask-size:100% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;z-index:{z};pointer-events:none;{extra}"}

def frame_item(name, kind, x, y, w, ih, rnd, paper, edge, fnum, rot=None, z=10, ki_label=True, fs=1.0):
    px, pt, pb = [round(v * fs) for v in FR[kind]]; fw, fh = w + 2 * px, ih + pt + pb
    if rot is None:
        rot = 0.0 if kind == 'negative' else rnd.uniform(-2.2, 2.2) if kind in ('polaroid', 'torn') else rnd.uniform(-1.1, 1.1) if kind == 'border' else (rnd.uniform(-0.8, 0.8) if rnd.random() < 0.35 else 0)
    wrap = f"position:absolute;left:{x:.0f}px;width:{fw}px;height:{fh}px;transform:rotate({rot:.2f}deg);z-index:{z};"
    it = {'name': name, 'video': name not in IM, 'lt': round(y), 'is': f"display:block;width:{w}px;height:{ih}px;position:absolute;left:{px}px;top:{pt}px;", 'e': None, 'fnum': None, 'sp': None, 'ki': name in KI and ki_label}
    if kind == 'plain': wrap += SHADOW
    elif kind == 'border': wrap += 'background:#f3f0e9;' + SHADOW
    elif kind == 'polaroid': wrap += 'background:#f1eee6;background-image:linear-gradient(180deg,rgba(255,255,255,0.35),rgba(0,0,0,0.03));' + SHADOW
    elif kind == 'torn': wrap += f"background:#f3efe6;clip-path:{torn_clip(rnd)};filter:drop-shadow(0 8px 14px rgba(0,0,0,0.35));"
    elif kind == 'negative':
        wrap += 'background:#121110;' + SHADOW
        it['e'] = edge; it['fnum'] = fnum
        fz = max(7, round(10 * fs)); off = round(22 * fs); so = round(5 * fs); sh = round(14 * fs)
        it['s1'] = f"font:500 {fz}px/1 'Geist Mono Variable','Geist Mono',monospace;letter-spacing:0.2em;color:#d9823a;display:flex;padding:0 {round(14*fs)}px;box-sizing:border-box;white-space:nowrap;overflow:hidden;position:absolute;left:0;right:0;height:{sh}px;align-items:center;top:{off}px"
        it['s2'] = it['s1'].replace(f'top:{off}px', f'bottom:{off}px')
        it['sp'] = f"position:absolute;left:4px;width:{fw - 8}px;height:{sh}px;background:{paper};-webkit-mask-image:url(__B__media/marks/sprocket.png);mask-image:url(__B__media/marks/sprocket.png);-webkit-mask-size:{2*sh}px {sh}px;mask-size:{2*sh}px {sh}px;-webkit-mask-repeat:repeat-x;mask-repeat:repeat-x;pointer-events:none;"
        it['spt'] = so; it['spb'] = so
    it['wrap'] = wrap; it['fw'] = fw; it['fh'] = fh; it['x'] = round(x)
    return it

def pick_kind(name, rnd, allow_torn=False):
    if name not in IM: return rnd.choice(['plain', 'plain', 'border'])
    ks = ['plain'] * 7 + ['border'] * 4 + ['polaroid'] * 4 + ['negative'] * 4 + (['torn'] * 2 if allow_torn else [])
    return rnd.choice(ks)

def layout_rows(names, kinds, rnd, mobile, top0, maxh=None):
    W = 390 if mobile else 1440; M = 14 if mobile else 44; avail = W - 2 * M
    asp = [size(n)[0] / size(n)[1] for n in names]; n = len(names)
    rows, i = [], 0
    while i < n:
        if mobile:
            if i + 1 < n and asp[i] < 1 and asp[i + 1] < 1 and rnd.random() < 0.55: rows.append([i, i + 1]); i += 2
            else: rows.append([i]); i += 1
            continue
        cap = rnd.uniform(1.6, 2.5); r, s = [], 0
        while i < n and (not r or s + asp[i] <= cap): r.append(i); s += asp[i]; i += 1
        rows.append(r)
    rects = [None] * n; y = top0
    for r in rows:
        gap = rnd.uniform(14, 22) if mobile else rnd.uniform(26, 48)
        fill = (rnd.uniform(0.9, 1.0) if len(r) > 1 else rnd.uniform(0.8, 0.96)) if mobile else (rnd.uniform(0.86, 0.97) if len(r) > 1 else rnd.uniform(0.6, 0.8))
        pads = sum(2 * FR[kinds[ii]][0] for ii in r)
        kf = {ii: (1.28 if asp[ii] < 1 and len(r) > 1 and any(asp[jj] >= 1 for jj in r) else 1.0) for ii in r}
        h = (avail * fill - gap * (len(r) - 1) - pads) / sum(asp[ii] * kf[ii] for ii in r)
        h = min(h, 560 if mobile else 820)
        if maxh: h = min(h, maxh)
        sizes = [(h * kf[ii] * (rnd.uniform(0.9, 1.0) if len(r) > 1 else 1) * asp[ii], h * kf[ii]) for ii in r]
        sizes = [(w, w / asp[ii]) for (w, _), ii in zip(sizes, r)]
        tot = sum(w + 2 * FR[kinds[ii]][0] for (w, _), ii in zip(sizes, r)) + gap * (len(r) - 1)
        free = max(0, avail - tot); ws = [rnd.uniform(0.3, 1.7) for _ in range(len(r) + 1)]; tw = sum(ws); x = M; rowh = 0
        for j, ii in enumerate(r):
            w, ih = sizes[j]; px, pt, pb = FR[kinds[ii]]; x += free * ws[j] / tw
            dy = rnd.uniform(0, 20 if mobile else 50); fw, fh = round(w) + 2 * px, round(ih) + pt + pb
            rects[ii] = (round(x), round(y + dy), round(w), round(ih)); x += fw + gap; rowh = max(rowh, dy + fh)
        y += rowh + (rnd.uniform(22, 38) if mobile else rnd.uniform(36, 70))
    return rects, y + (30 if mobile else 60)

class Marks:
    def __init__(self, seed):
        self.pool = sorted(MM); random.Random(seed).shuffle(self.pool); self.i = 0
    def take(self):
        if self.i >= len(self.pool): self.i = 0
        k = self.pool[self.i]; self.i += 1; return k

def add_marks(back, rects_px, hues, rnd, mobile, marks, cnt):
    for _ in range(cnt):
        key = marks.take(); mw, mh, kind = MM[key]
        h0 = rnd.choice(hues)
        paint = hsl(h0 + (0.5 if rnd.random() < 0.45 else rnd.uniform(-0.04, 0.04)), rnd.uniform(0.55, 0.78), rnd.uniform(0.46, 0.6))
        x, y, fw, fh = rnd.choice(rects_px); SC = 0.42 if mobile else 1.0; op = rnd.uniform(0.82, 0.97); fl = ' scaleX(-1)' if rnd.random() < 0.5 else ''
        if kind in ('ring', 'arc'):
            d = (rnd.uniform(0.75, 1.15) * min(fw, fh) + 60 * SC) * (1.15 if kind == 'arc' else 1)
            cx = x + rnd.choice([0, fw, fw * rnd.uniform(0.2, 0.8)]) + rnd.uniform(-0.2, 0.2) * d
            cy = y + rnd.choice([0, fh, fh * rnd.uniform(0.3, 0.9)]) + rnd.uniform(-0.15, 0.15) * d
            back.append(mask(key + '.png', paint, cx - d / 2, cy - d / 2, d, d, 4, f'opacity:{op:.2f};transform:rotate({rnd.uniform(0, 360):.0f}deg){fl};'))
        elif kind == 'swipe':
            sw = min((390 if mobile else 1440), fw * rnd.uniform(1.6, 2.4)); sh = sw * mh / mw * rnd.uniform(0.75, 1.0)
            sx = x + fw / 2 - sw / 2 + rnd.uniform(-0.25, 0.25) * fw; sy = y + fh * rnd.uniform(0.2, 0.85) - sh / 2
            back.append(mask(key + '.png', paint, sx, sy, sw, sh, 4, f'opacity:{op:.2f};transform:rotate({rnd.uniform(-9, 9):.1f}deg){fl};'))
        else:
            lw = rnd.uniform(0.6, 1.1) * (360 if mobile else 1000); lh = lw * mh / mw
            lx = x + rnd.uniform(-0.4, 0.6) * fw; ly = y + rnd.choice([fh + rnd.uniform(-30, -6) * SC, rnd.uniform(0.1, 0.9) * fh])
            back.append(mask(key + '.png', paint, lx, ly, lw, lh, 4, f'opacity:{op:.2f};transform:rotate({rnd.uniform(-4, 4):.1f}deg){fl};'))

def sheet(names, paper, rnd_seed, mobile, marks, edge, label=False, cnt=None, allow_torn=False, maxh=None):
    rnd = random.Random(rnd_seed)
    kinds = [pick_kind(n, rnd, allow_torn) for n in names]
    top0 = (60 if mobile else 110) + ((40 if mobile else 50) if label else 0)
    rects, H = layout_rows(names, kinds, rnd, mobile, top0, maxh)
    imgs, back = [], []
    for k, (n, kd) in enumerate(zip(names, kinds)):
        x, y, w, ih = rects[k]
        imgs.append(frame_item(n, kd, x, y, w, ih, rnd, paper, edge, rnd.randint(2, 35), z=10 + k))
    hs = [hue(n) for n in names if hue(n) is not None and not isbw(n)] or [0.02, 0.09]
    rp = [(i['x'], i['lt'], i['fw'], i['fh']) for i in imgs]
    add_marks(back, rp, hs, rnd, mobile, marks, cnt if cnt is not None else (2 if len(names) <= 3 else rnd.choice([2, 3, 3])))
    return {'h': round(H), 'imgs': imgs, 'back': back}

def paper_of(names, fixed=None):
    if fixed: return fixed
    hs = [hue(n) for n in names if hue(n) is not None and not isbw(n) and COL[n]['sat'] > 0.12]
    bwr = sum(1 for n in names if isbw(n) or COL.get(n, {}).get('sat', 1) < 0.1) / max(1, len(names))
    if not hs or bwr >= 0.6: return CHAR
    ang = [h * 2 * math.pi for h in hs]; h = (math.atan2(sum(map(math.sin, ang)), sum(map(math.cos, ang))) / (2 * math.pi)) % 1
    return paper_for(h)

def build_arbeiten():
    P = json.load(open(D('tools/arbeiten_content.json')))
    for pi, p in enumerate(P):
        marks = Marks(1000 + pi)
        sheets = []
        for si, s in enumerate(p['sections']):
            paper = paper_of(s['items'], p.get('color'))
            dd = sheet(s['items'], paper, 31 * pi + si, False, marks, p['edge'], label=bool(s['label']) or bool(s.get('note')))
            mm = sheet(s['items'], paper, 31 * pi + si + 7, True, Marks(2000 + pi * 10 + si), p['edge'], label=bool(s['label']) or bool(s.get('note')))
            sheets.append({'bg': paper, 'label': s['label'], 'labelEn': s['labelEn'], 'note': s.get('note'), 'noteEn': s.get('noteEn'), 'd': dd, 'm': mm})
        p['color'] = p.get('color') or sheets[0]['bg']
        json.dump({'slug': p['slug'], 'sheets': sheets}, open(os.path.join(OUT, 'a-' + p['slug'] + '.json'), 'w'), ensure_ascii=False)
    # Übersicht: pro Arbeit ein kleiner Bogen mit drei Bildern
    idx = []
    for pi, p in enumerate(P):
        allimg = [n for s in p['sections'] for n in s['items'] if n in IM]
        r = random.Random(500 + pi); prev = [allimg[0]] + r.sample(allimg[1:], min(2, len(allimg) - 1))
        marks = Marks(3000 + pi)
        dd = sheet(prev, p['color'], 700 + pi, False, marks, p['edge'], label=False, cnt=2, maxh=430)
        mm = sheet(prev[:2], p['color'], 800 + pi, True, Marks(4000 + pi), p['edge'], label=False, cnt=1, maxh=300)
        idx.append({'slug': p['slug'], 'title': p['title'], 'kind': p['kind'], 'kindEn': p['kindEn'], 'year': p['year'], 'bg': p['color'], 'd': dd, 'm': mm})
    json.dump(idx, open(os.path.join(OUT, 'arbeiten-index.json'), 'w'), ensure_ascii=False)
    json.dump(P, open(D('src/data/arbeiten.json'), 'w'), ensure_ascii=False)
    print('arbeiten', len(P))

# ---------- Flashes: Haufen, Reihen, Diagonalen, Bögen, Kreise, Einzelbilder mit Luft
def flashes(mobile):
    names = sorted(n for n in IM if n.startswith('f-')) + sorted(n for n in VM if n.startswith('flash-'))
    r = random.Random(17 if not mobile else 18); r.shuffle(names)
    W = 390 if mobile else 1440; S = 0.42 if mobile else 1.0
    out = []; y = 20; i = 0; z = 1
    def put(n, ls, x, yy):
        nonlocal z
        w0, h0 = size(n); sc = ls * S / max(w0, h0); w, ih = round(w0 * sc), round(h0 * sc)
        kd = pick_kind(n, r, allow_torn=True); fs = 0.55 if mobile else 1.0
        px, pt, pb = [round(v * fs) for v in FR[kd]]; fw, fh = w + 2 * px, ih + pt + pb
        cx = min(max(x, fw / 2 - 6), W - fw / 2 + 6)
        it = frame_item(n, kd, cx - fw / 2, yy - fh / 2, w, ih, r, '#3a1414', ['FLASHES', 'KÖLN'], r.randint(2, 35), rot=0 if kd == 'negative' else r.uniform(-8, 8), z=z, fs=fs)
        z += 1; out.append(it)
    while i < len(names):
        band = r.uniform(460, 620) * S
        parts = [(30 * S, W - 30 * S)]
        if not mobile and r.random() < 0.55:
            sp = r.uniform(560, 880); parts = [(30, sp), (sp, 1410)]
        for x0, x1 in parts:
            Wd = x1 - x0; cx = (x0 + x1) / 2; yc = y + band / 2
            g = r.choice(['heap', 'diag', 'row', 'arc', 'ring', 'single']) if Wd > 900 * S else r.choice(['heap', 'heap', 'diag', 'single', 'ring'])
            n = {'heap': r.randint(3, 6), 'diag': r.randint(3, 6), 'row': r.randint(4, 6), 'arc': r.randint(5, 6), 'ring': r.randint(5, 7), 'single': 2 if Wd > 900 * S else 1}[g]
            if mobile: n = min(n, 4)
            ms = names[i:i + n]; i += len(ms)
            for j, m in enumerate(ms):
                t = (j + .5) / len(ms)
                if g == 'heap': put(m, r.uniform(300, 420), cx + r.gauss(0, Wd * 0.27), yc + r.gauss(0, band * 0.2))
                elif g == 'diag': put(m, r.uniform(280, 360), x0 + t * Wd + r.uniform(-20, 20) * S, yc + (t - .5) * band * 0.55)
                elif g == 'row': put(m, r.uniform(280, 350), x0 + t * Wd, yc + r.uniform(-25, 25) * S)
                elif g == 'arc': put(m, r.uniform(270, 340), x0 + t * Wd, yc + (0.5 - math.sin(t * math.pi)) * band * 0.42)
                elif g == 'ring':
                    a = r.uniform(0, .4) + j * 2 * math.pi / len(ms); Rr = min(Wd * 0.34, band * 0.36); put(m, r.uniform(240, 300), cx + Rr * 1.15 * math.cos(a), yc + Rr * math.sin(a))
                else: put(m, r.uniform(360, 460), (x0 + t * Wd) if len(ms) > 1 else cx + r.uniform(-Wd * .25, Wd * .25), yc + r.uniform(-40, 40) * S)
        y += band * r.uniform(0.7, 0.82)
    top = min(o['lt'] for o in out)
    for o in out: o['lt'] -= top - 20
    H = max(o['lt'] + o['fh'] for o in out) + 80
    return {'h': round(H), 'imgs': out}

def build_flashes():
    json.dump({'d': flashes(False), 'm': flashes(True)}, open(os.path.join(OUT, 'flashes.json'), 'w'))
    print('flashes ok')

if __name__ == '__main__':
    build_arbeiten()

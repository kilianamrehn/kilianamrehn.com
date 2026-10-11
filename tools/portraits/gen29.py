import json, random, colorsys, math, os, sys, re
B = os.path.dirname(os.path.abspath(__file__))
CAN = os.path.join(B, '..', 'canvas')
LOCAL = '--local' in sys.argv
items = json.load(open(os.path.join(CAN, 'art', 'items.json')))
blobs = open(os.path.join(B, '..', 'r18', 'blobs.txt')).read().split()
TEXB = json.load(open(os.path.join(B, 'texblobs.json')))
TEXB.update(json.load(open(os.path.join(B, 'tex2blobs.json'))) if os.path.exists(os.path.join(B, 'tex2blobs.json')) else {})
meta2 = json.load(open(os.path.join(B, 'tex2', 'meta.json')))
metaH = json.load(open(os.path.join(B, '..', 'hand3', 'meta.json')))

def T(name):
    if LOCAL:
        if name.startswith('G_'): return f'../hand3/{name[2:]}.png'
        if name.startswith('M_'): return f'marks2/{name[2:]}.png'
        return f'tex2/{name}.png' if name in meta2 else f'tex/{name}.png'
    return '/_blob/' + TEXB['B_' + name[2:] if name.startswith('G_') else name]

for it, b in zip(items, blobs):
    it['src'] = ('../canvas/art/' + it['f']) if LOCAL else '/_blob/' + b
    it['video'] = None

# ---- removals / changes (Kilian, 11.10. 17:06)
REMOVED = {'a013', 'a096', 'a001', 'a050', 'a051', 'a060', 'a079', 'a084', 'a056', 'a024', 'a026', 'a065', 'a017', 'a018', 'a021', 'a023', 'a030', 'a070', 'a022', 'a012', 'a068', 'a088', 'a064', 'a038', 'a076', 'a075', 'a054', 'a055', 'a049', 'a052', 'a025', 'a005', 'a097', 'a016'}
items = [x for x in items if x['proj'] not in ('Guls', 'Feye', 'DJ O-Sun', 'Daniels') and x['f'][:4] not in REMOVED]
NOCAT = {'a031', 'a032', 'a033', 'a034', 'a035', 'a056', 'a060', 'a061'}
for x in items:
    if x['proj'] == 'HIMOYA':
        x['video'] = '/_blob/d0cc89de0a0c8f8edab9fd4810b942a7'
        x['src'] = ('../r20/vid/HIMOYA_bunt_poster.jpg' if LOCAL else '/_blob/41ec99fb5cdafcc15c72e5529526c413'); x['w'], x['h'] = 1000, 666
rares_last = max([i for i, x in enumerate(items) if x['proj'] == 'Rares'] or [len(items) - 1])
items.insert(rares_last + 1, {'f': 'rares_v', 'proj': 'Rares', 'year': 2024, 'w': 1000, 'h': 654, 'bw': False, 'sat': 0.4, 'light': 0.4, 'rgb': '#6a8fb0', 'analog': False,
                              'src': ('../r20/vid/Rares_epic_poster.jpg' if LOCAL else '/_blob/49f1e0d7a75bc96e0455c0f821c28b93'), 'video': '/_blob/a42f3060701c1a4867e5a5dd7655ddf9', 'ki': True})

items.append({'f': 'nbk', 'proj': 'Nici und Nati', 'year': 2025, 'w': 667, 'h': 1000, 'bw': True, 'sat': 0.0, 'light': 0.3, 'rgb': '#333333', 'analog': False,
              'src': ('../book/nati_DSC06949.jpg' if LOCAL else '/_blob/014c042de2183f2f177bd8cbf7866ee4'), 'video': None})
for x in items:
    if x['f'] == 'nbk' or x['f'][:4] in ('a061', 'a063'): x['proj'] = 'Nati'
    if x['proj'] == 'Simon Below': x['proj'] = 'Simon und Quartett'

def artist(p):
    if p.startswith('Nicole Da Silva'): return 'Nicole Da Silva'
    if p.startswith('Scholl iconic'): return 'Scholl iconic'
    if p.startswith('Analog'): return 'Alua und Linde'
    if p.startswith('Nicole ·'): return 'Nicole'
    return p

NAMED = {'Bianca Berding': 'bianca', 'David Vormweg': 'david', 'Slavko Popadic': 'slavko', 'Lea Mende': 'lea', 'Pelin': 'zahnatzin', 'Mario Holi': 'mario',
         'Morley': 'morley', 'Paulus Goerden': 'paulus', 'Parzhuber Trio': 'parzhuber', 'Simon und Quartett': 'simon', 'Nicole Da Silva': 'nicoleds',
         'Nicole': 'nicole', 'Salomé': 'salome', 'Pia Stutzenstein': 'pia', 'Paula, DJ': 'paula'}
YEARS = {2021: 'y21', 2022: 'y22', 2023: 'y23', 2024: 'y24', 2025: 'y25', 2026: 'y26'}
CAPTION_ONLY = set()
SHEETS = [
    [['082'], ['083', '085']],                                          # Bianca
    [['019', '020'], ['037'], ['039', '040']],                          # Slavko
    [['043', '044'], ['045'], ['046', '047', '048']],                   # Lea
    [['069', '071'], ['072', '027', '028']],                            # Zahnatzin, Mario
    [['042', '002', 'nbk'], ['010', '029'], ['009', '003'], ['006', '004'], ['063', '061']],  # Einzel-Porträts
    [['007', '008'], ['053', '011'], ['073', '074'], ['077', '078']],   # Bands
    [['031', '032'], ['033', '034']],                                   # Paulus
    [['062', '066']],                                                   # Nicole Da Silva
    [['092', '093'], ['094', '095']],                                   # Nicole
    [['059'], ['058', '035', '036'], ['014', '015']],                   # Schauspiel: Salome, Pia, David
    [['086', '087', '089'], ['090', '091']],                            # Paula
]
TOP = {0, 1, 2, 3}
KIND = {
 '083': 'polaroid', '085': 'negative', '015': 'border',
 '019': 'negative', '040': 'border', '043': 'negative', '045': 'polaroid', '048': 'border',
 '071': 'polaroid', '028': 'negative',
 '042': 'border', '002': 'negative', '010': 'polaroid', '003': 'negative', '006': 'negative', '004': 'border', '069': 'negative',
 '007': 'polaroid', '053': 'negative', '074': 'border', '078': 'negative',
 '032': 'polaroid', '033': 'border',
 '063': 'negative', '066': 'polaroid',
 '093': 'negative', '094': 'border',
 '058': 'negative', '036': 'polaroid',
 '087': 'negative', '090': 'polaroid', '091': 'border',
}
EDGE = {
 '085': ('MODERATIONSPORTRÄTS', 'PORTRÄTS FÜR WEBSITES'),
 '069': ('DJ-PORTRÄTS', 'PLATTENCOVER'),
 '006': ('GERICHTETES LICHT', 'PORTRÄTFOTOGRAFIE KÖLN'),
 '019': ('PORTRÄTFOTOGRAFIE KÖLN', 'GERICHTETES LICHT'),
 '043': ('FARBIGES LICHT', 'KEINE POSE'),
 '028': ('MUSIKPORTRÄTS', 'PRESSEFOTOS'),
 '002': ('PORTRÄTFOTOGRAFIE KÖLN', 'KEINE POSE'),
 '003': ('SCHAUSPIELPORTRÄTS', 'PORTRÄTFOTOGRAFIE KÖLN'),
 '053': ('PRESSEFOTOS FÜR BANDS', 'MUSIKPORTRÄTS'),
 '078': ('PRESSEFOTOS FÜR BANDS', 'ARTISTPORTRÄTS KÖLN'),
 '063': ('PORTRÄTFOTOGRAFIE KÖLN', 'KEINE POSE'),
 '093': ('KÜNSTLERINNENPORTRÄTS', 'GERICHTETES LICHT'),
 '058': ('SCHAUSPIELPORTRÄTS', 'KEINE POSE'),
 '087': ('DJ-PORTRÄTS', 'FARBIGES LICHT'),
}
POLAROID_YEAR = {'083', '045', '032', '090', '036'}
MAXW = {'a072': (600, 330), 'a027': (620, 340)}
SHOWN = {'Pelin': 'Zahnatzin', 'Mario Holi': 'Mario Nyeky', 'Paula, DJ': 'Paula'}
BANDS = {'Schön im Wald', 'Simon und Quartett', 'HIMOYA', 'Morley', 'Simon Below', 'Parzhuber Trio', 'Nici und Nati'}
MUSIC = BANDS | {'Nicole Da Silva', 'Mos Def', 'Pelin', 'Mario Holi', 'Paula, DJ'}
COVERS = {'Pelin', 'Mario Holi', 'Nicole Da Silva', 'Morley'}
ACTING = {'Flo Wünsche', 'David Vormweg', 'Pia Stutzenstein', 'Salomé'}
DJ = {'Pelin', 'Paula, DJ'}
MODERATION = {'Bianca Berding'}
COVER_IDS = {'072', '027', '062', '073'}
ART = {'Muli', 'Nicole'}
NEUTRAL = ['PORTRÄTFOTOGRAFIE KÖLN', 'LICHT, DAS SUCHT', 'KEINE POSE', 'GERICHTETES LICHT', 'PORTRÄTS KÖLN']

def edge_words(a, it):
    w = list(NEUTRAL)
    if not it['bw']: w.append('FARBIGES LICHT')
    if a in MUSIC: w += ['MUSIKPORTRÄTS', 'ARTISTPORTRÄTS KÖLN', 'PRESSEFOTOS'] * 2
    if a in BANDS: w += ['PRESSEFOTOS FÜR BANDS'] * 2
    if a in COVERS: w += ['EP- UND ALBUMCOVER'] * 2
    if a in ACTING: w += ['SCHAUSPIELPORTRÄTS'] * 3
    if a in ART: w += ['KÜNSTLERINNENPORTRÄTS'] * 3
    return w

groups, order = {}, []
for it in items:
    k = artist(it['proj'])
    if k not in groups: groups[k] = []; order.append(k)
    groups[k].append(it)

def hsl(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h % 1, l, s)
    return '#%02x%02x%02x' % tuple(round(v * 255) for v in (r, g, b))
def rgb_h(c):
    r, g, b = [int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    return colorsys.rgb_to_hls(r, g, b)[0]

PAPERS = [(15, '#3b1515'), (35, '#4a2514'), (55, '#4a3a17'), (90, '#30351a'), (160, '#17321f'), (190, '#123333'), (215, '#14293b'), (260, '#181d3a'), (340, '#301930'), (361, '#3b1515')]
CHAR = '#1f1d1b'
def paper_for(h):
    d = (h * 360) % 360
    for lim, c in PAPERS:
        if d < lim: return c
PAPER_HUE = {c: None for _, c in PAPERS}

# ---- assign each artist group to a paper (colour fit: same or complementary), balance, then merge per paper
def build_sheets(seed):
    rnd = random.Random(seed)
    used = {}
    sheets = {}
    keys = order[:]
    rnd.shuffle(keys)
    CANDS = {}
    BWP = [CHAR, '#181d3a', '#3b1515', '#17321f', '#301930']
    for k in keys:
        g = groups[k]
        bwr = sum(1 for x in g if x['bw'] or x['sat'] < 0.2) / len(g)
        hs = [rgb_h(x['rgb']) for x in g if not x['bw'] and x['sat'] > 0.25]
        if bwr >= 0.6 or not hs:
            cls = 'bw'; cands = BWP[:]
        else:
            cls = 'col'
            cands = list(dict.fromkeys([paper_for(h) for h in hs] + [paper_for(h + 0.5) for h in hs]))
        rnd.shuffle(cands)
        CANDS[k] = (cls, set(cands))
        c = min(cands, key=lambda c: used.get((c, cls), 0) + rnd.random() * 0.5)
        used[(c, cls)] = used.get((c, cls), 0) + len(g)
        sheets.setdefault((c, cls), []).append(k)
    out = []
    for (c, cls), ks in sheets.items():
        chunk, n = [], 0
        for k in ks:
            if n + len(groups[k]) > 14 and chunk:
                out.append((c, chunk)); chunk, n = [], 0
            chunk.append(k); n += len(groups[k])
        if chunk: out.append((c, chunk))
    # merge tiny sheets (<5 images) into another sheet whose paper also fits all of its groups
    changed = True
    while changed:
        changed = False
        out.sort(key=lambda s: sum(len(groups[k]) for k in s[1]))
        for a in range(len(out)):
            ca, ka = out[a]
            if sum(len(groups[k]) for k in ka) >= 5: continue
            for b in range(len(out)):
                if b == a: continue
                cb, kb = out[b]
                if sum(len(groups[k]) for k in kb) + sum(len(groups[k]) for k in ka) > 16: continue
                if all(cb in CANDS[k][1] and CANDS[k][0] == CANDS[kb[0]][0] for k in ka):
                    out[b] = (cb, kb + ka); out.pop(a); changed = True; break
            if changed: break
    return out

SHADOW = "box-shadow:0 1px 1px rgba(0,0,0,0.28),0 4px 8px rgba(0,0,0,0.16),0 18px 34px -12px rgba(0,0,0,0.45);"
PENCIL_LIGHT = 'rgba(236,231,222,0.88)'
PENCIL_DARK = 'rgba(40,38,36,0.85)'

def mask(name, color, x, y, w, h, z, extra=''):
    u = T(name)
    return {'lt': round(y), 's': f"position:absolute;left:{x:.0f}px;width:{w:.0f}px;height:{h:.0f}px;background:{color};-webkit-mask-image:url({u});mask-image:url({u});-webkit-mask-size:100% 100%;mask-size:100% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;z-index:{z};pointer-events:none;{extra}", 't': ''}

def torn_clip(rnd, n=34, depth=1.1):
    pts = []
    for side in range(4):
        for i in range(n):
            t = i / n * 100; j = rnd.uniform(0, depth)
            pts.append([(t, j), (100 - j, t), (100 - t, 100 - j), (j, 100 - t)][side])
    return 'polygon(' + ','.join('%.1f%% %.1f%%' % p for p in pts) + ')'

def overlap(a, b, m=0):
    return a[0] < b[0] + b[2] + m and b[0] < a[0] + a[2] + m and a[1] < b[1] + b[3] + m and b[1] < a[1] + a[3] + m

FR = {'polaroid': (18, 18, 74), 'border': (12, 12, 12), 'negative': (16, 40, 40), 'torn': (16, 16, 16), 'plain': (0, 0, 0)}

def layout_sheet(sheet_items, kinds, rnd, mobile, label=(), rowspec=None):
    W = 390 if mobile else 1440
    M = 14 if mobile else 44
    avail = W - 2 * M
    n = len(sheet_items)
    rects, inner = [None] * n, [None] * n
    asp = [it['w'] / it['h'] for it in sheet_items]
    rows, i = [], 0
    if rowspec and not mobile:
        rows, i = [], n
        MINH = 470
        queue = [list(r) for r in rowspec]
        while queue:
            r = queue.pop(0)
            if len(r) > 1:
                kf0 = {ii: (1.28 if asp[ii] < 1 and any(asp[jj] >= 1 for jj in r) else 1.0) for ii in r}
                hh0 = (avail * 0.92 - 36 * (len(r) - 1)) / sum(asp[ii] * kf0[ii] for ii in r)
                capped = all(sheet_items[ii]['f'][:4] in MAXW for ii in r)
                if hh0 < MINH and not capped:
                    k = len(r) // 2 if len(r) > 2 else 1
                    queue[0:0] = [r[:k], r[k:]]
                    continue
            rows.append(r)
    while i < n:
        if mobile:
            if i + 1 < n and asp[i] < 1 and asp[i + 1] < 1 and rnd.random() < 0.55:
                rows.append([i, i + 1]); i += 2
            else:
                rows.append([i]); i += 1
            continue
        cap = rnd.uniform(1.75, 2.6)  # in "aspect units": sum of aspect ratios per row
        r, s = [], 0
        while i < n and (not r or s + asp[i] <= cap):
            r.append(i); s += asp[i]; i += 1
        rows.append(r)
    y = 110 if not mobile else 60
    for r in rows:
        gap = rnd.uniform(14, 22) if mobile else rnd.uniform(26, 48)
        fill = rnd.uniform(0.86, 0.97) if len(r) > 1 else (0.9 if sheet_items[r[0]]['f'][:4] == 'a059' else rnd.uniform(0.62, 0.8))
        if mobile: fill = rnd.uniform(0.9, 1.0) if len(r) > 1 else rnd.uniform(0.8, 0.96)
        pads = sum(2 * FR[kinds[ii]][0] for ii in r)
        kf = {ii: (1.28 if asp[ii] < 1 and len(r) > 1 and any(asp[jj] >= 1 for jj in r) else 1.0) for ii in r}
        h = (avail * fill - gap * (len(r) - 1) - pads) / sum(asp[ii] * kf[ii] for ii in r)
        h = min(h, 560 if mobile else 820)
        sizes = []
        for ii in r:
            hh = h * kf[ii] * (rnd.uniform(0.9, 1.0) if len(r) > 1 else 1)
            mx = MAXW.get(sheet_items[ii]['f'][:4])
            if mx and hh * asp[ii] > mx[1 if mobile else 0]:
                hh = mx[1 if mobile else 0] / asp[ii]
            sizes.append((hh * asp[ii], hh))
        tot = sum(w + 2 * FR[kinds[ii]][0] for (w, _), ii in zip(sizes, r)) + gap * (len(r) - 1)
        free = max(0, avail - tot)
        ws = [rnd.uniform(0.3, 1.7) for _ in range(len(r) + 1)]
        tw = sum(ws); x = M
        rowh = 0
        for j, ii in enumerate(r):
            w, ih = sizes[j]; px, pt, pb = FR[kinds[ii]]
            x += free * ws[j] / tw
            dy = rnd.uniform(0, 20 if mobile else 60)
            fw, fh = round(w) + 2 * px, round(ih) + pt + pb
            rects[ii] = (round(x), round(y + dy), fw, fh)
            inner[ii] = (round(w), round(ih))
            x += fw + gap
            rowh = max(rowh, dy + fh)
        y += rowh + (rnd.uniform(22, 38) if mobile else rnd.uniform(36, 70))
        if any(ii in label for ii in r): y += 62 if mobile else 92
    H = y + (30 if mobile else 60)
    return rects, inner, H

metaM = json.load(open(os.path.join(B, 'marks2', 'meta.json')))
def build(seed, mobile):
    global MARK_POOL, MARK_IDX
    _r = random.Random(77); MARK_POOL = sorted(metaM); _r.shuffle(MARK_POOL); MARK_IDX = [0]
    rnd = random.Random(seed)
    byid = {(x['f'][1:4] if x['f'][0] == 'a' and x['f'][1:4].isdigit() else x['f']): x for x in items}
    used_p = {}
    sheets = []
    for spec in SHEETS:
        its = [byid[i] for row in spec for i in row]
        bwr = sum(1 for x in its if x['bw'] or x['sat'] < 0.2) / len(its)
        hs = [rgb_h(x['rgb']) for x in its if not x['bw'] and x['sat'] > 0.25]
        score = {}
        for _, c in PAPERS[:-1]: score[c] = 0
        score[CHAR] = 0
        for h in hs:
            score[paper_for(h)] += 1; score[paper_for(h + 0.5)] += 0.8
        if bwr >= 0.6:
            for c in (CHAR, '#181d3a', '#3b1515', '#17321f', '#301930'): score[c] += 2.5
        for c in score: score[c] -= 1.6 * used_p.get(c, 0)
        best = max(score, key=lambda c: score[c] + random.Random(len(sheets)).random() * 0.3)
        used_p[best] = used_p.get(best, 0) + 1
        sheets.append((best, its, spec))
    out = []
    TS = 0.36 if mobile else 0.5  # text scale
    motifs = ['ring', 'stroke', 'bar', 'ring', 'stroke']
    for si, (paper, sheet_items, spec) in enumerate(sheets):
        rnd = random.Random(seed * 100 + si)
        n = len(sheet_items)
        hs = [rgb_h(x['rgb']) for x in sheet_items if not x['bw'] and x['sat'] > 0.25]
        # paint: colour taken from the photos on this sheet
        if hs:
            h0 = rnd.choice(hs)
            paint_cols = [hsl(h0, 0.7, 0.55), hsl(h0 + 0.5, 0.62, 0.52)]
        else:
            paint_cols = ['#c8352c', '#d9a24f']
        kinds = [KIND.get(it['f'][1:4], 'plain') for it in sheet_items]
        for k, it in enumerate(sheet_items):
            if it['analog']: kinds[k] = 'torn'
        lab_idx, seen_ = [], set()
        for ii, it in enumerate(sheet_items):
            k0 = NAMED.get(it['proj']) or NAMED.get(artist(it['proj']))
            if k0 and k0 not in seen_: seen_.add(k0); lab_idx.append(ii)
        pos = 0; rowspec = []
        for row in spec: rowspec.append(list(range(pos, pos + len(row)))); pos += len(row)
        rects, inner, H = layout_sheet(sheet_items, kinds, rnd, mobile, set(lab_idx), rowspec)
        imgs, back, front, texts = [], [], [], []
        for ii, it in enumerate(sheet_items):
            a = artist(it['proj'])
            x, y, fw, fh = rects[ii]; w, ih = inner[ii]
            kind = kinds[ii]; px, pt, pb = FR[kind]
            rot = 0.0
            if kind in ('polaroid', 'torn'): rot = rnd.uniform(-2.4, 2.4)
            elif kind == 'border': rot = rnd.uniform(-1.2, 1.2)
            elif kind == 'plain' and rnd.random() < 0.35: rot = rnd.uniform(-0.9, 0.9)
            nm = SHOWN.get(it['proj'], a)
            cat = 'Albumcover' if it['f'][1:4] in COVER_IDS else 'DJ-Porträt' if a in DJ or it['proj'] in DJ else 'Moderationsporträt' if a in MODERATION else 'Pressefoto für Bands' if a in BANDS else 'Musikporträt' if a in MUSIC else 'Schauspielporträt' if a in ACTING else 'Künstlerinnenporträt' if a in ART else 'Porträt'
            alt = (f"{nm}, {cat}, fotografiert von Kilian Amrehn, Köln {it['year']}" if (a in NAMED or it['proj'] in NAMED) else f"{cat}, Porträtfotografie Kilian Amrehn, Köln {it['year']}")
            wrap = f"position:absolute;left:{x}px;width:{fw}px;height:{fh}px;transform:rotate({rot:.2f}deg);z-index:{10 + ii};cursor:zoom-in;"
            isty = f"display:block;width:{w}px;height:{ih}px;position:absolute;left:{px}px;top:{pt}px;"
            s1 = s2 = 'display:none'; t1 = t2 = ''
            if kind == 'plain':
                wrap += SHADOW
            elif kind == 'border':
                wrap += 'background:#f3f0e9;' + SHADOW
            elif kind == 'polaroid':
                wrap += 'background:#f1eee6;background-image:linear-gradient(180deg,rgba(255,255,255,0.35),rgba(0,0,0,0.03));' + SHADOW
                if it['f'][1:4] in POLAROID_YEAR and YEARS.get(it['year']):
                    q = 'G_' + YEARS[it['year']]; mw, mh = metaH[YEARS[it['year']]]; sc = 0.2 if not mobile else 0.13
                    s2 = (f"position:absolute;left:{fw - mw * sc - 22:.0f}px;top:{pt + ih + (pb - mh * sc) / 2:.0f}px;width:{mw * sc:.0f}px;height:{mh * sc:.0f}px;background:{hsl(rnd.choice(hs) if hs else 0.02, 0.62, 0.42)};"
                          f"-webkit-mask-image:url({T(q)});mask-image:url({T(q)});-webkit-mask-size:100% 100%;mask-size:100% 100%;transform:rotate({rnd.uniform(-4, 3):.0f}deg)")
            elif kind == 'negative':
                wrap = re.sub(r'rotate\([^)]*\)', 'rotate(0deg)', wrap)
                fnum = rnd.randint(2, 35)
                words = edge_words(a, it)
                wrap += 'background:#121110;' + SHADOW
                tx = f"font:500 {9 if mobile else 10}px/1 'Geist Mono',monospace;letter-spacing:0.2em;color:#d9823a;display:flex;padding:0 14px;box-sizing:border-box;white-space:nowrap;overflow:hidden;position:absolute;left:0;right:0;height:14px;align-items:center;"
                e1, e2 = EDGE.get(it['f'][1:4], ('PORTRÄTFOTOGRAFIE KÖLN', 'KEINE POSE'))
                s1 = tx + "top:22px"; t1 = f"{fnum}A  ▸  {e1}"
                s2 = tx + "bottom:22px"; t2 = f"{fnum + 1}  ◂  {e2}"
                sp = T('sprocket')
                for yy in (5, fh - 19):
                    front.append({'lt': y + yy, 's': f"position:absolute;left:{x + 4}px;width:{fw - 8}px;height:14px;background:{paper};-webkit-mask-image:url({sp});mask-image:url({sp});-webkit-mask-size:28px 14px;mask-size:28px 14px;-webkit-mask-repeat:repeat-x;mask-repeat:repeat-x;z-index:{10 + ii};pointer-events:none", 't': ''})
            elif kind == 'torn':
                wrap += f"background:#f3efe6;clip-path:{torn_clip(rnd)};filter:drop-shadow(0 8px 14px rgba(0,0,0,0.35));"
            if it.get('ki'):
                s2 = f"position:absolute;right:8px;bottom:8px;font:500 9px/1 'Geist Mono',monospace;letter-spacing:0.18em;color:rgba(255,255,255,0.75);background:rgba(0,0,0,0.35);padding:4px 6px"
                t2 = 'KI-VIDEO'
            imgs.append({'fid': it['f'], 'year': it['year'], 'nm': nm, 'cat': cat, 'named': bool(a in NAMED or it['proj'] in NAMED), 'artist': a, 'e1': (EDGE.get(it['f'][1:4], ('PORTRÄTFOTOGRAFIE KÖLN', 'KEINE POSE')) if kind == 'negative' else None), 'fnum': (fnum if kind == 'negative' else None), 'lt': y, 'src': it['src'], 'vsrc': it.get('video') or '', 'alt': alt, 'wrap': wrap, 'is_': isty, 's1': s1, 't1': t1, 's2': s2, 't2': t2,
                         'cap': nm if (a in NAMED or it['proj'] in NAMED or a in CAPTION_ONLY) else ''})
        # ---- names (only the chosen ones), next to the first photo of that person
        seen = set()
        for ii, it in enumerate(sheet_items):
            key0 = NAMED.get(it['proj']) or NAMED.get(artist(it['proj']))
            if not key0 or key0 in seen: continue
            seen.add(key0)
            key = 'G_' + key0
            mw, mh = metaH[key0]; sc = (0.24 if mobile else 0.36) * rnd.uniform(0.94, 1.06)
            tw, th = mw * sc, mh * sc
            x, y, fw, fh = rects[ii]
            W = 390 if mobile else 1440
            cands = [(x + fw + 18, y + rnd.uniform(0, fh * 0.6)), (x - tw - 18, y + rnd.uniform(0, fh * 0.6)),
                     (x + rnd.uniform(0, max(1, fw - tw)), y + fh + 10), (x + rnd.uniform(0, max(1, fw - tw)), y - th - 6)]
            if mobile: cands = cands[2:] + cands[:2]
            else:
                rnd.shuffle(cands)
                cands.append((x + rnd.uniform(0, max(1, fw - tw)), y + fh + 10))
                cands.append((max(10, x + fw - tw), y + fh + 10))
            ybot = max(r[1] + r[3] for r in rects if r[1] < y + fh and r[1] + r[3] > y) + 10
            cands += [(xx, ybot) for xx in range(20, W - 20, 30)]
            for cx, cy in cands:
                box = (cx, cy, tw + 6, th)
                if cx < 8 or cx + box[2] > W - 8 or cy < 10 or cy + box[3] > H - 6: continue
                if any(overlap(box, r, 8) for r in rects) or any(overlap(box, t, 8) for t in texts): continue
                texts.append(box)
                rd = rnd.uniform(-3, 2)
                hn = rnd.choice(hs) if hs else rnd.choice([0.02, 0.1])
                ph_ = colorsys.rgb_to_hls(*[int(paper[k:k+2], 16) / 255 for k in (1, 3, 5)])[0]; hd_ = lambda a: min(abs(a - ph_) % 1, 1 - abs(a - ph_) % 1); hn = hn if hd_(hn) > 0.18 and rnd.random() < 0.5 else (hn + 0.5 if hd_(hn + 0.5) > hd_(hn) else hn); NCOL = hsl(hn, 0.7, 0.68)
                front.append(mask(key, NCOL, cx, cy, tw, th, 30, f'transform:rotate({rd:.1f}deg);'))
                yk = YEARS.get(it['year'])
                if yk and rnd.random() < 0.35:
                    yw, yh = metaH[yk]; ys_ = sc * 0.85
                    yx = cx + tw + 14 * (0.6 if mobile else 1)
                    if yx + yw * ys_ > W - 8: yx = cx + 6
                    yy_ = cy + (th - yh * ys_) / 2 if yx > cx + tw else cy + th + 4
                    front.append(mask('G_' + yk, NCOL, yx, yy_, yw * ys_, yh * ys_, 30, f'transform:rotate({rd + rnd.uniform(-3, 3):.1f}deg);'))
                break
        # ---- painted marks: every mark unique on the page, 2 to 4 per sheet, behind photos
        cnt = {0: 3, 1: 3, 2: 4}[si % 3] if n > 3 else 2
        cnt = min(cnt, len(MARK_POOL) - MARK_IDX[0])
        hs_all = [rgb_h(x['rgb']) for x in sheet_items if not x['bw'] and x['sat'] > 0.25] or [0.02, 0.1]
        used_t = set()
        for mi in range(cnt):
            key = MARK_POOL[MARK_IDX[0]]; MARK_IDX[0] += 1
            mw, mh, kind = metaM[key]
            h0 = rnd.choice(hs_all)
            paint = hsl(h0 + (0.5 if rnd.random() < 0.45 else rnd.uniform(-0.04, 0.04)), rnd.uniform(0.55, 0.78), rnd.uniform(0.46, 0.6))
            cands = [i for i in range(n) if i not in used_t] or list(range(n))
            t_ = rnd.choice(cands); used_t.add(t_)
            x, y, fw, fh = rects[t_]
            SC = 0.42 if mobile else 1.0
            op = rnd.uniform(0.82, 0.97)
            if kind in ('ring', 'arc'):
                d = (rnd.uniform(0.75, 1.15) * min(fw, fh) + 60 * SC) * (1.15 if kind == 'arc' else 1)
                cx = x + rnd.choice([0, fw, fw * rnd.uniform(0.2, 0.8)]) + rnd.uniform(-0.2, 0.2) * d
                cy = y + rnd.choice([0, fh, fh * rnd.uniform(0.3, 0.9)]) + rnd.uniform(-0.15, 0.15) * d
                back.append(mask('M_' + key, paint, cx - d / 2, cy - d / 2, d, d, 4, f'opacity:{op:.2f};transform:rotate({rnd.uniform(0, 360):.0f}deg){" scaleX(-1)" if rnd.random() < 0.5 else ""};'))
            elif kind == 'swipe':
                sw = min((390 if mobile else 1440) * 1.0, fw * rnd.uniform(1.6, 2.4)); sh = sw * mh / mw * rnd.uniform(0.75, 1.0)
                sx = x + fw / 2 - sw / 2 + rnd.uniform(-0.25, 0.25) * fw; sy = y + fh * rnd.uniform(0.2, 0.85) - sh / 2
                back.append(mask('M_' + key, paint, sx, sy, sw, sh, 4, f'opacity:{op:.2f};transform:rotate({rnd.uniform(-9, 9):.1f}deg){" scaleX(-1)" if rnd.random() < 0.5 else ""};'))
            else:  # thin line
                lw = rnd.uniform(0.6, 1.1) * (360 if mobile else 1000); lh = lw * mh / mw
                lx = x + rnd.uniform(-0.4, 0.6) * fw; ly = y + rnd.choice([fh + rnd.uniform(-30, -6) * SC, rnd.uniform(0.1, 0.9) * fh])
                back.append(mask('M_' + key, paint, lx, ly, lw, lh, 4, f'opacity:{op:.2f};transform:rotate({rnd.uniform(-4, 4):.1f}deg){" scaleX(-1)" if rnd.random() < 0.5 else ""};'))
        out.append({'top': si in TOP, 'h': round(H), 'bg': paper, 'imgs': imgs, 'back': back, 'front': front})
    return out

if __name__ == '__main__':
    D = build(5, False); Mo = build(5, True)
    tpl = open(os.path.join(B, 'tpl27.html')).read()
    html = (tpl.replace('__PAPER__', T('paper')).replace('__DATA_D__', json.dumps(D, ensure_ascii=False).replace('</', '<\\/'))
            .replace('__DATA_M__', json.dumps(Mo, ensure_ascii=False).replace('</', '<\\/')))
    if LOCAL:
        html = html.replace('/_blob/804323ba3e5c03e67b270f9094afd2b5', '../canvas/kilian_logo_weiss.png')
        open(os.path.join(B, 'R29_local.html'), 'w').write(html)
    else:
        for nm in ('R29_Artists_Tisch.dc.html', 'R29_Artists_Tisch_Handy.dc.html'):
            open(os.path.join(CAN, 'project', nm), 'w').write(html)
    print(len(D), sum(d['h'] for d in D), sum(d['h'] for d in Mo), len(html) // 1024, 'KB', [len(d['imgs']) for d in D])

"""Unique hand-made-looking marks: every mark is generated once, never reused.
Principles from research: pressure + speed variation, ink pooling at the start,
dry-brush break-up at the end, imperfect closure / overshoot, asymmetry, single events."""
import numpy as np, math, random, os, json
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter
from scipy.interpolate import CubicSpline
B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(B, 'marks2'); os.makedirs(OUT, exist_ok=True)

def smooth(pts, n=300):
    P = np.array(pts, float); t0 = np.linspace(0, 1, len(P)); t = np.linspace(0, 1, n)
    return np.stack([CubicSpline(t0, P[:, 0])(t), CubicSpline(t0, P[:, 1])(t)], 1)

def brush(P, width, size, seed, dry=0.5, ss=2, pool=True, splat=True):
    rnd = np.random.default_rng(seed)
    W, H = size
    P = np.asarray(P) * ss
    seg = np.sqrt(((P[1:] - P[:-1]) ** 2).sum(1)); s = np.concatenate([[0], np.cumsum(seg)])
    tt = np.linspace(0, s[-1], max(50, int(s[-1] / 1.4)))
    px = np.interp(tt, s, P[:, 0]); py = np.interp(tt, s, P[:, 1])
    dx = np.gradient(px); dy = np.gradient(py); ln = np.hypot(dx, dy) + 1e-9
    nx, ny = -dy / ln, dx / ln
    t = tt / tt[-1]
    # pressure: a random smooth curve, not a sine
    kn = rnd.uniform(0.55, 1.0, size=rnd.integers(4, 8)); kn[0] = rnd.uniform(0.75, 1.0)
    pres = np.interp(t, np.linspace(0, 1, len(kn)), kn)
    pres = gaussian_filter(pres, len(t) / 30)
    start = np.minimum(1, t / rnd.uniform(0.02, 0.06)) ** 0.5
    endtaper = 1 - rnd.uniform(0.15, 0.45) * np.clip((t - rnd.uniform(0.7, 0.85)) / 0.2, 0, 1)
    prof = pres * start * endtaper
    load = np.clip(1.05 - t * rnd.uniform(0.2, 0.5), 0.5, 1)  # paint runs out
    K = int(rnd.integers(90, 140))
    img = Image.new('L', (W * ss, H * ss), 0); dr = ImageDraw.Draw(img)
    for j in range(K):
        o = rnd.uniform(-0.5, 0.5); edge = abs(o) * 2
        ts = rnd.uniform(0, 0.025) * (1 + 5 * edge ** 2)
        te = 1 - rnd.uniform(0, 0.25) * edge ** 1.4 - dry * rnd.uniform(0, 0.15)
        ink = rnd.uniform(0.55, 1.0)
        fr = rnd.uniform(20, 100); ph = rnd.uniform(0, 100)
        nz = np.sin(t * fr + ph) * 0.55 + np.sin(t * fr * 2.7 + ph * 0.6) * 0.45
        dryness = dry * 1.6 * np.clip(t - rnd.uniform(0.25, 0.5), 0, 1) ** 1.5 + 0.25 * dry * edge ** 3
        alpha = ink * load
        alpha = np.where((nz < -1 + 2.2 * dryness) | (t < ts) | (t > te), 0, alpha)
        wob = 0.03 * np.sin(t * rnd.uniform(1.5, 7) + rnd.uniform(0, 6))
        ox = px + nx * (o + wob) * width * ss * prof; oy = py + ny * (o + wob) * width * ss * prof
        bw = max(1, int(rnd.uniform(1.0, 3.6) * ss))
        for i in range(0, len(t) - 2, 2):
            a = alpha[i]
            if a > 0.02: dr.line([(ox[i], oy[i]), (ox[i + 2], oy[i + 2])], fill=int(255 * a), width=bw)
    # stray hairs: a couple of bristles that wander off near the end
    for _ in range(int(rnd.integers(0, 3))):
        o = rnd.choice([-0.55, 0.55]) * rnd.uniform(0.9, 1.2); t0 = rnd.uniform(0.5, 0.85)
        idx = np.where(t > t0)[0]
        drift = np.cumsum(rnd.normal(0, 0.012, len(idx)))
        xs = px[idx] + nx[idx] * (o + drift) * width * ss * prof[idx]; ys = py[idx] + ny[idx] * (o + drift) * width * ss * prof[idx]
        for i in range(0, len(idx) - 2, 2):
            dr.line([(xs[i], ys[i]), (xs[i + 2], ys[i + 2])], fill=int(255 * rnd.uniform(0.4, 0.8) * (1 - i / len(idx))), width=max(1, ss))
    a = np.asarray(img, float) / 255
    a = np.clip(gaussian_filter(a, 0.9 * ss) * 0.85 + a * 0.45, 0, 1)
    if pool:  # ink pooling where the brush lands
        yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
        r = width * ss * prof[3] * 0.55
        blob = np.exp(-(((xx - px[3]) ** 2 + (yy - py[3]) ** 2) / (2 * (r * 0.8) ** 2)))
        a = np.clip(a + blob * 0.35 * (a > 0.05), 0, 1)
    tex = gaussian_filter(rnd.normal(size=a.shape), 1.1 * ss); tex = (tex - tex.min()) / (np.ptp(tex) + 1e-9)
    a = a * (0.78 + 0.22 * tex)
    # occasional splatter dots
    if splat and rnd.random() < 0.35:
        for _ in range(int(rnd.integers(2, 7))):
            i = int(rnd.integers(0, len(t))); d = rnd.uniform(0.7, 1.6) * width * ss
            cx, cy = px[i] + rnd.normal(0, d), py[i] + rnd.normal(0, d); rr = rnd.uniform(1, 4) * ss
            yy, xx = np.ogrid[0:a.shape[0], 0:a.shape[1]]
            a = np.maximum(a, ((xx - cx) ** 2 + (yy - cy) ** 2 < rr * rr) * rnd.uniform(0.6, 0.95))
    out = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)
    return out

def ring(seed):
    rr = random.Random(seed)
    S = 760; c = S / 2; r = S * rr.uniform(0.3, 0.37)
    ex, ey = rr.uniform(0.86, 1.08), rr.uniform(0.86, 1.08)
    a0 = rr.uniform(0, 6.28)
    span = rr.choice([rr.uniform(1.65, 1.95), rr.uniform(2.05, 2.25)]) * math.pi  # open gap or overshoot
    n = rr.randint(9, 14)
    pts = []
    for i in range(n):
        a = a0 + span * i / (n - 1)
        rad = r * (1 + rr.uniform(-0.035, 0.035)) * (1 - rr.uniform(0, 0.06) * i / n)
        pts.append((c + rad * math.cos(a) * ex, c + rad * math.sin(a) * ey))
    w = S * rr.uniform(0.045, 0.1)
    return brush(smooth(pts, 500), w, (S, S), seed, dry=rr.uniform(0.3, 0.8))

def swipe(seed, thin=False):
    rr = random.Random(seed)
    W = 1500; H = 300 if not thin else 110
    n = rr.randint(3, 5)
    ys = [H / 2 + rr.uniform(-H * 0.18, H * 0.18) for _ in range(n)]
    end = W - rr.uniform(60, 200)
    xs = [70 + (end - 70) * (i / (n - 1)) + (rr.uniform(-60, 60) if 0 < i < n - 1 else 0) for i in range(n)]
    w = rr.uniform(120, 200) if not thin else rr.uniform(18, 34)
    return brush(smooth(list(zip(xs, ys)), 400), w, (W, H), seed, dry=rr.uniform(0.35, 0.85), pool=not thin)

def arc(seed):
    rr = random.Random(seed)
    S = 900; c = S / 2; r = S * 0.38
    a0 = rr.uniform(0, 6.28); span = rr.uniform(0.6, 1.1) * math.pi
    pts = [(c + r * math.cos(a0 + span * i / 7) * rr.uniform(0.97, 1.03), c + r * math.sin(a0 + span * i / 7) * rr.uniform(0.97, 1.03)) for i in range(8)]
    return brush(smooth(pts, 400), S * rr.uniform(0.05, 0.09), (S, S), seed, dry=rr.uniform(0.4, 0.8))

if __name__ == '__main__':
    meta = {}
    plan = [('ring', 12), ('swipe', 10), ('line', 8), ('arc', 6)]
    k = 0
    for kind, cnt in plan:
        for i in range(cnt):
            sd = 1000 + k * 37
            im = ring(sd) if kind == 'ring' else swipe(sd) if kind == 'swipe' else swipe(sd, thin=True) if kind == 'line' else arc(sd)
            name = f'm{k:02d}_{kind}'
            rgba = Image.merge('RGBA', [Image.new('L', im.size, 255)] * 3 + [im])
            rgba.save(os.path.join(OUT, name + '.png'), optimize=True)
            meta[name] = [im.width, im.height, kind]
            k += 1
    json.dump(meta, open(os.path.join(OUT, 'meta.json'), 'w'))
    print(len(meta))

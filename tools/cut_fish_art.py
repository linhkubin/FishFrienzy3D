"""Tách nền và cắt bộ phận từ bộ tranh một loài cá (bước 3 trong docs/quy-trinh-ve-ca.md).

Cách dùng:
    python tools/cut_fish_art.py art/clownfish            # đọc art/clownfish/cut-config.json, ghi vào art/clownfish/cut/
    python tools/cut_fish_art.py art/clownfish --out tmp  # ghi ra thư mục khác (để so thử)

Đầu vào (trong thư mục tranh): side.png, body.png, fins.png, eyes.png (nền phẳng, thường là #FF00FF).
Đầu ra: body_tex.webp, sf_*.webp (vây lẻ cắt từ side − body), fin_*.webp (vây cắt từ fins.png),
        e_*.webp / m_*.webp (mắt, miệng) và meta.json (đường viền thân, vị trí mắt, toạ độ vây...).

cut-config.json (ví dụ cá hề):
{
  "finsCells": [                      // các ô trong fins.png, theo thứ tự đọc (trên → dưới, trái → phải)
    {"name": "tail", "rot": 0}, {"name": "dorsalB", "rot": 90}, ...   // rot: xoay để GỐC vây nằm ở mép phải
  ],
  "eyesCells": ["e_normal", "e_scared", "e_narrow", "e_dizzy", "e_closed", "m_closed", "m_open"],
  "sideFinNames": ["sf_dorsal", "sf_tail", "sf_anal", "sf_pelvic"],   // theo thứ tự đọc của các mảng side − body
  "mouthBox": [0.9, 0.42, 0.72, 0.955],   // vùng miệng vẽ sẵn cần xoá: u >= a và b <= v <= c, hoặc u >= d (toạ độ chuẩn hoá trong khung thân)
  "snoutRef": 0.885                       // cột màu (u) kéo dài ra phía mõm
}
Cần: Python 3 + Pillow + numpy.
"""
import sys, json, argparse
sys.stdout.reconfigure(encoding='utf-8')
from collections import deque
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter


def key_out(path):
    """Tách nền: độ trong suốt theo khoảng cách màu tới màu nền (trung vị ở viền ảnh), rồi khử viền màu nền."""
    im = np.asarray(Image.open(path).convert('RGB')).astype(np.float32)
    edge = np.concatenate([im[:8].reshape(-1, 3), im[-8:].reshape(-1, 3), im[:, :8].reshape(-1, 3), im[:, -8:].reshape(-1, 3)])
    bg = np.median(edge, axis=0)
    d = np.sqrt(((im - bg) ** 2).sum(-1))
    a = np.clip((d - 40) / 70, 0, 1)
    aa = np.maximum(a, 1e-3)[..., None]
    col = np.clip((im - (1 - aa) * bg) / aa, 0, 255)
    return np.dstack([col, a * 255]).astype(np.float32)


def components(mask, minpix=400, step=2):
    """Các mảng liền nhau trong mask: [(x0, y0, x1, y1, số điểm, nhãn)], sắp theo thứ tự đọc."""
    H, W = mask.shape
    lab = np.zeros((H, W), np.int32)
    out, n = [], 0
    for y in range(0, H, step):
        for x in range(0, W, step):
            if mask[y, x] and lab[y, x] == 0:
                n += 1
                q = deque([(y, x)]); lab[y, x] = n
                c, x0, x1, y0, y1 = 0, x, x, y, y
                while q:
                    cy, cx = q.popleft(); c += 1
                    x0, x1, y0, y1 = min(x0, cx), max(x1, cx), min(y0, cy), max(y1, cy)
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = n; q.append((ny, nx))
                if c >= minpix:
                    out.append((x0, y0, x1, y1, c, n))
    rowH = max(1, H // 12)
    out.sort(key=lambda b: (b[1] // rowH, b[0]))
    return out, lab


def diffuse_fill(rgb, known, iters=1500):
    """Lấp vùng chưa biết bằng cách loang dần màu các điểm đã biết xung quanh vào."""
    fill = rgb * known[..., None]
    w = known.astype(np.float32).copy()
    for _ in range(iters):
        s = np.zeros_like(fill); c = np.zeros_like(w)
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            s += np.roll(np.roll(fill * w[..., None], dy, 0), dx, 1)
            c += np.roll(np.roll(w, dy, 0), dx, 1)
        upd = (known == 0) & (c > 0)
        fill[upd] = s[upd] / c[upd][:, None]
        w[upd] = np.minimum(1, c[upd] * .5 + w[upd])
    return np.where(known[..., None] > 0, rgb, fill)


def save(im_arr, path, mode='RGBA', maxside=None, quality=88):
    im = Image.fromarray(np.clip(im_arr, 0, 255).astype(np.uint8), mode)
    if maxside:
        s = min(1, maxside / max(im.size))
        im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
    im.save(path, quality=quality, method=6)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('art', help='thư mục tranh, ví dụ art/clownfish')
    ap.add_argument('--out', help='thư mục ghi (mặc định <art>/cut)')
    args = ap.parse_args()
    art = Path(args.art); out = Path(args.out or art / 'cut'); out.mkdir(parents=True, exist_ok=True)
    cfg = json.load(open(art / 'cut-config.json', encoding='utf-8'))
    meta = {}

    # ---- thân: khung bao, đường viền, vị trí mắt -------------------------------------
    side, body = key_out(art / 'side.png'), key_out(art / 'body.png')
    ba = body[..., 3] > 128
    ys, xs = np.where(ba); X0, Y0, X1, Y1 = xs.min() - 4, ys.min() - 4, xs.max() + 5, ys.max() + 5
    B = body[Y0:Y1, X0:X1]; H, W = B.shape[:2]; A = B[..., 3] / 255
    prof = []
    for x in range(0, W, max(1, W // 64)):
        col = np.where(A[:, x] > .5)[0]
        prof.append([x / W, col.min() / H if len(col) else None, col.max() / H if len(col) else None])
    rgb = B[..., :3]
    yy, xx = np.mgrid[0:H, 0:W]; u, v = xx / W, yy / H
    orange = (rgb[..., 0] > 200) & (rgb[..., 1] > 90) & (rgb[..., 1] < 200) & (rgb[..., 2] < 140)
    eyeCand = (~orange) & (A > .9) & (u > .74) & (u < .95) & (v > .2) & (v < .62)   # vùng đầu, tránh sọc / hoa văn thân
    ey_, ex_ = np.where(eyeCand)
    ex, ey = ex_.mean(), ey_.mean(); er = (np.percentile(ex_, 99) - np.percentile(ex_, 1)) / 2
    meta['body'] = {'size': [W, H], 'profile': prof, 'eye': [float(ex / W), float(ey / H), float(2 * er / W)]}
    meta['bodyBox'] = [int(X0), int(Y0), int(X1), int(Y1)]
    print('thân', W, 'x', H, ' mắt', [round(c, 3) for c in meta['body']['eye']])

    # ---- ảnh da thân: xoá mắt + miệng vẽ sẵn, kéo dài màu ra mõm, loang ra ngoài viền --
    er5 = np.asarray(Image.fromarray((A * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(5))) / 255
    eye = ((xx - ex) ** 2 + (yy - ey) ** 2) < (er * 1.25) ** 2
    ma, mb, mc, md = cfg.get('mouthBox', [.9, .42, .72, .955])
    mouth = ((u > ma) & (v > mb) & (v < mc)) | (u > md)
    pink = (rgb[..., 2] > rgb[..., 1] * .92) & (u > .8)
    known = ((~eye) & (~mouth) & (er5 > .95) & (~pink)).astype(np.float32)
    tex = diffuse_fill(rgb, known)
    pr = [p for p in prof if p[1] is not None]
    pu, pt, pb = (np.array([p[i] for p in pr]) for i in range(3))
    uR = cfg.get('snoutRef', .885); vtR, vbR = np.interp(uR, pu, pt), np.interp(uR, pu, pb); xR = int(uR * W)
    ref = tex[:, xR - 2:xR + 1].mean(1); ext = tex.copy()
    for x in range(xR + 1, W):
        uu = min(x / W, pu[-1]); vt, vb = np.interp(uu, pu, pt), np.interp(uu, pu, pb)
        s = (np.arange(H) / H - vt) / max(vb - vt, 1e-3)
        ext[:, x] = ref[(np.clip(vtR + s * (vbR - vtR), 0, 1 - 1 / H) * H).astype(int)]
    bl = np.clip((np.arange(W) - xR) / 12, 0, 1)[None, :, None]
    tex = tex * (1 - bl) + ext * bl
    save(tex, out / 'body_tex.webp', 'RGB', maxside=1024, quality=90)

    # ---- vây lẻ: side − body (đúng toạ độ trong tranh) ------------------------------
    sa = side[..., 3] > 128
    bad = np.asarray(Image.fromarray((ba * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 128
    comps, lab = components(sa & ~bad, minpix=300)
    meta['sideFins'] = {}
    for name, c in zip(cfg['sideFinNames'], comps):
        x0, y0, x1, y1, _, L = c
        m = np.asarray(Image.fromarray(((lab == L) * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(15))) > 0
        m &= side[..., 3] > 8
        p = 10; bx = [x0 - p, y0 - p, x1 + p, y1 + p]
        crop = side[bx[1]:bx[3] + 1, bx[0]:bx[2] + 1].copy(); crop[..., 3] *= m[bx[1]:bx[3] + 1, bx[0]:bx[2] + 1]
        save(crop, out / f'{name}.webp', maxside=512)
        meta['sideFins'][name] = [int(b) for b in bx]
        print('vây (side − body)', name, meta['sideFins'][name])
    # đổi toạ độ pixel của tranh ngang sang đơn vị thân (dùng trong <ca>.js: PX, PY)
    meta['sideFrame'] = {'scale': 1 / (X1 - X0), 'x0': int(X0), 'yMid': (Y0 + Y1) / 2}

    # ---- vây từ fins.png: xoay để gốc ở mép phải, làm mờ mép gốc --------------------
    fins = key_out(art / 'fins.png')
    fc, _ = components(fins[..., 3] > 128)
    for spec, c in zip(cfg['finsCells'], fc):
        x0, y0, x1, y1 = c[:4]
        im = Image.fromarray(fins[max(0, y0 - 6):y1 + 7, max(0, x0 - 6):x1 + 7].astype(np.uint8), 'RGBA')
        if spec.get('rot'): im = im.rotate(spec['rot'], expand=True)
        s = min(1, 512 / max(im.size)); im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
        f = np.asarray(im).astype(np.float32); h, w = f.shape[:2]
        rows = np.where((f[:, -12:-4, 3] > 128).any(1))[0]
        ramp = np.clip((w - 1 - np.arange(w)) / (.12 * w), 0, 1); ramp = ramp * ramp * (3 - 2 * ramp)
        f[..., 3] *= ramp[None, :]
        save(f, out / f"fin_{spec['name']}.webp")
        meta[spec['name']] = {'size': [w, h], 'root': [float(rows.min() / h), float(rows.max() / h)]}
        print('vây (fins.png)', spec['name'], w, 'x', h)

    # ---- mắt, miệng ------------------------------------------------------------------
    eyes = key_out(art / 'eyes.png')
    ec, _ = components(eyes[..., 3] > 128)
    for name, c in zip(cfg['eyesCells'], ec):
        x0, y0, x1, y1 = c[:4]
        im = save(eyes[max(0, y0 - 6):y1 + 7, max(0, x0 - 6):x1 + 7], out / f'{name}.webp', maxside=256, quality=90)
        meta[name] = {'size': list(im.size)}
    json.dump(meta, open(out / 'meta.json', 'w', encoding='utf-8'))
    print('xong →', out)


if __name__ == '__main__':
    main()

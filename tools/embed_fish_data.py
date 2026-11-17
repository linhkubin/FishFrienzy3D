"""Nhúng ảnh đã cắt (art/<ca>/cut/*.webp) + meta.json vào file dựng cá (demo/<ca>.js), giữa hai dấu
/*<TEN>_TEX_BEGIN*/ ... /*<TEN>_TEX_END*/  (bước 4 trong docs/quy-trinh-ve-ca.md).
Nhúng dạng base64 để mở thẳng trang từ ổ đĩa (file://) vẫn chạy.

Cách dùng:
    python tools/embed_fish_data.py art/clownfish/cut demo/clownfish.js CLOWN

Mọi file .webp trong thư mục cut được nhúng, khoá = tên file bỏ đuôi; riêng body_tex.webp → khoá "body".
"""
import sys, json, base64, re
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path


def main():
    if len(sys.argv) != 4:
        print(__doc__); sys.exit(1)
    cut, js, tag = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    meta = json.load(open(cut / 'meta.json', encoding='utf-8'))
    tex = {}
    for f in sorted(cut.glob('*.webp')):
        key = 'body' if f.stem == 'body_tex' else f.stem
        tex[key] = 'data:image/webp;base64,' + base64.b64encode(f.read_bytes()).decode()
    blob = json.dumps({'tex': tex, 'meta': meta}, separators=(',', ':'))
    s = js.read_text(encoding='utf-8')
    pat = re.compile(r'/\*' + tag + r'_TEX_BEGIN\*/.*?/\*' + tag + r'_TEX_END\*/', re.S)
    if not pat.search(s):
        sys.exit(f'Không thấy dấu /*{tag}_TEX_BEGIN*/ … /*{tag}_TEX_END*/ trong {js}')
    s = pat.sub(lambda m: f'/*{tag}_TEX_BEGIN*/{blob}/*{tag}_TEX_END*/', s)
    js.write_text(s, encoding='utf-8', newline='')
    print(f'Đã nhúng {len(tex)} ảnh ({len(blob) // 1024} KB) vào {js}')


if __name__ == '__main__':
    main()

#!/usr/bin/env bash
# Chụp ảnh trang 3D bằng Chrome chạy ngầm (bước 5 trong docs/quy-trinh-ve-ca.md).
# Cách dùng:
#   tools/shot.sh out.png "creatures.html#studio/clown/normal/side"        # mở thẳng file
#   tools/shot.sh out.png "http://localhost:8123/index.html" 900x700        # qua máy chủ cục bộ (demo bơi)
# Tham số 3 (tuỳ chọn): kích thước cửa sổ, mặc định 1440x860.
# Địa chỉ phòng xem chi tiết: #studio/<id>/<biểu cảm>/<góc>
#   góc: side top front back under · biểu cảm: normal open scared narrow dizzy
set -e
OUT="$1"; PAGE="$2"; SIZE="${3:-1440x860}"
CHROME="${CHROME:-/c/Program Files/Google/Chrome/Application/chrome.exe}"
ROOT="$(cd "$(dirname "$0")/.." && pwd -W 2>/dev/null || pwd)"
case "$PAGE" in http*) URL="$PAGE" ;; *) URL="file:///$ROOT/demo/$PAGE" ;; esac
PROFILE="${TMPDIR:-/tmp}/fish-shot-profile"
# SwiftShader đôi khi làm tiến trình vẽ bị dừng → thử lại tối đa 3 lần
for i in 1 2 3; do
  rm -f "$OUT"
  timeout 150 "$CHROME" --headless=new --user-data-dir="$PROFILE" --use-angle=swiftshader --enable-unsafe-swiftshader \
    --hide-scrollbars --window-size="${SIZE/x/,}" --virtual-time-budget=4000 --screenshot="$OUT" "$URL" >/dev/null 2>&1 || true
  [ -f "$OUT" ] && { echo "đã chụp → $OUT"; exit 0; }
done
echo "chụp thất bại: $URL" >&2; exit 1

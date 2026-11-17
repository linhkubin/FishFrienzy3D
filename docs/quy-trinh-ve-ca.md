# Quy trình vẽ và dựng một loài cá 3D từ tranh

Cách làm đã dùng cho **bé cá vàng** (`demo/goldfish.js`) và **cá hề** (`demo/clownfish.js`). Ý tưởng: **Codex chỉ vẽ tranh, Claude dựng 3D bám theo tranh** — không tự sáng tác hình dáng. Nhìn ngang cá giống hệt tranh; các góc khác có khối thật.

---

## Bước 1 — Viết mô tả loài cá

Tạo `docs/<ten-ca>-mo-ta.md` (xem mẫu `docs/be-ca-vang-mo-ta.md`, `docs/ca-he-mo-ta.md`), gồm:

- **Tỷ lệ thân** (dài : cao, không tính vây), độ lớn đầu, vị trí và cỡ mắt.
- **Màu** từng vùng bằng mã hex (lưng, hông, bụng, mặt), hoa văn (vảy, sọc…).
- **Miệng / môi**: hình dáng (chu, cười…), màu.
- **Từng vây**: hình dáng, màu gốc → mép, viền.
- **Phong cách**: phong cách 2 "khối đơn giản", chất liệu đất sét mềm, cùng kiểu mắt với bé cá vàng.

## Bước 2 — Codex vẽ bộ tranh

Chạy Codex **chỉ để tạo ảnh**, không sửa code (model `gpt-6.1-sol`, reasoning `medium`):

```bash
codex exec --skip-git-repo-check -s workspace-write -m gpt-6.1-sol -c model_reasoning_effort=medium -C "D:/Unity/WebGames/Fish" - < prompt.txt
```

Bộ tranh lưu vào `art/<ten-ca>/`:

| File | Nội dung | Dùng để |
|---|---|---|
| `side.png` | Toàn thân nhìn ngang, đầu quay phải, đủ vây | **Cắt vây** (side − body) |
| `body.png` | Đúng thân trong `side.png`, **bỏ hết vây** | Đường viền thân + **dán lên hai hông** |
| `fins.png` | Các vây tách rời | Vây ngực (tấm riêng) |
| `top.png` | Nhìn từ trên | Ước lượng độ dày thân |
| `front.png` | Nhìn từ trước | Mặt cắt thân, kiểm tra |
| `eyes.png` | 5 kiểu mắt + 2 kiểu miệng | Mắt đổi biểu cảm |
| `mouth/side.png`, `mouth/front.png`, `mouth/open-front.png` | Cận cảnh miệng | Tham chiếu dựng môi |

**Yêu cầu bắt buộc trong prompt:**
- Nền phẳng hồng tím `#FF00FF`, không bóng đổ xuống nền.
- Ánh sáng đều, nhìn thẳng (orthographic), không viền đen quanh cả con cá, không chữ.
- Vẽ `side.png` **trước**, rồi dùng nó làm mẫu cho mọi ảnh khác.
- `body.png` phải **trùng khít vị trí và kích thước** với `side.png` (quan trọng nhất — để cắt vây chuẩn).
- Đưa kèm bộ tranh cá vàng làm mẫu phong cách.

Xem lại ảnh; ảnh nào sai luật thì bảo Codex vẽ lại.

## Công cụ (thư mục `tools/`)

| Công cụ | Việc làm | Bước |
|---|---|---|
| `tools/cut_fish_art.py <art/ca> [--out dir]` | Tách nền, cắt thân / vây / mắt, đo đường viền, tạo ảnh da thân, ghi `cut/meta.json`. Đọc cấu hình `art/<ca>/cut-config.json` | 3 |
| `tools/embed_fish_data.py <art/ca/cut> <demo/ca.js> <TEN>` | Nhúng ảnh + meta vào file dựng cá (giữa `/*<TEN>_TEX_BEGIN*/…/*<TEN>_TEX_END*/`) | 4 |
| `tools/shot.sh <out.png> <trang> [WxH]` | Chụp trang bằng Chrome chạy ngầm, tự thử lại khi lỗi | 5 |

Cần Python 3 với Pillow và numpy. Ví dụ với cá hề:

```bash
python tools/cut_fish_art.py art/clownfish
python tools/embed_fish_data.py art/clownfish/cut demo/clownfish.js CLOWN
bash tools/shot.sh out.png "creatures.html#studio/clown/normal/side"
```

`art/<ca>/cut-config.json` (xem mẫu `art/clownfish/cut-config.json`):
- `finsCells`: tên và góc xoay từng ô vây trong `fins.png`, theo thứ tự đọc (trên → dưới, trái → phải). Xoay sao cho **gốc vây nằm ở mép phải**.
- `eyesCells`: tên từng ô trong `eyes.png`, theo thứ tự đọc.
- `sideFinNames`: tên các mảng vây lẻ cắt từ side − body, theo thứ tự đọc.
- `mouthBox`, `snoutRef`: vùng miệng vẽ sẵn cần xoá, và cột màu kéo dài ra mõm.

Chạy thử với `--out` ra thư mục tạm trước, mở ảnh kiểm tra thứ tự các ô có đúng tên không, rồi mới ghi vào `cut/`.

## Bước 3 — Tách nền và cắt bộ phận (`tools/cut_fish_art.py`)

Kết quả lưu ở `art/<ten-ca>/cut/` (ảnh `.webp` + `meta.json`).

1. **Tách nền**: mỗi điểm ảnh lấy độ trong suốt theo khoảng cách màu tới màu nền (lấy trung vị ở viền ảnh), rồi khử viền hồng (despill).
2. **Thân** (`body.png`): cắt khung bao, lưu `body.size` và `body.profile` = mép trên/dưới của thân theo từng cột (64 điểm) — đây là đường viền để dựng khối.
3. **Vị trí mắt**: tìm vùng không phải màu da quanh con ngươi → tâm và đường kính mắt (`body.eye`).
4. **Ảnh da thân** (`body_tex.webp`):
   - **Xoá mắt vẽ sẵn** (vòng tròn quanh mắt, rộng hơn mắt ~25%) và **xoá miệng vẽ sẵn** (vùng chóp mõm), lấp bằng cách loang màu da xung quanh vào — vì mắt và môi sẽ là khối 3D riêng.
   - Phần mõm phía trước: **kéo dài cột màu ngay sau chỗ nối** ra phía trước (giữ đậm nhạt trên–dưới) để mõm cùng tông thân, không vệt.
   - Loang màu ra ngoài viền để khi chiếu lên mép thân không ăn màu nền.
5. **Vây lẻ** (đuôi, vây lưng, hậu môn, vây bụng): lấy **`side.png` trừ `body.png`** → phần còn lại là vây **đúng vị trí trong tranh**. Lưu ảnh vây và khung toạ độ pixel (`sideFins`).
6. **Vây ngực**: cắt từ `fins.png`, xoay sao cho **gốc vây ở mép phải**, ghi `root` (khoảng dọc của gốc), **làm mờ dần mép gốc** (~12% bề rộng) để liền thân.
7. **Mắt / miệng**: cắt từng ô trong `eyes.png`.

## Bước 4 — Dựng 3D (file `demo/<ten-ca>.js`)

Sao chép `demo/clownfish.js` thành file mới (đây là bản theo đúng quy trình này; `goldfish.js` dùng bộ vây cắt từ `fins.png`), đổi tên thư viện (`window.<Ten>Lib`), dấu dữ liệu (`/*<TEN>_TEX_BEGIN*/…/*<TEN>_TEX_END*/`) rồi nhúng dữ liệu bằng `tools/embed_fish_data.py` (base64, để mở thẳng file vẫn chạy). Sau đó chỉnh các phần riêng dưới đây.

**Hệ toạ độ:** thân dài 1, `x` từ −0.5 (đuôi) → +0.5 (mũi), `y` lên, `z` sang hông.

### 4.1 Thân
- **Khối tiện theo đường viền tranh**: mỗi vòng cắt ngang lấy cao từ `profile`, bề ngang = cao × `widthK` (cá vàng 0.84, cá hề 0.82).
- **Mặt cắt hình quả trứng**: bề ngang nhân `egg(t) = 1 − 0.2·t` (bụng rộng hơn lưng) → cá béo tròn. Dùng **cùng một hàm** cho thân, mõm (SDF), vị trí mắt và vây (`surf`).
- **Dán tranh**: tranh da thân chiếu lên hai hông theo vị trí dọc trong đường viền.

### 4.2 Mõm + môi — **một lưới liền với thân**
- Thân tiện tới `uB ≈ 0.905`, rồi khép **vòm mũi** có độ cong khớp **cả giá trị lẫn độ dốc** của thân tại chỗ nối (nếu không sẽ lồi một cục trước mắt).
- Mặt + môi + khe miệng mô tả bằng **hàm khoảng cách (SDF)**: môi trên / môi dưới là các khối elip ghép mềm (smooth union) vào mặt; khe miệng là khối elip mỏng khoét vào trong.
- Các đỉnh vùng mõm được **bắn tia theo pháp tuyến** tới bề mặt SDF → môi mọc ra từ chính da mặt, **không có đường nối**.
- **Giãn đều lưới** quanh môi (lặp ~120 lần: kéo về trung bình các đỉnh kề rồi chiếu lại lên bề mặt) để hết tam giác bị kéo dài; điểm chóp đặt ngay khe miệng.
- **Màu môi / lòng miệng**: tô theo khoảng cách SDF (môi trên sáng, môi dưới đậm, lòng miệng cam đậm dần vào trong). Da mõm dùng màu đều (không dùng tranh ở vùng này).
- **Há / khép miệng**: dịch chuyển đỉnh (`aOpen`, `aClose`) điều khiển bằng `uMouth`.
- Tham số riêng mỗi loài: `LIPU`, `LIPL` (tâm và bán kính khối môi), `CAV` (khe miệng), bảng màu môi.

### 4.3 Mắt
- **Vòm cầu lồi 3D** (chỏm cầu ~2×46°) đặt đúng chỗ mắt trên bề mặt, tranh mắt chiếu thẳng lên vòm → nhìn từ trên vẫn thấy mắt cong.
- Đổi biểu cảm bằng cách đổi ảnh mắt (bình thường, sợ hãi, nheo, choáng, nhắm), tự chớp mắt.

### 4.4 Vây
- **Vây lẻ** (cắt từ side − body): đặt đúng toạ độ trong tranh bằng phép đổi pixel → đơn vị thân (`PX`, `PY`). Vây bụng tách đôi, xoè nhẹ hai bên.
- **Vây ngực**: tấm riêng gắn ở gốc vây ngực trên bề mặt, quạt theo nhịp bơi.
- Vây uốn theo nhịp bơi bằng shader (`bendPatch`).

### 4.5 Nạp vào trang
- `creatures.html` và `index.html`: thêm `<script src="<ten-ca>.js">`, gọi `window.<Ten>Lib(THREE, { mergeGeometries, mergeVertices })`.
- Bộ sưu tập / phòng xem chi tiết: thêm vào `BUILD`, `ITEMS`, `STUDIO_IDS`.

## Bước 5 — Kiểm tra

Chụp bằng Chrome chạy ngầm (khung trình duyệt của app quá nhỏ / hay bị ẩn):

```bash
bash tools/shot.sh out.png "creatures.html#studio/<id>/normal/side"
bash tools/shot.sh swim.png "http://localhost:8123/index.html" 900x700
```

- Địa chỉ: `#studio/<id>/<biểu cảm>/<góc>` — góc `side`, `top`, `front`, `back`, `under`; biểu cảm `normal`, `open`, `scared`, `narrow`, `dizzy`.
- Kiểm tra các góc ngang, ba phần tư, trước, trên, há miệng, nheo mắt; **đặt cạnh tranh gốc** để so.
- Demo bơi `index.html` cần chạy qua máy chủ cục bộ (cấu hình `.claude/launch.json`, cổng 8123) vì trang nạp file `.js`.

## Những lỗi đã gặp và cách tránh

| Lỗi | Nguyên nhân | Cách tránh |
|---|---|---|
| Lộ hai lớp mắt | Mắt vẽ sẵn trên tranh thân lệch với mắt 3D | Xoá mắt khỏi tranh thân |
| Môi "tấu hề", nhô thành cục | Tự nặn môi bằng khối riêng / mõm nới rộng | Môi mọc từ da mặt (SDF + một lưới); làm theo ảnh tham chiếu miệng của Codex, không tự sáng tạo |
| Gờ bầu dục quanh miệng | Thân và mõm là hai lưới ghép | Một lưới liền |
| Cục lồi trước mắt | Vòm mũi bắt đầu phẳng | Vòm khớp độ dốc của thân |
| Vệt sọc / gạch vàng ở môi | Tranh bị kéo giãn ở mõm, lưới gấp nếp | Da mõm màu đều; giãn lưới; ẩn mặt trong |
| Vây lệch thân | Ước lượng vị trí từ ảnh vây tách rời | Cắt vây từ side − body (đúng toạ độ) |
| Môi "nhập" vào nhau, lưới lật | Thứ tự đỉnh tam giác ngược | Kiểm tra chiều quấn lưới khi môi trông rỗng/dẹt |

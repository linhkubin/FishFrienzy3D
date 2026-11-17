# Cá hề — mô tả để vẽ bộ ảnh dựng 3D

Loài cá chơi được, mở khóa ở khu 8 (Rạn san hô): miễn nhiễm hải quỳ, trốn được trong đó. Cùng phong cách 2 "khối đơn giản" và cùng chất liệu với bé cá vàng (`art/goldfish/side.png`): mềm như đất sét bóng nhẹ, dễ thương nhưng không trẻ con. Bộ ảnh dùng làm **kết cấu và đường viền** để dựng 3D, nên cần đúng tỷ lệ, sạch, nhất quán giữa các ảnh.

## Ngoại hình

- **Dáng:** cá hề con, thân hình bầu dục tròn, hơi dẹt hai bên. Dài : cao (không tính vây) ≈ 1,9 : 1. Lưng cong đều, bụng tròn, cuống đuôi ngắn và dày.
- **Đầu:** tròn, chiếm khoảng 30% chiều dài thân, mõm ngắn tròn.
- **Mắt:** to (≈ 1/4 chiều cao đầu), ở 1/3 trước của đầu, hơi cao hơn đường giữa. Tròng nâu cam ấm #6A3A1A, đồng tử đen, 2 đốm sáng trắng. Viền mắt cam sẫm mảnh. Không có mí ở mặt bình thường.
- **Miệng:** nhỏ ở chóp mõm, hơi thấp hơn đường giữa; môi mềm cam hồng nhạt, khép hờ, cong nhẹ như mỉm cười (không chu như cá vàng).
- **Màu thân:** cam tươi #F2711C, bụng sáng hơn #F7934A.
- **Ba sọc trắng** #FBF7EF, mỗi sọc có **viền đen mảnh** #1E1B1A:
  1. Sọc đầu: ngay sau mắt, cong như vòng cung ôm quanh đầu, rộng nhất ở giữa.
  2. Sọc thân: giữa thân, phình rộng ở giữa (như hình chữ C ngược / bóng đèn), hẹp ở lưng và bụng.
  3. Sọc đuôi: hẹp, ngay trước gốc đuôi.
- **Má:** vệt hồng rất nhạt dưới mắt.
- **Vây:** tròn, mềm, viền đen mảnh ở mép, có tia vây mảnh.
  - Vây lưng: hai phần, phần trước thấp nhọn tròn, phần sau cao tròn; màu cam, mép viền đen.
  - Đuôi: tròn như cái quạt (không chẻ), cam, mép viền đen + một dải trắng mảnh trong viền.
  - Vây ngực: tròn như mái chèo, cam trong, mép viền đen.
  - Vây bụng và vây hậu môn: tròn, cam, mép viền đen.

## Bộ ảnh cần vẽ (Codex)

Tất cả ảnh: **nền phẳng hồng tím #FF00FF**, ánh sáng đều mềm chiếu thẳng (không vệt sáng gắt, không bóng đậm), **hình chiếu thẳng** không phối cảnh, cá ở giữa đủ khoảng trống, không viền đen quanh cả con cá, không chữ.

| File | Nội dung |
|---|---|
| `art/clownfish/side.png` | Toàn thân nhìn ngang, đầu quay **sang phải**, đủ vây và đuôi, mắt mở bình thường. |
| `art/clownfish/body.png` | Đúng thân trong `side.png` (cùng tỷ lệ, vị trí, kích thước) nhưng **bỏ hết vây và đuôi**; giữ sọc, mắt, miệng. |
| `art/clownfish/fins.png` | Các vây tách rời, trải phẳng, cách xa nhau: đuôi, vây lưng (trước + sau), vây ngực, vây bụng, vây hậu môn. Gốc vây thẳng ở phía gắn vào thân. |
| `art/clownfish/top.png` | Nhìn từ trên xuống, đầu quay **lên trên**: độ dày thân (rộng nhất ≈ 0,55 chiều cao thân), hai mắt, vây ngực xòe. |
| `art/clownfish/front.png` | Nhìn thẳng từ trước: mặt cắt thân, hai mắt, miệng, sọc đầu ôm quanh. |
| `art/clownfish/eyes.png` | 5 kiểu mắt cùng góc ngang: bình thường, sợ hãi, nheo (mí cam sụp chéo), choáng (xoáy), nhắm; kèm 2 kiểu miệng: khép và há tròn. |
| `art/clownfish/mouth/side.png`, `mouth/front.png`, `mouth/open-front.png` | Cận cảnh đầu: miệng khép nhìn ngang, nhìn trước, và há tròn nhìn trước — để dựng môi. |

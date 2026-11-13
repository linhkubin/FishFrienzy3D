# Bé cá vàng — mô tả để vẽ bộ ảnh dựng 3D

Nhân vật chính của Bé Cá Phiêu Lưu, phong cách 2 "khối đơn giản" (xem `art/style-2-khoi-don-gian.png`). Bộ ảnh này dùng làm **kết cấu và đường viền** để dựng model 3D, nên cần đúng tỷ lệ, sạch và nhất quán giữa các ảnh.

## Ngoại hình

- **Loài:** cá vàng đuôi đôi (kiểu cá vàng ranchu lai đuôi dài), dáng cá con dễ thương nhưng không trẻ con.
- **Tỷ lệ thân (không tính vây):** dài : cao ≈ 1,6 : 1. Thân hình giọt nước tròn trịa, bụng sâu và tròn, lưng cong đều, cuống đuôi thon gọn.
- **Đầu:** to, tròn, chiếm khoảng 38% chiều dài thân. Trán hơi gồ. Mõm ngắn, tròn.
- **Mắt:** to (đường kính ≈ 1/4 chiều cao đầu), nằm ở 1/3 trước của đầu, hơi cao hơn đường giữa thân. Tròng nâu ấm #5B3A22 chiếm gần hết mắt, đồng tử đen, 2 đốm sáng trắng (một to ở góc trên trước, một nhỏ ở dưới). Viền mắt cam sẫm mảnh.
- **Miệng:** nhỏ, ở chóp mõm hơi thấp hơn đường giữa, môi hồng cam nhạt, khép hờ.
- **Màu thân:**
  - Lưng cam đậm #E0661C.
  - Hông cam tươi #EF8A33.
  - Bụng chuyển sang kem vàng #F7C88C.
  - Mặt và mõm màu kem cam nhạt #F8C588, chuyển mềm sang cam ở sau mang.
- **Má:** một vệt hồng rất nhạt dưới mắt, không tròn đậm.
- **Nắp mang:** đường cong mảnh, cam sẫm hơn thân một chút.
- **Vảy:** vảy hình vỏ sò xếp lớp rõ trên thân từ sau mang tới cuống đuôi. Mỗi vảy có mép sáng nhẹ, nhỏ dần về phía đuôi. Không có vảy trên đầu.
- **Vây:** mỏng như lụa, hơi trong, có tia vây mảnh màu kem.
  - Màu: gốc vây cam #EF8F45, chuyển dần sang cam đào nhạt #F8D2AE ở mép.
  - Mép vây sáng hơn, hơi gợn sóng.
- **Vây lưng:** cao, hình buồm, mọc từ đỉnh lưng (giữa thân), ngả ra sau.
- **Đuôi:** đuôi đôi dài bằng khoảng 0,9 lần thân, gồm 2 thùy trên và dưới xòe rộng, chẻ sâu ở giữa, mép thùy cong mềm như vải lụa.
- **Vây ngực:** 2 vây dài, mềm, ngay sau mang, chĩa ra sau và xuống.
- **Vây bụng:** 2 vây nhỏ dưới bụng.
- **Vây hậu môn:** đôi, nhỏ, gần cuống đuôi.

## Bộ ảnh cần vẽ (Codex)

Tất cả ảnh cần:
- **Nền phẳng một màu hồng tím #FF00FF** để tách nền. Không vẽ chi tiết nền, không bóng đổ xuống nền.
- **Ánh sáng đều, mềm, chiếu thẳng**: chỉ sáng tối nhẹ theo khối, không có vệt sáng gắt hay bóng tối đậm, vì ảnh sẽ được dán lên model 3D đã có ánh sáng riêng.
- **Hình chiếu thẳng (orthographic)**, không phối cảnh, cá nằm giữa, đủ khoảng trống quanh mép.
- **Không viền đen, không chữ.**

| File | Nội dung |
|---|---|
| `art/goldfish/side.png` | Toàn thân nhìn ngang, đầu quay **sang phải**, đầy đủ vây và đuôi, mắt mở bình thường. |
| `art/goldfish/body.png` | Đúng thân trong `side.png` (cùng tỷ lệ, cùng vị trí, cùng kích thước) nhưng **bỏ hết vây và đuôi**, chỉ còn thân, đầu, mắt, miệng. |
| `art/goldfish/fins.png` | Các vây tách rời, trải phẳng, cách xa nhau: đuôi đôi (hai thùy), vây lưng, vây ngực, vây bụng, vây hậu môn. Mỗi vây có gốc thẳng ở phía gắn vào thân. |
| `art/goldfish/top.png` | Nhìn thẳng từ trên xuống, đầu quay **lên trên**, để thấy độ dày thân (rộng nhất ≈ 0,6 chiều cao thân), hai mắt lồi hai bên, vây ngực xòe. |
| `art/goldfish/front.png` | Nhìn thẳng từ phía trước (mặt cá), để thấy mặt cắt ngang tròn của thân, hai mắt, miệng. |
| `art/goldfish/eyes.png` | Bảng 5 kiểu mắt cùng góc nhìn ngang: bình thường, sợ hãi (mắt to, đồng tử nhỏ), nheo (mí cam sụp chéo, thấp về phía mũi), choáng (mắt xoáy), nhắm. Kèm 2 kiểu miệng: khép và há tròn. |

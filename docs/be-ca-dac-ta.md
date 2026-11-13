# Bé Cá Phiêu Lưu — Đặc tả theme và bối cảnh: Bể cá

Khu đầu tiên của game. Bé cá vàng bắt đầu hành trình trong một bể kính đặt ngoài hiên nhà.

## 1. Phong cách chung — "khối đơn giản" (phong cách 2, đã chốt 13/11/2026)

Ảnh tham chiếu: `art/style-2-khoi-don-gian.png`. Bản dựng 3D theo phong cách này: `demo/creatures.html`. Mục tiêu là **dễ thương nhưng trưởng thành**, cho thiếu niên và người lớn, không phải phong cách đồ chơi trẻ em.

- **Hình khối:** gọn, ít chi tiết, mặt phẳng lộ rõ (low-poly, đổ bóng phẳng từng mặt). Bề mặt chuyển màu mềm, không có viền đen quanh vật.
- **Ánh sáng và sương nước làm phần lớn không khí:** nắng ấm từ trên chiếu xuống, vệt sáng lay động trên đáy, tia nắng xiên, càng xa càng chìm vào màu xanh ngọc.
- **Bảng màu hạn chế** khoảng 5 màu cho mỗi khu, cộng màu cam của bé cá làm điểm nhấn.
- **Mắt:** chỉ **bé cá** (và trùm) có mắt to biểu cảm: tròng nâu, đồng tử, 2 đốm sáng, mí mắt đổi được. Các loài khác có mắt nhỏ kiểu cá thật, không cười.
- **Má hồng:** chỉ bé cá có một chút. Không loài nào khác có.
- **Kẻ săn trông đáng sợ thật:** dáng sắc, mí nheo chéo, viền đỏ mảnh theo luật ăn.
- **Đồ trang trí cũ, có câu chuyện:** tàn tích đá phủ rêu, sơn bong tróc, gỗ cũ viền đồng xỉn.
- **Lấp lánh** chỉ dùng cho thứ quan trọng: ngọc trai, bong bóng, bong bóng sao.
- **Biểu cảm của bé cá:** bình thường, há miệng (lao đớp), sợ hãi (mắt to, đồng tử nhỏ), nheo mắt (mí sụp chéo, lúc lao săn), choáng (mắt xoáy).
- **Không máu me:** bị nuốt là "ực" kèm bong bóng ợ; cắn trúng bung ra bong bóng sao lấp lánh.

## 2. Bảng màu bối cảnh

| Thành phần | Màu |
|---|---|
| Nước, sương xa | Xanh ngọc đậm #2B6765; vạt mặt nước phía trên sáng hơn, có gợn |
| Ánh nắng | Vàng ấm #FFF0D2, vệt sáng mạng lưới lay động trên đáy |
| Sỏi đáy | Đá cuội dẹt màu cát và xám be (#CCB596, #BEA685, #B19B80, #A6937C…); rất ít viên gỉ cam hoặc xám xanh |
| Đá to | Xám nhạt #A19F96, mặt trên có ít rêu #86955A |
| Rong, cây | Xanh rêu ô liu #56723D → #8FA56A; cây lá đỏ cam #B4563A → #E48D62 |
| Lâu đài | Đá xếp màu be #D6C4A0, mái ngói san hô #DE876A, rêu và dây thường xuân, cờ vàng mù tạt #D9AE4F |
| Kim loại | Đồng xỉn #A8863F |
| Viền luật ăn | Đỏ #E0573D (nó nuốt được bạn) |

## 3. Bối cảnh: bể kính ngoài hiên

- **Hình dạng:** bể kính chữ nhật, tỷ lệ dài : sâu : cao khoảng 2 : 1 : 1. Khung bể viền nhựa đen bo tròn, nắp có đèn.
- **Camera:** nhìn chéo khoảng 45° từ phía trước và trên xuống. Thấy được đáy, tầng giữa và mặt nước cùng lúc.
- **Thành kính:** có vệt phản chiếu chéo nhẹ và vài bong bóng nhỏ bám kính. Cá chạm kính thì trượt dọc theo.

### Decor (đồ trang trí) — mỗi món có vai trò trong lối chơi

1. **Lâu đài cổ (trung tâm bể):** tàn tích đá xếp màu be, 3 tháp tròn, mái ngói san hô xếp 3 tầng mép răng cưa, rêu ở mép mái, dây thường xuân bò trên tường, cờ vàng trên đỉnh, cửa sổ tròn sáng ấm, cổng vòm tối. Cá cấp 1–2 chui qua được cổng, cá lớn thì không. Cá xiêm canh lãnh thổ quanh lâu đài (ở các màn sau).
2. **Rương báu:** gỗ cũ ba tấm ván, viền và khóa đồng xỉn, nắp cong mở ra sau, lót nhung đỏ sẫm, ngọc trai trắng ánh hồng; nhả ngọc trai theo chu kỳ.
3. **Tàu ngầm đồ chơi (mối nguy):** thân tròn như quả trứng, sơn vàng mù tạt bong tróc, đai nâu gỉ ở đuôi, 2 cửa kính tròn viền đồng có đinh tán, tháp nhỏ với đèn đỏ nhấp nháy, chân vịt quay. Chạy vòng quanh lâu đài theo đường cố định.
4. **Ống sục khí (mối nguy):** đá sủi tròn màu xanh xám có lỗ li ti, vòi nhỏ trên đỉnh. Phun bong bóng nhỏ liên tục và chùm bong bóng lớn theo chu kỳ; bong bóng trong suốt, viền sáng ánh cầu vồng.
5. **Vỏ ốc lớn:** vỏ ốc xoắn màu kem nằm nghiêng, mặt xoắn quay ra ngoài, miệng vỏ hồng nhạt là chỗ trốn cho cá cấp 1.
6. **Hòn đá nổi:** tảng đá phẳng nhô gần mặt nước, rùa con nằm phơi mai trên đó.
7. **Cây nhựa và rong thật:** cây nhựa cao lá to nhiều màu; bụi rong mềm rẽ ra khi cá nhỏ đi qua.
8. **Khúc gỗ lũa:** nằm chéo, cá tỳ bà bám vào (màn sau).
9. **Vài món vui:** thợ lặn đồ chơi bé xíu, cây cầu vòm nhỏ, nấm đồ chơi.

### Không khí
- Vệt sáng đèn lay động trên đáy (caustics).
- Bụi lấp lánh lơ lửng trôi chậm.
- Bong bóng nhỏ lẻ tẻ nổi lên từ sỏi.
- Ngoài kính mờ thấy hiên nhà: chậu cây, cột nhà, bầu trời. Các màn cuối khu, trời tối dần để báo trước bão.

## 4. Sinh vật cho demo đầu tiên (8 loài)

Kích thước tính theo bé cá cấp 1 = 1,0.

| Sinh vật | Cấp | Kích thước | Ngoại hình (phong cách 2) | Hành vi |
|---|---|---|---|---|
| **Bé cá vàng** (người chơi) | 1→5 | 1,0 → 4,5 | Cam đậm có vảy, bụng kem, đuôi đôi mỏng như lụa màu cam đào, mắt to tròng nâu, má hơi ửng | Nhân vật chính |
| **Cám cá** | 0 | 0,15 | Vụn cám dẹt màu cam | Rơi thành vệt chéo từ mặt nước |
| **Cá neon** | 1 | 0,7 | Thân thon xám bạc, sọc xanh hơi phát sáng, nửa sau bụng đỏ, mắt nhỏ | Đàn 10–15 con, co cụm khi hoảng |
| **Cá bảy màu** | 1 | 0,8 | Thân bạc xanh nhỏ, đuôi xòe màu san hô có tia vây | Đàn 5–8 con, đổi hướng gắt |
| **Tôm càng xanh con** | 2 | 1,2 | Xanh lục trong mờ, thân đốt, mắt đen trên cuống, râu dài cong, càng nhỏ | Sống ở đáy; hoảng thì búng giật lùi rồi khựng lại; càng kẹp phía trước |
| **Cá mún** | 2 | 1,3 | Thân tròn đỏ cam, vây lưng sẫm | Lẻ hoặc cặp, lượn chậm |
| **Cá ông tiên** | 3 | 2,2 | Thân dẹt cao màu kem bạc, 3 sọc xám đậm kéo cả vào vây, vây lưng và vây hậu môn dài vút, mí nheo chéo | Kẻ săn đầu tiên, săn cấp 1–2, quay đầu chậm |
| **Cá hồng két** | 4 | 3,2 | Tròn, màu san hô, môi chúm, mí lười biếng | Kẻ săn chính, chậm nhưng tham ăn |
| **Rùa tai đỏ con** | — | 2,5 | Mai ô liu từng mảng, viền và đường mảng vàng nhạt, vệt đỏ sau mắt | Không ai ăn được; nằm phơi trên đá phẳng; đớp cá cấp 1–2 đi ngang miệng |

Trùm cá la hán (cấp 6, kích thước 7,0): thân đỏ cam lấm tấm chấm ánh ngọc, vệt đen dọc thân, u trán to, môi dày, mí lười biếng kiêu căng.

## 5. Mối nguy

- **Ống sục khí:** cứ 4–6 giây phun một chùm bong bóng lớn; trước đó 1 giây có bọt nhỏ sủi lên. Cá chạm bong bóng lớn bị nhốt 2 giây, trôi lên, rồi bong bóng vỡ và cá bơi tiếp. Áp dụng cho mọi con cá.
- **Tàu ngầm đồ chơi:** chạy vòng quanh lâu đài, tốc độ khoảng 70% bé cá, đèn nhấp nháy và tiếng động cơ. Va trúng thì bị hất văng, choáng 0,8 giây. Cá săn không lao xuyên qua tàu nên có thể nấp sau tàu.

## 6. Vật phẩm

- **Cám cá:** cứ 15–20 giây rơi một cụm 6–10 viên; có bóng tròn trên mặt nước báo trước.
- **Ngọc trai từ rương báu:** tiền trong game.

## 7. Góc nhìn và camera khi chơi

Mục tiêu: người chơi luôn đọc được **kích thước, khoảng cách và độ cao** của mọi con cá, trong khi bể vẫn trông là một khối 3D thật.

### Góc nhìn
- **Hướng nhìn:** từ phía trước bể, chếch từ trên xuống. Góc nghiêng (pitch) **khoảng 40° so với mặt phẳng ngang** (bản dựng thử: camera cách điểm nhìn ~14,6 đơn vị). Người chơi thấy cùng lúc mặt đáy sỏi, mặt trước lâu đài, thân cá và vạt nước phía sau.
- **Cá nghiêng hông về phía camera:** vì camera nhìn chếch từ trên, mỗi con cá tự nghiêng thân quanh trục dọc (tối đa khoảng 45°) để hông cá hướng về camera. Nhờ vậy người chơi luôn thấy rõ thân, sọc và kích thước, kể cả loài thân dẹt như cá ông tiên. Cá bơi thẳng về phía camera thì không nghiêng.
- **Không xoay ngang (yaw cố định):** camera luôn nhìn vào bể từ cùng một phía. Trái/phải trên màn hình luôn là trái/phải của bể, lên trên màn hình là đi vào phía trong bể.
- **Phối cảnh nhẹ:** FOV dọc khoảng 35–40°, để vật ở xa và gần không méo nhiều khi so kích thước.
- **Kính mặt trước không vẽ** (camera ở bên trong lớp kính trước). Vẫn thấy khung bể và kính hai bên, kính sau.

### Theo dõi người chơi
- Camera **bám theo bé cá**, có độ trễ mềm (khoảng 0,25 giây) để không giật.
- **Nhìn trước theo hướng bơi:** tâm khung hình lệch về phía cá đang bơi tới khoảng 15% màn hình, để người chơi thấy mồi và nguy hiểm phía trước.
- **Không ra ngoài bể:** camera dừng ở mép bể; khi cá ở sát thành kính thì cá lệch khỏi tâm thay vì camera nhìn ra ngoài.
- **Khung hình theo cấp:** bé cá luôn chiếm khoảng **8–10% chiều cao màn hình**. Khi lên cấp, camera lùi ra xa và nâng cao hơn trong khoảng 0,5 giây (kèm hiệu ứng "bloop"). Ở cấp 1 thấy khoảng 1/4 bể; ở cấp 5 thấy gần cả bể, bể trông chật lại.

### Độ sâu (chiều cao trong nước)
- Người chơi chỉ điều khiển bằng **một cần điều khiển**: hướng kéo trên màn hình là hướng bơi trên mặt phẳng ngang của bể.
- **Độ cao của cá do game tự quyết:** cá càng nhỏ bơi càng sát đáy, lên cấp thì nổi lên một tầng; địa hình (sỏi, lâu đài, đá) tự nâng hạ cá; lao về con mồi ở tầng dưới thì tự chúi xuống đớp rồi trở về tầng của mình.
- **Đọc độ cao:** mỗi con cá có **bóng đổ tròn mờ trên nền sỏi** ngay dưới thân. Khoảng cách giữa cá và bóng cho biết cá cao hay thấp. Cá ở xa camera (sâu vào trong bể) nhạt dần trong sương nước.

### Không để vật che khuất
- Đồ trang trí cao (lâu đài, cây nhựa, rong) **trong suốt dần** khi nằm giữa camera và bé cá, và hiện lại bóng dáng bé cá dạng viền sáng.
- Cá lớn ở tầng trên, gần camera hơn bé cá, cũng trong suốt bớt khi che bé cá.

### Hiệu ứng camera
- Rung rất nhẹ khi đớp chuỗi dài, khi bị đớp, khi tàu ngầm va trúng.
- Phóng to nhẹ (khoảng 5%) khi vào Hăng mồi, trở lại khi hết.
- Không bao giờ để camera tự xoay hay cắt cảnh giữa lúc đang chơi.

### Màn hình
- Ưu tiên **màn hình ngang 16:9** (điện thoại xoay ngang và trình duyệt). Màn hình dọc thì camera lùi ra thêm để giữ đủ khung nhìn ngang.

## 8. Giao diện trong màn (HUD)

Ít và gọn, không che vùng chơi ở giữa.

- **Góc trên bên trái:** thanh tăng trưởng nằm ngang, chia 5 nấc theo cấp, mỗi nấc có biểu tượng mặt bé cá to dần; đầy thanh thì nấc sáng lên.
- **Giữa phía trên:** bộ đếm chuỗi đớp ("x5!") chỉ hiện khi đang chuỗi; khi vào Hăng mồi thì viền màn hình ánh vàng.
- **Góc trên bên phải:** số ngọc trai và nút tạm dừng.
- **Nửa trái dưới:** cần điều khiển nổi, chỉ hiện ở nơi ngón tay chạm.
- **Góc dưới bên phải:** 3 chấm hơi sức của cú lao (chạm đúp bất kỳ đâu để lao).
- **Mép màn hình:** mũi tên đỏ nhấp nháy khi kẻ săn sắp vào khung hình.
- **Trên mỗi con cá:** viền màu theo luật ăn — xanh: bạn ăn được; vàng: cùng cấp, chỉ cắn được; đỏ: nó nuốt được bạn; xám: không ai ăn được (rùa). Viền mảnh, chỉ hiện với cá trong khoảng gần.

# Problem statement + downstream contract

## Bài toán

Gắn box + phân loại theo tầng (`sign_family` → `sign_class`) cho **biển báo giao thông Đức** trong ảnh camera trước
xe, và đánh dấu biển đó có **áp dụng cho làn/hướng đi của ego** hay không — khó nhất ở biển nhỏ/xa không đọc được
chữ số, biển bị che/ngược sáng, biển đặt ở giao lộ phục vụ đường khác, và các vật giống biển nhưng không phải biển
(biển chỉ đường, biển quảng cáo, mặt sau biển, tiêu phản quang).

## Downstream contract

1. **Downstream task / model / user là ai?** Detector + classifier biển báo cho tính năng hỗ trợ lái (ISA: nhắc tốc
   độ giới hạn, cảnh báo STOP/nhường đường/cấm vào) trên đường nội đô và ngoại ô Đức.
2. **Output annotation nào thực sự cần?** Box ôm mặt biển; `sign_family` (7 nhóm theo hình dạng + màu, luôn gán
   được khi thấy hình dạng); `sign_class` (biển cụ thể, `unknown` khi không đọc được); `relevant_to_ego`
   (`yes`/`no`/`unknown`); cờ `needs_review`. Tag ảnh `no_target_sign` cho ảnh đã kiểm mà không có biển trong scope.
3. **Failure nào gây hậu quả lớn nhất?** (a) Bỏ sót hoặc gán `relevant_to_ego=no` cho biển STOP / nhường đường /
   cấm vào / mandatory đang áp dụng cho ego → xe không dừng hoặc đi sai hướng. (b) Sai **giá trị** tốc độ giới hạn
   (30 ↔ 50/80) → ISA nhắc sai tốc độ. (c) Đoán class khi không đọc được (model học nhãn sai có độ tin cao).
   Đây là các decision `critical` trong gold.
4. **Khi ambiguity không resolve được, ai / ở đâu là escalation path?** Annotator giữ box, gán giá trị `unknown`
   cho attribute không chắc và tick `needs_review=true` trên object (hoặc tag ảnh `image_escalate` nếu cả ảnh
   không đủ bằng chứng). QA owner xử lý hàng đợi `needs_review` mỗi batch; câu trả lời thành rule mới trong guideline
   (tăng version) — không trả lời bằng miệng.

## Scope

- **Trong scope (bắt buộc label):** mọi biển báo giao thông theo luật (StVO) nhìn thấy **mặt trước**, chiều cao mặt
  biển ≥ 12 px: danger (tam giác đỏ), prohibitory (tròn viền đỏ, gồm tốc độ), mandatory (tròn xanh), priority (STOP,
  nhường đường, đường ưu tiên), informative (vuông/chữ nhật xanh: qua đường, một chiều…), supplementary (biển phụ
  trắng gắn dưới biển chính).
- **Ngoài scope (ignore, không vẽ):** biển chỉ đường/địa danh (nền vàng, xanh, trắng có tên địa điểm hoặc số
  đường), mặt sau biển, biển quảng cáo/cửa hàng/tên phố, gương cầu, tiêu phản quang/tiêu hướng dẫn kẻ sọc (Leitbake,
  biển mũi tên đỏ-trắng ở khúc cua), rào chắn, đèn giao thông, biển nhỏ hơn 12 px.
- **Geometry tolerance:** box ôm phần mặt biển **nhìn thấy** (gồm viền, không gồm cột và biển phụ); mỗi cạnh lệch
  ≤ 2 px (biển < 30 px) hoặc ≤ 10 % cạnh biển (biển lớn) là đạt.

## Output chấm được

Blind test có: LABEL (số box theo từng biển), IGNORE (không có box trên biển chỉ đường / mặt sau / tiêu phản quang),
class + family, attribute `relevant_to_ego`, UNKNOWN (`sign_class=unknown` hoặc `relevant_to_ego=unknown`),
ESCALATE (`needs_review=true`), geometry (box không gồm cột/biển phụ). Tất cả nằm trong export CVAT for images 1.1:
label, attribute và tag ảnh.

## Dữ liệu và giới hạn

17 ảnh GTSDB (1360×800, ban ngày, Đức, mùa thu): 4 example, 7 calibration, 5 blind. Giới hạn: không có ảnh đêm/mưa;
chỉ biển Đức nên taxonomy không áp nguyên cho BDD (Mỹ); ảnh tĩnh nên relevance chỉ suy từ vị trí biển và hình học
đường trong một khung hình.

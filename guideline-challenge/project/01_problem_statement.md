# Problem statement + downstream contract

## Bài toán

Gắn box + phân loại theo tầng (`sign_family` → `sign_class`) cho **biển báo giao thông Việt Nam (QCVN 41)** trong
ảnh camera hành trình, và đánh dấu biển có **áp dụng cho hướng đi của ego** hay không — khó nhất ở biển nhỏ/xa
(38 % box trong dataset cao < 20 px), biển tạm trên rào công trường, cột nhiều biển ở giao lộ/dải phân cách, và vật
giống biển nhưng không phải biển QCVN (bảng dự án, bảng địa danh, quảng cáo dày đặc).

## Downstream contract

1. **Downstream task / model / user là ai?** Detector + classifier biển báo cho tính năng hỗ trợ lái (nhắc tốc độ
   giới hạn, cảnh báo cấm rẽ/quay đầu, đường cấm, công trường) trên đường nội đô và quốc lộ Việt Nam.
2. **Output annotation nào thực sự cần?** Box ôm mặt biển; `sign_family` (5 nhóm QCVN + `unknown`, theo hình dạng + màu, luôn gán
   được khi thấy hình dạng); `sign_class` (biển cụ thể, `unknown` khi không đọc được); `relevant_to_ego`
   (`yes`/`no`/`unknown`); cờ `needs_review`. Tag ảnh `no_target_sign` cho ảnh đã kiểm mà không có biển trong scope.
3. **Failure nào gây hậu quả lớn nhất?** (a) Bỏ sót hoặc gán `relevant_to_ego=no` cho biển đường cấm / cấm đi
   ngược chiều / cấm rẽ-quay đầu / hiệu lệnh đi vòng đang áp dụng cho ego → xe đi vào đường cấm hoặc sai hướng quanh
   chướng ngại vật. (b) Sai **giá trị** tốc độ / tải trọng / chiều cao → nhắc sai hoặc xe cao đâm dầm cầu. (c) Đoán class khi không đọc được (model học nhãn sai có độ tin cao).
   Đây là các decision `critical` trong gold.
4. **Khi ambiguity không resolve được, ai / ở đâu là escalation path?** Annotator giữ box, gán giá trị `unknown`
   cho attribute không chắc và tick `needs_review=true` trên object (hoặc tag ảnh `image_escalate` nếu cả ảnh
   không đủ bằng chứng). QA owner xử lý hàng đợi `needs_review` mỗi batch; câu trả lời thành rule mới trong guideline
   (tăng version) — không trả lời bằng miệng.

## Scope

- **Trong scope (bắt buộc label):** mọi biển QCVN nhìn thấy **mặt trước**, mặt biển cao ≥ 12 px: biển cấm, nguy
  hiểm/cảnh báo, hiệu lệnh (gồm biển làn), chỉ dẫn luật (qua đường, một chiều, cầu vượt, bến xe buýt…), biển phụ —
  kể cả biển tạm trên rào công trường.
- **Ngoài scope (ignore, không vẽ):** bảng địa danh/chỉ đường, bảng thông tin dự án, bảng "công trường đang thi
  công", băng rôn, quảng cáo/bảng quán, mặt sau biển, biển nhìn từ cạnh, rào/cọc/barie, đèn giao thông, biển < 12 px.
- **Geometry tolerance:** box ôm phần mặt biển **nhìn thấy** (gồm viền, không gồm cột và biển phụ); mỗi cạnh lệch
  ≤ 2 px (biển < 30 px) hoặc ≤ 10 % cạnh biển (biển lớn) là đạt.

## Output chấm được

Blind test có: LABEL (số box theo từng biển), IGNORE (không có box trên biển chỉ đường / mặt sau / tiêu phản quang),
class + family, attribute `relevant_to_ego`, UNKNOWN (`sign_class=unknown` hoặc `relevant_to_ego=unknown`),
ESCALATE (`needs_review=true`), geometry (box không gồm cột/biển phụ). Tất cả nằm trong export CVAT for images 1.1:
label, attribute và tag ảnh.

## Dữ liệu và giới hạn

16 ảnh từ dataset Kaggle *Vietnamese traffic signs detection and recognition* (Dat Nguyen, 2023; 1.170 ảnh
1622×626, nhãn YOLO 29 class): 4 example, 7 calibration, 5 blind, lưu ở `data/vtsd/VN01–VN16.png`. Nhóm dùng dataset
ngoài `data/` của template **với sự cho phép của Lab Coach/giảng viên**; license trên Kaggle ghi "Unknown" — chỉ dùng
học tập phi thương mại (xem `ATTRIBUTION.txt`). Giới hạn: ảnh là frame cắt từ video nên nhiều frame liền nhau cùng
cảnh, và dataset có ảnh trùng giữa train/val/test — nhóm chọn ảnh blind không cùng cảnh với example/calibration;
chỉ có ban ngày; nhãn gốc của dataset gộp một số loại (một class "speed limit" chung) nên không dùng làm gold.

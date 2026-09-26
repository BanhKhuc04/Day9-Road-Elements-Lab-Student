# QA plan + quality gates

Áp cho production label biển báo theo `02_guideline.md` (batch = 100 frame camera hành trình Việt Nam, 1 annotator / batch).

## Flow

Guideline → Calibration → Production → Self-QC → Review → Rework → Quality Gate.

- **Ai review, review bao nhiêu:** 1 reviewer (không phải người label batch đó) review **100 % ảnh có tag rủi ro** +
  **20 % ngẫu nhiên** phần còn lại của mỗi batch. Annotator mới (< 2 batch PASS): review 100 % batch đầu. Hàng đợi
  `needs_review=true` và tag `image_escalate` luôn được QA owner xử lý 100 %.
- **Chọn sample theo rule nào:** lát rủi ro lọc tự động từ export: (1) ảnh có box `sign_family ∈ {prohibitory,
  mandatory}` — lỗi ở đây là critical; (2) box nhỏ (cao < 25 px) hoặc `sign_class=unknown`; (3) ảnh có
  ≥ 4 box (giao lộ, dễ bỏ sót / nhầm relevance); (4) ảnh gắn `no_target_sign` (negative dễ bỏ sót biển). Phần 20 %
  ngẫu nhiên lấy từ ảnh không thuộc lát nào để đo lỗi nền.
- **Issue được ghi ở đâu, đóng thế nào:** reviewer mở issue CVAT trên đúng object (hoặc ảnh), ghi severity + mục
  guideline bị vi phạm. Annotator sửa rồi resolve; reviewer đóng issue sau khi kiểm lại. Batch chỉ qua gate khi không
  còn issue critical/major mở.
- **Khi phát hiện guideline gap:** issue gắn nhãn `question` → QA owner gom trong ngày, spec owner viết rule/ví dụ
  mới, tăng version guideline (v3 → v3.1…), ghi `08_revision_log.md`, dán lại Guide trong CVAT, thông báo annotator.
  Ảnh đã label theo bản cũ bị ảnh hưởng bởi rule mới được lọc lại bằng lát tương ứng và rework.

## Defect severity

| Severity | Định nghĩa cho project này | Ví dụ | Action mặc định |
|---|---|---|---|
| Critical | Lỗi làm downstream ra quyết định lái sai: bỏ sót / sai class / sai relevance ở biển `prohibitory` (gồm số tốc độ/tải trọng/chiều cao, đường cấm, cấm rẽ/quay đầu), `mandatory` hướng đi; đoán class khi không đọc được | Bỏ sót biển đường cấm trên rào công trường; `speed_limit_50` thay vì `speed_limit_60`; `keep_right` thay vì `keep_left`; cấm quay đầu gán `relevant_to_ego=no` | Rework ngay cả ảnh; đếm vào critical escape; ≥ 1 critical trong sample → review 100 % batch |
| Major | Sai ở biển ít rủi ro hơn hoặc lỗi scope: bỏ sót / sai class biển `danger`, `informative`, `supplementary`; vẽ box cho bảng dự án/địa danh/quảng cáo; relevance `unknown` thiếu `needs_review`; còn `__undefined__` | Vẽ box cho bảng "công trường đang thi công"; `danger_road` thay vì `danger_construction`; quên biển phụ | Rework object |
| Minor | Geometry ngoài tolerance nhưng đúng object và attribute; box gồm một phần cột | Box lệch 5 px ở biển 20 px; box gồm cả biển phụ | Sửa khi rework cùng ảnh; không chặn batch nếu dưới ngưỡng |
| Question | Rule không đủ để phân xử (guideline gap), không tính lỗi annotator | Biển bến xe buýt có trong scope không? | Chuyển spec owner, xử lý theo mục "guideline gap" |

## Metrics

| Metric | Cách tính | Vì sao phù hợp với bài toán |
|---|---|---|
| Object recall (in-scope) | box đúng / số biển trong scope reviewer đếm được trên ảnh review | Bỏ sót biển là lỗi nguy hiểm nhất cho ISA |
| Precision scope | box đúng scope / tổng box annotator vẽ | Bắt lỗi vẽ biển chỉ đường, mặt sau, quảng cáo |
| Family accuracy | box đúng `sign_family` / box đúng scope | Tầng taxonomy downstream lọc theo |
| Class accuracy (readable) | box đúng `sign_class` / box mà reviewer đọc được class | Không phạt `unknown` hợp lệ, chỉ đo class đọc được |
| Unknown misuse | box `unknown` mà reviewer đọc được rõ + box có class mà reviewer thấy không đọc được | Bắt cả "lười" lẫn "đoán" |
| Relevance accuracy | box đúng `relevant_to_ego` / box prohibitory+mandatory | Relevance chỉ quan trọng ở biển điều khiển xe |
| Geometry pass rate | box trong tolerance mục 3 / box đúng scope | Tolerance đã viết trong guideline |

Metric high-risk tách riêng: **critical escape rate** = số lỗi critical mà reviewer tìm thấy ở vòng QA thứ hai (audit
10 % ảnh đã PASS) / số ảnh audit. Mục tiêu 0; ≥ 1 escape → mở lại batch đó và rà lại sample plan.

## Quality gate

```text
PASS if:
  critical defects in sample = 0
  AND object recall >= 98 %
  AND precision scope >= 97 %
  AND family accuracy >= 97 %
  AND class accuracy (readable) >= 95 %
  AND relevance accuracy >= 95 %
  AND geometry pass rate >= 90 %
  AND no attribute left __undefined__
REWORK if: không có critical nhưng một metric dưới ngưỡng PASS và >= ngưỡng REJECT → annotator sửa các ảnh lỗi + reviewer review lại 100 % lát rủi ro
REJECT / ESCALATE if: critical defects >= 2 trong sample, HOẶC object recall < 90 %, HOẶC class accuracy < 85 % → trả cả batch, annotator re-label sau coaching; lỗi dồn vào cùng một rule → escalate guideline gap cho spec owner
```

Trade-off: ngưỡng critical = 0 và recall 98 % đắt (review 100 % lát prohibitory/mandatory) nhưng lỗi ở lát
này có hậu quả trực tiếp cho xe; bù lại, geometry chỉ yêu cầu 90 % và lỗi minor không chặn batch vì model detection
chịu được lệch vài px, còn thời gian vẽ lại box chính xác từng px rất tốn. Class accuracy 95 % (thấp hơn family 97 %)
vì biển xa 12–25 px (38 % box của dataset cao < 20 px) đọc class khó; guideline cho phép `unknown` nên không cần ép cao hơn và tránh khuyến khích đoán.

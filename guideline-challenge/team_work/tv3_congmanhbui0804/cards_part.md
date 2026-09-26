# Edge-case cards — Thành viên 3 — congmanhbui0804

Copy khối dưới, điền hết chữ TODO. Không đổi dòng `CASE ID:`.

---

CASE ID: TV3-1
Sample: VN16
Scene: Giao lộ có dải phân cách và đèn tín hiệu giao thông, phía xa có dầm cầu vượt bắc ngang làn ego; ảnh có 4 biển đều nhỏ/xa/mờ, hai trong số đó (735.84-760.57;469.50-485.60 và 849.89-860.27;484.86-496.95) rất dễ đoán sai nhóm biển nếu không zoom kỹ.
Observation: Biển tại (849.89-860.27;484.86-496.95) ban đầu bị gán `sign_family=informative`, nhưng khi zoom 400% và kiểm màu pixel thì viền lại là màu đỏ, dạng tròn — đúng đặc điểm nhóm `prohibitory` ("tròn, viền đỏ") chứ không phải hình vuông/chữ nhật xanh của `informative`. Biển tại (735.84-760.57;469.50-485.60) gắn trên cột ngay cạnh đèn tín hiệu, nền xanh dương, còn thấy dạng mũi tên/chữ mờ phía trong nhưng không đọc được nội dung.
Decision: LABEL (cả hai)
Expected: (849.89-860.27;484.86-496.95): `sign_family=prohibitory; sign_class=unknown; relevant_to_ego=yes` — không phải `informative`. (735.84-760.57;469.50-485.60): `sign_family=informative; sign_class=unknown; relevant_to_ego=yes` — vuông/chữ nhật xanh có ký hiệu, không phải bảng tên địa danh nên không IGNORE theo mục 5.
Rationale: gắn với downstream contract ở `project/01_problem_statement.md` mục Output annotation (`sign_family` "luôn gán được khi thấy hình dạng"); guideline mục 4 (bảng nhận biết theo hình dạng + màu) và mục 6.1 mức B (hình dạng/màu rõ, ký hiệu không đọc được -> class=unknown).
Common mistake: Đoán `sign_family` theo cảm giác vị trí/ngữ cảnh (gần đèn tín hiệu, gần biển chỉ dẫn khác) thay vì đọc đúng hình dạng + màu viền sau khi zoom; dễ lẫn biển cấm tròn mờ với biển informative nếu không kiểm màu viền kỹ.
Diversity: occlusion, small_far, ambiguity, conflict (giữa 2 gán ban đầu và giá trị đúng)

---

CASE ID: TV3-2
Sample: VN08
Scene: Vỉa hè bên trái đường, có người ngồi cạnh gốc cây, phía xa là làn xe và dải phân cách; đây là ảnh calibration để chốt phạm vi cho biển/bảng liên quan đến xe buýt.
Observation: Trụ tại khoảng (300-380;55-210) mang 2 tấm bảng ghép chồng: tấm trên nền sáng có nhiều dòng chữ nhỏ + một ô màu xanh nhỏ (giống khung quảng cáo/tiêu đề), tấm dưới nền xanh dương đậm có nhiều dòng chữ vàng/trắng (giống bảng số hiệu tuyến / giờ chạy) — không phải một pictogram đơn giản.
Decision: IGNORE
Expected: Không vẽ box `traffic_sign` cho cụm bảng này. Đây là bảng thông tin/lộ trình nhà chờ xe buýt (nhiều dòng chữ, có phần giống bảng quảng cáo), khác với biển `informative/informative_other` mẫu "bến xe buýt" mà guideline mô tả — biển đó là hình vuông xanh chỉ có một icon đơn, còn bảng này là bảng thông tin nhiều nội dung.
Rationale: gắn với downstream contract ở `project/01_problem_statement.md` mục Output annotation, kết hợp guideline mục 5 "Bảng thông tin dự án... -> IGNORE (không phải biển QCVN, dù có hình biển nhỏ in bên trong)" và mục 4 (chỉ liệt kê `informative_other` là pictogram đơn, không phải bảng nhiều dòng chữ).
Common mistake: Thấy icon/chữ liên quan xe buýt rồi LABEL cả cụm bảng là `informative/informative_other`, trong khi bảng thực chất là bảng thông tin/lộ trình nhiều dòng chữ chứ không phải biển pictogram QCVN.
Diversity: ambiguity, conflict (ranh giới giữa biển QCVN dạng pictogram và bảng thông tin công cộng), calibration

---

## Câu hỏi cho nhóm trưởng

1. VN08 (calibration): tấm bảng dưới nền xanh dương ở trụ (300-380;55-210) có bố cục giống bảng lộ trình xe buýt hơn là biển pictogram QCVN đơn — guideline mục 4 chỉ liệt kê `informative_other` là loại pictogram đơn (bến xe buýt/chợ...). Xác nhận giúp: những bảng lộ trình/giờ chạy kiểu này có nằm trong scope không, hay quy tắc IGNORE ở mục 5 (bảng thông tin dù có hình biển nhỏ bên trong) áp dụng cho cả trường hợp này?

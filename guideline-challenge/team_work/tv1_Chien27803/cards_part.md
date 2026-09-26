# Edge-case cards — Thành viên 1 — Chien27803

Copy khối dưới, điền hết chữ TODO. Không đổi dòng `CASE ID:`.

---

CASE ID: TV1-1
Sample: VN12
Scene: Đường đô thị cạnh cầu vượt, ban ngày; ego đi thẳng sát dải cây bên phải, gầm cầu vượt ở bên trái
Observation: Cột sọc đỏ-trắng trên dải cây bên phải có biển tròn viền đỏ lớn (≈ 1162–1253, 61–143) với một mũi tên hình chữ U bị gạch chéo; dưới gầm cầu bên trái xa có biển tròn đỏ vạch trắng rất nhỏ (≈ 570–578, 232–249, cao ~18 px); một biển xanh ở cột trái dưới gầm cầu chỉ thấy từ cạnh
Decision: LABEL 2 biển; IGNORE biển xanh nhìn từ cạnh
Expected: Biển lớn: `prohibitory / no_u_turn / relevant_to_ego=yes`, box ôm vành đỏ không gồm cột sọc. Biển nhỏ: `prohibitory / no_entry`, box ~18 px. Không có box trên biển xanh chỉ thấy cạnh
Rationale: Cấm quay đầu áp dụng cho làn ego (lề phải, quay mặt về camera) — bỏ sót hoặc gán sai class/relevance thì hệ thống cho phép quay đầu trái luật (downstream contract mục 3a). Biển nhỏ ≥ 12 px nên vẫn phải có box để detector học biển xa
Common mistake: Chọn `no_u_and_left_turn` vì mũi tên chữ U bắt đầu bằng đoạn rẽ trái — biển này chỉ có **một** mũi tên chữ U, không có mũi tên rẽ trái riêng; bỏ sót biển nhỏ dưới gầm cầu vì quá xa
Diversity: critical / small_far

---

CASE ID: TV1-2
Sample: VN15
Scene: Quốc lộ ngoại ô, ban ngày, lề phải dày đặc bảng quán ăn, bảng "BÁN ĐẤT", tờ rơi dán cột
Observation: Lề phải có tấm chữ nhật trắng chữ "ZONE" (≈ 931–1020, 97–247), bên trong là biển tròn nền xanh viền đỏ gạch chéo X (cấm dừng và đỗ), toàn tấm có các vạch chéo đen ở góc trên phải
Decision: LABEL (1 box cả tấm); IGNORE mọi bảng quảng cáo xung quanh
Expected: 1 box ôm **cả tấm ZONE**, `prohibitory / end_of_prohibition / relevant_to_ego=yes`. Không có box trên bảng "BÁN ĐẤT 700", "QUÁN NHẬU ÁNH THU", tờ rơi trên cột
Rationale: Vạch chéo đen nghĩa là **hết** khu vực cấm dừng đỗ; gán `no_stopping_parking` sẽ làm downstream cấm dừng đỗ ở đoạn đường đã hết cấm (hiểu ngược biển). Quảng cáo không phải biển QCVN, vẽ vào làm tăng false positive
Common mistake: Chỉ vẽ box quanh biển tròn bên trong và gán `no_stopping_parking`; vẽ box cho bảng "BÁN ĐẤT" vì có chữ đỏ, nền vàng giống biển
Diversity: ambiguity / conflict (biển khu vực giữa nhiều bảng quảng cáo)

---

## Câu hỏi cho nhóm trưởng

- VN12: biển tròn đỏ nhỏ dưới gầm cầu bên trái — đã gán `relevant_to_ego=yes`; theo mục 7 guideline có nên là `unknown` + `needs_review` không?
  - **Nhóm trưởng trả lời:** vị trí dưới gầm cầu bên trái không đủ để chốt; gold d3 chỉ chấm family/class, không chấm relevance.

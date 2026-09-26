# Edge-case cards — Thành viên 4 — Yuh5124

Copy khối dưới, điền hết chữ TODO. Không đổi dòng `CASE ID:`.

---

CASE ID: TV4-1
Sample: VN14
Scene: Đường ngoại ô 4 làn có dải phân cách; chiều của ego bị chặn bằng rào công trường ngang đường; nắng gắt ban ngày.
Observation: Đầu dải phân cách bên trái: cột có cấm đi ngược chiều (≈556–587;161–191) trên và tròn xanh mũi tên chéo xuống phải (≈558–589;192–221) dưới. Rào giữa đường: tam giác vàng hai vạch đứng (≈929–975;319–361); tròn xanh mũi tên ngang chỉ sang trái (≈970–1021;323–375) bị cọc rào che một phần nhỏ; tam giác vàng chữ ĐI CHẬM (≈1007–1058;327–372). Rào làn phải: tròn trắng viền đỏ trống (≈1357–1452;368–438) có dây rào vắt qua; tam giác vàng người xúc đất (≈1463–1562;387–457). Vật dễ nhầm: rào sắt; dây đỏ-trắng; cọc tiêu; tấm tối nhỏ ở lề trái xa (mặt sau biển); bảng tím thấp nhỏ ở lề phải xa.
Decision: LABEL 7 biển (kể cả 5 biển tạm trên rào); IGNORE rào / dây / cọc / mặt sau biển / bảng tím.
Expected: road_closed (prohibitory) / keep_left (mandatory) / no_entry (prohibitory) / keep_right (mandatory) / danger_road / danger_slow / danger_construction (danger); cả 7 đều relevant_to_ego=yes và needs_review=false; box đường cấm ôm trọn vòng tròn gồm viền đỏ và không gồm khung rào.
Rationale: Failure (a) trong `project/01_problem_statement.md`: bỏ sót hoặc gán relevance sai cho đường cấm / cấm đi ngược chiều / hiệu lệnh đi vòng làm xe đi vào đường cấm hoặc sai hướng quanh chướng ngại. Hai biển ở đầu dải phân cách là yes theo mục 7(b); biển trên rào chắn đường ego là yes theo mục 7(d).
Common mistake: Bỏ qua biển tạm vì gắn trên rào không có cột (mistake 4); gán road_closed thành no_entry (mistake 6); nhìn nhầm hướng mũi tên nên đổi keep_left và keep_right (mistake 5); gán cấm ngược chiều ở dải phân cách là no hoặc unknown vì biển nằm bên trái; box đường cấm dính cả khung rào.
Diversity: critical / conflict (keep_left trên rào và keep_right ở dải phân cách trong cùng ảnh) / edge (biển tạm công trường)
---

CASE ID: TV4-2
Sample: VN11
Scene: Phố thương mại đông xe máy, ban ngày; lề phải có một cột biển trước lối lên cầu, mặt tiền cửa hàng phía sau có chữ và hình trang trí
Observation: Cột lề phải có 3 tấm từ trên xuống: tròn viền đỏ "13 t" (≈ 1210–1300, 165–258); tròn viền đỏ có hai ô tô, vạch chéo đỏ và "30 m" (≈ 1220–1310, 258–360); tấm chữ nhật xanh "CẦU KIỆU — DÀI 38.9 m — RỘNG 15.2 m" (≈ 1238–1312, 355–425). Mặt tiền cửa hàng có hình thoi vàng trang trí và băng rôn xanh bên trái
Decision: LABEL 2 biển tròn; IGNORE tấm tên cầu, hình trang trí, băng rôn
Expected: `prohibitory / weight_limit / relevant_to_ego=yes` cho tấm "13 t"; `prohibitory / min_distance / relevant_to_ego=yes` cho tấm "30 m" hai ô tô. Không có box trên tấm tên cầu (không phải biển phụ vì không giải thích biển chính), hình thoi trang trí trên cửa hàng, băng rôn tuyên truyền
Rationale: Tải trọng và cự ly tối thiểu là giới hạn cho xe ego trước khi lên cầu (failure b trong `project/01_problem_statement.md`: sai giá trị tải trọng → xe quá tải lên cầu). Tấm tên cầu có số mét dễ bị đọc nhầm thành biển phụ hoặc `height_limit`, làm downstream hiểu sai giới hạn
Common mistake: Gán biển hai ô tô + "30 m" thành `no_overtaking` (biển cấm vượt không có số mét); vẽ tấm tên cầu thành `supplementary_plate` hoặc `informative_other`; gộp 3 tấm vào 1 box; đọc "38.9 m" trên tấm tên cầu thành `height_limit`
Diversity: conflict / ambiguity (biển có số mét: cự ly tối thiểu vs cấm vượt vs tên cầu)
---

## Câu hỏi cho nhóm trưởng

1. VN14 — tấm tối lề trái xa và bảng tím thấp lề phải xa (~13–14 px): gold d9 chấm "không box" hoặc "box +
   needs_review=true" (mức D mục 6.1 v1.1) đều đúng; box không tick needs_review là sai. Nhóm trưởng xác nhận cách chấm.
2. VN14 — dây rào vắt ngang mặt biển đường cấm: gold d10 coi dây mảnh không phải "bị che" nên box ôm trọn vòng tròn.
   Guideline v2 có nên ghi rõ "dây/cọc mảnh vắt qua không tính là che" không?

**Nhóm trưởng trả lời:** (1) Đồng ý cách chấm d9: không box, hoặc box + `needs_review=true` đều đúng. (2) Đã thêm vào
guideline v1.2 mục 3: dây rào, cọc, cành mảnh vắt qua không tính là bị che.

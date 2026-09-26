# Revision log

Guideline v1 = bản nháp đầu; v2 = sau calibration nội bộ; v3 = sau blind handoff. Mỗi lần tăng `Version` trong
`02_guideline.md`, thêm một hoặc nhiều dòng vào bảng: đổi gì và vì sao, kèm bằng chứng (sample_id, dòng
calibration report, câu hỏi trong clarification log, feedback của peer).

Cột Version ghi dạng `v1`, `v2`, `v3` — `make status` tìm dòng bảng có `v2` và dòng có `v3`.

| Version | Đổi gì | Vì sao | Bằng chứng |
|---|---|---|---|
| v1 | Bản nháp đầu cho biển báo Việt Nam (QCVN 41): scope biển mặt trước ≥ 12 px gồm biển tạm công trường; taxonomy 2 tầng 5 nhóm → 45 class (tốc độ tách theo giá trị, `*_other`, `unknown`); rule 1 box cho biển làn và tấm ZONE; `relevant_to_ego` yes/no/unknown; bảng IGNORE (bảng địa danh, bảng dự án, quảng cáo, mặt sau); 4 ví dụ. Thay bản nháp GTSDB (biển Đức) trước khi calibration vì nhóm đổi sang dataset Kaggle VN được Lab Coach cho phép | Downstream là hỗ trợ lái trên đường Việt Nam; biển Đức không phản ánh biển làn, biển tạm công trường, mật độ quảng cáo của đường VN | `01_problem_statement.md`; ví dụ VN01–VN04 |
| v1.1 | Thêm mục 0 "Quy ước trái/phải": trái/phải luôn theo góc nhìn camera ego; class có hướng quyết định bằng đầu mũi tên trên ảnh, không theo vị trí biển; không thêm attribute vị trí (box đã chứa vị trí). Thêm mục 6.1 "Biển quá xa/quá mờ": 4 mức A/B/C/D sau khi zoom 200–400 % — C = biết là biển nhưng không thấy hình/màu → `sign_family=unknown`, `sign_class=unknown`, vẫn vẽ box; D = không chắc là biển → vẽ + `needs_review`; ngưỡng 12 px áp dụng trước. Thêm 3 common mistake | Nhóm trưởng rà v1 trước calibration: v1 chưa nói biển chỉ biết "là biển" thì gán gì, và dùng "lề trái/phải", "mũi tên trái" mà không định nghĩa trái/phải theo góc nhìn nào | Rà soát nội bộ của nhóm trưởng (toilatrung), trước khi có export calibration |

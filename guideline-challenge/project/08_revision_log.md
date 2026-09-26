# Revision log

Guideline v1 = bản nháp đầu; v2 = sau calibration nội bộ; v3 = sau blind handoff. Mỗi lần tăng `Version` trong
`02_guideline.md`, thêm một hoặc nhiều dòng vào bảng: đổi gì và vì sao, kèm bằng chứng (sample_id, dòng
calibration report, câu hỏi trong clarification log, feedback của peer).

Cột Version ghi dạng `v1`, `v2`, `v3` — `make status` tìm dòng bảng có `v2` và dòng có `v3`.

| Version | Đổi gì | Vì sao | Bằng chứng |
|---|---|---|---|
| v1 | Bản nháp đầu cho biển báo Việt Nam (QCVN 41): scope biển mặt trước ≥ 12 px gồm biển tạm công trường; taxonomy 2 tầng 5 nhóm → 45 class (tốc độ tách theo giá trị, `*_other`, `unknown`); rule 1 box cho biển làn và tấm ZONE; `relevant_to_ego` yes/no/unknown; bảng IGNORE (bảng địa danh, bảng dự án, quảng cáo, mặt sau); 4 ví dụ. Thay bản nháp GTSDB (biển Đức) trước khi calibration vì nhóm đổi sang dataset Kaggle VN được Lab Coach cho phép | Downstream là hỗ trợ lái trên đường Việt Nam; biển Đức không phản ánh biển làn, biển tạm công trường, mật độ quảng cáo của đường VN | `01_problem_statement.md`; ví dụ VN01–VN04 |

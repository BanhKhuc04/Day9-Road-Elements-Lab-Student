# Revision log

Guideline v1 = bản nháp đầu; v2 = sau calibration nội bộ; v3 = sau blind handoff. Mỗi lần tăng `Version` trong
`02_guideline.md`, thêm một hoặc nhiều dòng vào bảng: đổi gì và vì sao, kèm bằng chứng (sample_id, dòng
calibration report, câu hỏi trong clarification log, feedback của peer).

Cột Version ghi dạng `v1`, `v2`, `v3` — `make status` tìm dòng bảng có `v2` và dòng có `v3`.

| Version | Đổi gì | Vì sao | Bằng chứng |
|---|---|---|---|
| v1 | Bản nháp đầu: scope biển luật Đức ≥ 12 px; taxonomy 2 tầng `sign_family` → `sign_class` (40 class + `*_other` + `unknown`); `relevant_to_ego` yes/no/unknown; bảng IGNORE (biển chỉ đường, mặt sau, quảng cáo, thiết bị dẫn hướng); 4 ví dụ | Chốt downstream contract (ISA / cảnh báo STOP) trước khi mở CVAT | `01_problem_statement.md`; ví dụ GTS18, GTS20, GTS05, GTS28 |

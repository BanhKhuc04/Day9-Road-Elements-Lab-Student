# Team

- **Team:** Nhóm 2
- **Nhóm peer test bài của mình:** chưa công bố — Lab Coach ghép cặp trong buổi
- **Nhóm mình test bài của:** chưa công bố — Lab Coach ghép cặp trong buổi
- **Problem family:** Traffic sign taxonomy — phân loại biển báo theo tầng (family → class) + ego relevance cho biển nhỏ / xa / bị che
- **Nguồn ảnh:** `gtsdb` (17 ảnh: 4 example · 7 calibration · 5 blind + 1 negative trong example)

| Thành viên | GitHub | Vai trò chính | File phụ trách |
|---|---|---|---|
| Trịnh Quang Trung | toilatrung | Nhóm trưởng / điều phối; spec owner; gộp gold, người duy nhất chạy `make freeze` và `make handoff` | `01`, `02`, `04_edge_cases/` (bản gộp), `08`, `team_work/` |
| Thành viên 1 | Chien27803 | CVAT owner; annotator calibration (tv1); gold GTS06 + GTS12 | `03_*`, `sample_pack.csv`, `09` |
| Thành viên 2 | BanhKhuc04 | QA owner; annotator calibration (tv2); gold GTS21 | `05`, `06_calibration_report.csv` |
| Thành viên 3 | congmanhbui0804 | Annotator calibration (tv3); gold GTS22; chấm bài peer | `07_blind_handoff/` |
| Thành viên 4 | Yuh5124 | Setup tester (chưa tham gia setup); annotator calibration (tv4); gold GTS23; ghi clarification log | mục "Setup test" trong `03_ontology_and_cvat_setup.md`, `clarification_log.csv` |

Chi tiết phân việc, thư mục ảnh của từng người và mốc thời gian: [`team_work/README.md`](../team_work/README.md).
Calibration: cả 4 thành viên label **cùng 7 ảnh** độc lập. Gold set: mỗi thành viên viết expected decision cho phần
ảnh blind của mình, nhóm trưởng gộp và đối chiếu trước khi freeze.

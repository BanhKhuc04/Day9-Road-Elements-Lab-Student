# Phân việc nhóm 2 — Traffic sign taxonomy

Nhóm trưởng / điều phối: **Trịnh Quang Trung (toilatrung)** — người duy nhất chạy `make freeze` và `make handoff`.

Thư mục này là chỗ làm việc nội bộ, **không** phải file nộp chính (file nộp nằm trong `project/`). Không gửi gì trong
thư mục này cho nhóm peer.

## Ai làm gì

| Thành viên | GitHub | Calibration (cùng 7 ảnh) | Gold set (ảnh blind riêng) | Edge-case card |
|---|---|---|---|---|
| Thành viên 1 | Chien27803 | `tv1.zip` | GTS06, GTS12 → [`tv1_Chien27803/`](tv1_Chien27803/) | TV1-1 (GTS06), TV1-2 (GTS12) |
| Thành viên 2 | BanhKhuc04 | `tv2.zip` | GTS21 → [`tv2_BanhKhuc04/`](tv2_BanhKhuc04/) | TV2-1 (GTS21), TV2-2 (GTS09) |
| Thành viên 3 | congmanhbui0804 | `tv3.zip` | GTS22 → [`tv3_congmanhbui0804/`](tv3_congmanhbui0804/) | TV3-1 (GTS22), TV3-2 (GTS27) |
| Thành viên 4 | Yuh5124 | `tv4.zip` | GTS23 → [`tv4_Yuh5124/`](tv4_Yuh5124/) | TV4-1 (GTS23), TV4-2 (GTS17) |

- **Calibration** ([`calibration/README.md`](calibration/README.md)): cả 4 người label **cùng** 7 ảnh, độc lập, để đo
  bất đồng.
- **Gold set**: mỗi người viết expected decision cho ảnh blind của mình trong `gold_part.csv` và 2 card trong
  `cards_part.md`, theo README trong thư mục của mình. Tổng 5 ảnh blind, 8 card.

## Mốc thời gian

| Phút | Việc | Ai |
|---|---|---|
| 80–110 | Setup test task CVAT (ghi vào `project/03_ontology_and_cvat_setup.md`) | Yuh5124 |
| 120–140 | Label calibration, export `tvN.zip`, push | cả 4 |
| 140 | `make calib`, chọn ≥ 3 bất đồng → `06_calibration_report.csv`, guideline v2 | nhóm trưởng + BanhKhuc04 |
| 140–150 | Viết gold part + card theo guideline v2, push | cả 4 |
| 150–160 | Gộp + đối chiếu + freeze (bên dưới) | nhóm trưởng |

## Nhóm trưởng: gộp và freeze

```bash
cd guideline-challenge
git pull
python3 team_work/merge_gold.py            # kiểm: đủ ảnh, severity hợp lệ, ≥10 decision, ≥2 critical, ≥1 geometry
python3 team_work/merge_gold.py --write    # ghi project/04_edge_cases/gold_decisions.csv + edge_case_cards.md
```

Trước khi freeze, đối chiếu gold của các thành viên với `leader/gold_draft_ai.csv` — bản nháp từ lượt quét độc lập
các ảnh blind ở độ phân giải gốc (AI hỗ trợ). Chỗ nào hai bản khác nhau (thiếu biển, khác relevance, khác class) thì
mở ảnh ra xem lại và chốt; **không** chép nguyên bản nháp đè lên phần của thành viên. Sau đó `make freeze`,
`git push --follow-tags`.

Thành viên **không mở `leader/`** trước khi nộp gold part của mình — mở trước thì gold không còn là quét độc lập.

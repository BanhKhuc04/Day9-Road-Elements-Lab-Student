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

## Raw label cho CVAT

Khi tạo task (calibration, peer, review): **Labels → tab Raw** → xoá nội dung có sẵn → dán **toàn bộ** khối JSON
dưới đây → **Save** → sang tab **Constructor** kiểm có đủ `traffic_sign` (4 attribute: `sign_family`, `sign_class`,
`relevant_to_ego`, `needs_review`), `no_target_sign`, `image_escalate`.

Bản gốc là `project/03_cvat_labels.json` (khớp với bảng ontology trong `project/03_ontology_and_cvat_setup.md`).
Nếu file gốc đổi, khối dưới đây được cập nhật theo; thấy khác nhau thì dùng file gốc.

```json
[
  {
    "name": "traffic_sign",
    "color": "#E53935",
    "type": "rectangle",
    "attributes": [
      {
        "name": "sign_family",
        "mutable": false,
        "input_type": "select",
        "default_value": "__undefined__",
        "values": [
          "__undefined__",
          "danger",
          "prohibitory",
          "mandatory",
          "priority",
          "informative",
          "supplementary",
          "unknown"
        ]
      },
      {
        "name": "sign_class",
        "mutable": false,
        "input_type": "select",
        "default_value": "__undefined__",
        "values": [
          "__undefined__",
          "danger_general",
          "danger_curve",
          "danger_crossroads",
          "danger_road_works",
          "danger_pedestrians",
          "danger_children",
          "danger_other",
          "speed_limit_20",
          "speed_limit_30",
          "speed_limit_50",
          "speed_limit_60",
          "speed_limit_70",
          "speed_limit_80",
          "speed_limit_100",
          "speed_limit_120",
          "end_of_restriction",
          "no_overtaking",
          "no_entry",
          "no_vehicles",
          "no_heavy_vehicles",
          "no_parking_stopping",
          "prohibitory_other",
          "keep_right",
          "keep_left",
          "ahead_only",
          "turn_right",
          "turn_left",
          "ahead_or_turn",
          "roundabout",
          "mandatory_other",
          "stop",
          "give_way",
          "priority_road",
          "priority_next_intersection",
          "pedestrian_crossing",
          "one_way",
          "dead_end",
          "informative_other",
          "supplementary_plate",
          "unknown"
        ]
      },
      {
        "name": "relevant_to_ego",
        "mutable": false,
        "input_type": "select",
        "default_value": "__undefined__",
        "values": [
          "__undefined__",
          "yes",
          "no",
          "unknown"
        ]
      },
      {
        "name": "needs_review",
        "mutable": false,
        "input_type": "checkbox",
        "default_value": "false",
        "values": [
          "false"
        ]
      }
    ]
  },
  {
    "name": "no_target_sign",
    "color": "#43A047",
    "type": "tag",
    "attributes": []
  },
  {
    "name": "image_escalate",
    "color": "#8E24AA",
    "type": "tag",
    "attributes": []
  }
]
```

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

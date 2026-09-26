# Phân việc nhóm 2 — Biển báo giao thông Việt Nam (dataset Kaggle VN)

Nhóm trưởng / điều phối: **Trịnh Quang Trung (toilatrung)** — người duy nhất chạy `make freeze` và `make handoff`.

Thư mục này là chỗ làm việc nội bộ, **không** phải file nộp chính (file nộp nằm trong `project/`). Không gửi gì trong
thư mục này cho nhóm peer.

## Ai làm gì

| Thành viên | GitHub | Calibration (cùng 7 ảnh) | Gold set (ảnh blind riêng) | Edge-case card |
|---|---|---|---|---|
| Thành viên 1 | Chien27803 | `tv1.zip` | VN12, VN15 → [`tv1_Chien27803/`](tv1_Chien27803/) | TV1-1 (VN12), TV1-2 (VN15) |
| Thành viên 2 | BanhKhuc04 | `tv2.zip` | VN13 → [`tv2_BanhKhuc04/`](tv2_BanhKhuc04/) | TV2-1 (VN13), TV2-2 (VN06) |
| Thành viên 3 | congmanhbui0804 | `tv3.zip` | VN16 → [`tv3_congmanhbui0804/`](tv3_congmanhbui0804/) | TV3-1 (VN16), TV3-2 (VN08) |
| Thành viên 4 | Yuh5124 | `tv4.zip` | VN14 → [`tv4_Yuh5124/`](tv4_Yuh5124/) | TV4-1 (VN14), TV4-2 (VN11) |

- **Calibration** ([`calibration/README.md`](calibration/README.md)): cả 4 người label **cùng** 7 ảnh, độc lập, để đo
  bất đồng.
- **Gold set**: mỗi người viết expected decision cho ảnh blind của mình trong `gold_part.csv` và 2 card trong
  `cards_part.md`, theo README trong thư mục của mình. Tổng 5 ảnh blind, 8 card.

## Raw label cho CVAT

> ⚠️ Bản hiện tại ứng với guideline **v1.2** (52 class). Task CVAT tạo trước v1.2 hoặc tạo bằng raw label biển Đức cũ phải **tạo lại** trước khi label calibration.

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
          "prohibitory",
          "danger",
          "mandatory",
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
          "no_entry",
          "road_closed",
          "no_stopping_parking",
          "no_parking",
          "no_turn_left",
          "no_turn_right",
          "no_u_turn",
          "no_u_and_left_turn",
          "no_u_and_right_turn",
          "no_motorbike",
          "no_car",
          "no_truck",
          "no_overtaking",
          "min_distance",
          "speed_limit_30",
          "speed_limit_40",
          "speed_limit_50",
          "speed_limit_60",
          "speed_limit_70",
          "speed_limit_80",
          "speed_limit_other",
          "weight_limit",
          "height_limit",
          "end_of_prohibition",
          "prohibitory_other",
          "danger_intersection",
          "danger_road",
          "danger_pedestrian",
          "danger_construction",
          "danger_slow",
          "give_way",
          "danger_other",
          "keep_right",
          "keep_left",
          "stop",
          "ahead_only",
          "turn_left_only",
          "turn_right_only",
          "roundabout",
          "lane_vehicle_permission",
          "lane_vehicle_speed",
          "min_speed",
          "end_min_speed",
          "mandatory_other",
          "pedestrian_crossing",
          "one_way",
          "overpass_route",
          "priority_road",
          "end_priority_road",
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

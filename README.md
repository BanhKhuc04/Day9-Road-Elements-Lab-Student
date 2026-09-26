# Nhóm 2 — Phân loại biển báo giao thông Việt Nam theo tầng và xác định biển áp dụng cho xe ego — tập trung biển nhỏ/xa, biển tạm công trường và giao lộ nhiều biển

Nhóm 2 làm bài `guideline-challenge/`. Việc của từng thành viên: [`guideline-challenge/team_work/README.md`](guideline-challenge/team_work/README.md).
Ảnh calibration (cả nhóm label chung): [`guideline-challenge/team_work/calibration/`](guideline-challenge/team_work/calibration/).
Guideline (hiện **v1.2**): [`guideline-challenge/project/02_guideline.md`](guideline-challenge/project/02_guideline.md).

> ⚠️ Raw label đã đổi ở v1.2 (thêm `stop`, `give_way`, `priority_road`, `end_priority_road`, `min_speed`, `end_min_speed`, `min_distance`). Ai đã tạo task CVAT trước đó: **tạo task mới** với khối JSON dưới rồi mới label calibration.

## Raw label cho CVAT

Tạo task → **Labels** → tab **Raw** → xoá nội dung có sẵn → dán **toàn bộ** khối dưới → **Save** → tab **Constructor**
kiểm có `traffic_sign` (4 attribute), `no_target_sign`, `image_escalate`. Bản gốc:
[`guideline-challenge/project/03_cvat_labels.json`](guideline-challenge/project/03_cvat_labels.json).

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

---

# Day 9 Lab — Road Elements

Repo mẫu này chứa **hai bài lab Day 9 độc lập**. Đầu buổi Lab Coach báo lớp làm bài nào; bạn chỉ làm bài đó và để
nguyên thư mục bài kia.

| Thư mục | Bài | Tạo repo | Đọc tiếp |
|---|---|---|---|
| `mini-task/` | Gắn nhãn 4 mini-task (lane, drivable area, traffic sign, traffic light) trên CVAT, khoá bài, tự đối chiếu reference và ghi log | Mỗi người một repo | [mini-task/README.md](mini-task/README.md) |
| `guideline-challenge/` | Guideline Design Challenge: nhóm thiết kế guideline + task CVAT, freeze gold, nhóm peer label blind rồi chấm | Một repo cho cả nhóm | [guideline-challenge/README.md](guideline-challenge/README.md) |

## Bắt đầu

1. Tạo repo bài làm bằng **Use this template → Create a new repository** theo cột "Tạo repo" của bài được giao, rồi
   clone về một thư mục **không có dấu tiếng Việt và khoảng trắng** trong đường dẫn.
2. Vào thư mục của bài rồi chạy `make help`:

   ```bash
   cd mini-task            # hoặc: cd guideline-challenge
   make help
   ```

   Không có `make` (thường gặp trên Windows) thì chạy `python lab9.py --help` (máy chỉ có `python3` hoặc `py`: gõ
   `python3 lab9.py --help` / `py lab9.py --help`). Mọi lệnh `make …` và `python lab9.py …` của bài đều chạy
   **trong thư mục bài**, không chạy ở gốc repo.
3. Làm tiếp theo README của bài. Mọi file bạn tạo và nộp đều nằm trong thư mục bài đó.

Hai bài không dùng chung file nào. Nguồn và giấy phép dữ liệu ảnh: [ATTRIBUTION.txt](ATTRIBUTION.txt) — giữ nguyên
file này ở gốc repo và trong từng thư mục bài.

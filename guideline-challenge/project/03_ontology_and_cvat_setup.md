# Ontology + CVAT setup

Bảng ontology là **source of truth** cho schema CVAT: `03_cvat_labels.json` phải khớp từng dòng ở đây.

## Ontology table

| Name | Geometry | Type (class / attribute) | Allowed values | Default | Mutable? | Rationale |
|---|---|---|---|---|---|---|
| `traffic_sign` | rectangle | class | — | — | — | Một class duy nhất: mọi biển có cùng geometry rule (box ôm mặt biển) và cùng QA rule; loại biển là thuộc tính của object |
| `sign_family` | — | attribute của `traffic_sign` (select) | `__undefined__`, `danger`, `prohibitory`, `mandatory`, `priority`, `informative`, `supplementary`, `unknown` | `__undefined__` | false | Tầng 1 của taxonomy, luôn gán được từ hình dạng + màu kể cả khi biển nhỏ/xa; downstream dùng để lọc (priority/prohibitory quan trọng nhất) |
| `sign_class` | — | attribute của `traffic_sign` (select) | `__undefined__`, `danger_general`, `danger_curve`, `danger_crossroads`, `danger_road_works`, `danger_pedestrians`, `danger_children`, `danger_other`, `speed_limit_20`, `speed_limit_30`, `speed_limit_50`, `speed_limit_60`, `speed_limit_70`, `speed_limit_80`, `speed_limit_100`, `speed_limit_120`, `end_of_restriction`, `no_overtaking`, `no_entry`, `no_vehicles`, `no_heavy_vehicles`, `no_parking_stopping`, `prohibitory_other`, `keep_right`, `keep_left`, `ahead_only`, `turn_right`, `turn_left`, `ahead_or_turn`, `roundabout`, `mandatory_other`, `stop`, `give_way`, `priority_road`, `priority_next_intersection`, `pedestrian_crossing`, `one_way`, `dead_end`, `informative_other`, `supplementary_plate`, `unknown` | `__undefined__` | false | Tầng 2, chỉ gán khi đọc được; `unknown` tách "không đọc được" khỏi "chưa gán". Mỗi family có `*_other` để không ép vào class sai |
| `relevant_to_ego` | — | attribute của `traffic_sign` (select) | `__undefined__`, `yes`, `no`, `unknown` | `__undefined__` | false | Downstream chỉ hành động theo biển áp dụng cho ego; sai ở biển priority/prohibitory là lỗi critical |
| `needs_review` | — | attribute của `traffic_sign` (checkbox) | `false` (tick = true) | `false` | false | ESCALATE ở mức object, nhìn thấy được trong export |
| `no_target_sign` | tag (cả ảnh) | class kiểu tag | — | — | — | Phân biệt "đã kiểm, không có biển" với "quên label" ở ảnh negative |
| `image_escalate` | tag (cả ảnh) | class kiểu tag | — | — | — | ESCALATE cả ảnh khi không đủ bằng chứng |

IGNORE không có label riêng: rule "không vẽ" viết ở mục 5 guideline (biển chỉ đường, mặt sau biển, quảng cáo, tiêu
phản quang, đèn, biển < 12 px). Gold kiểm IGNORE bằng số box trên ảnh.

## Class hay attribute

- **Family/class là attribute, không phải class CVAT:** 40 class biển cùng geometry và QA rule; tách thành 40 label
  CVAT sẽ làm dropdown label rất dài, khó đổi khi annotator sửa phân loại (phải xoá vẽ lại), và không cho phép "biết
  family nhưng chưa biết class". Attribute 2 tầng giữ được `family=prohibitory, class=unknown` cho biển xa.
- **`relevant_to_ego` là attribute:** cùng một biển vật lý, relevance phụ thuộc ngữ cảnh ego chứ không phải loại biển.
- **Tag ảnh là label kiểu tag:** negative và escalate cả ảnh phải hiện trong export mới đo được.
- **Default gây bias:** mọi select để `__undefined__` đứng đầu và làm default — quên gán sẽ lộ ra trong export thay vì
  thành "đèn xanh im lặng". Nếu default `relevant_to_ego=yes`, annotator quên đổi sẽ tạo lỗi critical ở biển đường
  ngang; nếu default `no`, biển STOP bị bỏ qua — nên không chọn default nào có nghĩa. `needs_review` default `false`
  là chấp nhận được vì escalate là hành động chủ động; QA plan kiểm tỉ lệ `unknown` không kèm `needs_review`.

## CVAT

- **Phiên bản CVAT** (`make cvat-status`): 2.74.1 (máy toilatrung, `http://localhost:8080`)
- **Tên task calibration** (có version guideline): `signs-calib-v1-<tên>` (mỗi annotator một task trên CVAT của mình)
- **Guide của task đã dán `02_guideline.md`?** có — bản v1, dán theo bước 3 của `team_work/calibration/README.md`; đổi version thì dán lại
- **Nhóm dùng Track hay Shape, vì sao:** Shape — ảnh GTSDB là ảnh tĩnh độc lập, không có chuỗi frame.

## Setup test

Người test: Yuh5124 (Thành viên 4, không tham gia viết labels JSON/tạo task). Mở task calibration trên CVAT, không
đọc trước guideline ngoài nút **Guide**, trả lời 4 câu: label gì, dùng tool nào, gán attribute nào, khi nào escalate.

Kết quả: _chờ Yuh5124 điền sau khi mở task._

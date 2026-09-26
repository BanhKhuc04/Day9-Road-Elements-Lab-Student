# Annotation guideline — Biển báo giao thông Đức: family → class + ego relevance

**Version:** v1

<!--
v0 = chưa có bản nháp. Đổi dòng Version ở trên thành v1 khi xong bản nháp đầu, v2 sau calibration, v3 sau blind
handoff; mỗi lần tăng version ghi một dòng vào 08_revision_log.md. `make freeze` đòi v2 trở lên.
File này là thứ nhóm peer nhận nguyên văn trong blind pack và là Guide dán vào CVAT.
-->

Đọc hết một lượt (≈ 8 phút) trước khi vẽ. Mọi quyết định bạn cần đều nằm trong file này; chỗ nào không đủ thì dùng
`unknown` + `needs_review` theo mục 7, **đừng đoán**.

## 1. Objective + scope

Dữ liệu này huấn luyện hệ thống nhận biển báo cho xe (nhắc tốc độ giới hạn, cảnh báo STOP / nhường đường / cấm vào).
Với mỗi ảnh bạn phải: (1) vẽ box cho **mọi biển báo giao thông trong scope**, (2) gán nhóm (`sign_family`) và biển
cụ thể (`sign_class`), (3) cho biết biển có áp dụng cho xe mình (ego — xe gắn camera) không.

**Trong scope:** biển báo giao thông theo luật Đức nhìn thấy **mặt trước**, mặt biển cao ≥ 12 px: biển nguy hiểm,
biển cấm, biển hiệu lệnh, biển ưu tiên, biển chỉ dẫn luật (qua đường, một chiều…), biển phụ gắn dưới biển chính.

**Ngoài scope — không vẽ:** xem bảng mục 5.

## 2. Annotation unit

- Đơn vị = **một mặt biển vật lý** trên một ảnh tĩnh. Một box cho một mặt biển.
- Nhiều biển cùng một cột: mỗi mặt biển một box riêng (biển chính và biển phụ là 2 box).
- Hai biển giống nhau đặt hai bên đường (ví dụ STOP bên phải và STOP trên đảo bên trái): **2 box**, mỗi box gán
  attribute riêng.
- Ảnh đã kiểm hết mà không có biển nào trong scope: gắn tag ảnh `no_target_sign` (không vẽ box nào). Ảnh có ít nhất
  một box thì **không** gắn tag này.

## 3. Geometry rule

- Công cụ: **Draw new rectangle → label `traffic_sign` → Shape**.
- Box ôm sát **phần mặt biển nhìn thấy được**, gồm cả viền màu (viền đỏ, viền trắng ngoài). **Không** gồm cột, giá
  đỡ, biển phụ bên dưới, bóng đổ.
- Biển tam giác / tròn / bát giác: box là hình chữ nhật nhỏ nhất chứa toàn bộ biên ngoài của biển (đỉnh tam giác
  chạm cạnh trên box).
- Bị che một phần: box chỉ ôm phần nhìn thấy (không đoán phần bị che). Bị cắt ở mép ảnh: box chạy tới mép ảnh.
- Tolerance: mỗi cạnh lệch ≤ 2 px với biển cao < 30 px, ≤ 10 % chiều cao biển với biển lớn hơn. Zoom (cuộn chuột)
  khi vẽ biển nhỏ.

## 4. Taxonomy

Một class `traffic_sign` + attribute. `sign_family` luôn gán được nếu thấy hình dạng + màu; `sign_class` chỉ gán khi
**đọc được** ký hiệu / chữ số.

| `sign_family` | Nhận biết | `sign_class` cho phép |
|---|---|---|
| `danger` | Tam giác đỉnh hướng **lên**, viền đỏ, nền trắng/vàng, ký hiệu đen | `danger_general` (dấu !), `danger_curve` (khúc cua, cua kép), `danger_crossroads` (dấu + / giao lộ), `danger_road_works` (người xúc đất), `danger_pedestrians`, `danger_children`, `danger_other` (ký hiệu tam giác khác đọc được: băng tuyết, trơn, đá lở…) |
| `prohibitory` | Tròn, viền đỏ, nền trắng; hoặc tròn trắng có vạch chéo đen/xám | `speed_limit_20/30/50/60/70/80/100/120`, `end_of_restriction` (tròn trắng vạch chéo), `no_overtaking`, `no_entry` (đỏ vạch trắng ngang), `no_vehicles` (tròn trắng viền đỏ trống), `no_heavy_vehicles`, `no_parking_stopping` (nền xanh viền đỏ gạch chéo), `prohibitory_other` |
| `mandatory` | Tròn nền **xanh**, mũi tên trắng | `keep_right` (mũi tên chéo xuống phải), `keep_left` (chéo xuống trái), `ahead_only`, `turn_right`, `turn_left`, `ahead_or_turn`, `roundabout` (3 mũi tên vòng), `mandatory_other` |
| `priority` | STOP bát giác đỏ; tam giác **ngược** viền đỏ; hình thoi vàng viền trắng; tam giác đỉnh lên có **mũi tên đen dày dọc** | `stop`, `give_way`, `priority_road`, `priority_next_intersection` |
| `informative` | Vuông / chữ nhật **xanh** có ký hiệu trắng | `pedestrian_crossing` (người đi trên vạch), `one_way`, `dead_end`, `informative_other` |
| `supplementary` | Chữ nhật trắng nhỏ viền đen, gắn ngay dưới biển chính (khoảng cách, giờ, mũi tên…) | `supplementary_plate` |
| `unknown` | Chỉ dùng khi **không** xác định được cả hình dạng lẫn màu | `unknown` |

Quy tắc:

- `sign_class=unknown` khi thấy family nhưng không đọc được ký hiệu/chữ số (ví dụ tròn viền đỏ mà số bị nhoè → family
  `prohibitory`, class `unknown`). **Không đoán số tốc độ.**
- Class phải thuộc đúng family trong bảng (ví dụ `stop` luôn đi với `priority`).
- `relevant_to_ego`: xem mục 7. Mọi attribute mặc định `__undefined__`; còn `__undefined__` trong export = chưa gán
  = lỗi.
- `needs_review`: checkbox, mặc định tắt; tick khi escalate (mục 7).

## 5. Inclusion / exclusion

| Thấy gì | Quyết định |
|---|---|
| Biển luật (bảng mục 4) mặt trước, cao ≥ 12 px | **LABEL** |
| Biển phụ trắng gắn dưới biển chính | **LABEL** riêng: `supplementary` / `supplementary_plate`, `relevant_to_ego` = như biển chính |
| Biển chỉ đường / địa danh: mũi tên nền vàng, xanh hoặc trắng có tên địa điểm, số đường, ký hiệu "i", bảng hướng đi trên cao | **IGNORE** (không vẽ) |
| Mặt sau biển (chỉ thấy tấm kim loại xám, không thấy ký hiệu) | **IGNORE** |
| Biển quảng cáo, biển cửa hàng, tên phố, bảng thông báo tư nhân, gương cầu | **IGNORE** |
| Tiêu phản quang, cột kẻ sọc đỏ-trắng / xanh-trắng, bảng mũi tên đỏ-trắng ở khúc cua, rào chắn | **IGNORE** (thiết bị dẫn hướng, không phải biển) |
| Đèn giao thông | **IGNORE** |
| Biển cao < 12 px | **IGNORE** |

## 6. Visibility / occlusion

- Bị che ≤ 50 % nhưng còn đọc được ký hiệu: label bình thường, box ôm phần thấy.
- Bị che > 50 % hoặc chỉ còn thấy màu/hình: label, `sign_class=unknown`, family theo hình dạng thấy được.
- Ngược sáng / loá / tối: nếu hình dạng + ký hiệu còn nhận được thì gán bình thường; nếu chỉ còn bóng hình dạng thì
  family theo hình dạng, class `unknown`.
- Nhỏ/xa 12–20 px: thường chỉ gán được family; class chỉ gán khi đọc được thật sự sau khi zoom.
- Biển nghiêng/xoay mạnh sang bên (thấy mặt biển rất hẹp): vẫn label nếu thấy mặt trước; relevance thường `no`
  (biển quay về đường khác) — xem mục 7.

## 7. Ambiguity / escalation

**`relevant_to_ego`** — biển có điều khiển xe ego (đang đi theo hướng camera nhìn) không:

- `yes`: biển **quay mặt về camera** và đứng ở lề **phải** đường ego, trên đảo giữa / dải phân cách của chiều ego,
  treo trên làn ego, hoặc là bản lặp bên trái của cùng một biển bên phải (STOP, nhường đường, cấm vào thường đặt cả hai
  bên).
- `no`: biển rõ ràng phục vụ đường khác — quay mặt lệch hẳn sang đường ngang, đặt ở góc đường ngang mà ego không đi
  vào, hoặc ở phía chiều ngược lại.
- `unknown`: biển quay về camera nhưng đặt ở lề **trái** / góc giao lộ và **không** có bản lặp bên phải, nên không suy
  ra được nó phục vụ ego hay đường nhánh. Luôn kèm `needs_review=true`.

**Bốn quyết định và cách thể hiện trong CVAT:**

| Quyết định | Khi nào | Trong CVAT |
|---|---|---|
| LABEL | Biển trong scope, đủ bằng chứng | Box `traffic_sign` + đủ 3 attribute khác `__undefined__` |
| IGNORE | Vật trong bảng IGNORE mục 5 | Không vẽ gì |
| UNKNOWN | Thấy biển nhưng không đọc được class, hoặc không suy ra được relevance | `sign_class=unknown` và/hoặc `relevant_to_ego=unknown` |
| ESCALATE (object) | Có attribute `unknown` ở relevance, hoặc phân vân LABEL/IGNORE | Vẫn vẽ box, tick `needs_review` |
| ESCALATE (ảnh) | Cả ảnh không đủ bằng chứng (quá tối, nhoè toàn bộ) | Tag ảnh `image_escalate` |

Phân vân "đây có phải biển trong scope không" → **vẽ box**, gán theo thứ thấy được, tick `needs_review`. Reviewer
xoá box thừa dễ hơn tìm biển bị bỏ sót.

## 8. Temporal rule

Không áp dụng — task ảnh tĩnh, mỗi ảnh độc lập, dùng **Shape** (không dùng Track).

## 9. Examples

Ảnh ví dụ nằm trong `data/gtsdb/` (split example). Toạ độ (x, y) là pixel gần đúng trên ảnh 1360×800.

| sample_id | Thấy gì | Expected output | Rule áp dụng |
|---|---|---|---|
| GTS18 | Cột bên phải: tam giác cua kép phía trên, tròn "30" phía dưới; bảng trắng trên hàng rào | 2 box: `danger/danger_curve/yes` (≈ 712–780, 266–342) và `prohibitory/speed_limit_30/yes` (≈ 722–771, 340–398). Bảng trắng: IGNORE | mục 2 (mỗi mặt biển một box), mục 5 |
| GTS20 | Giao lộ: tam giác ngược + tròn xanh vòng xuyến + vuông xanh qua đường bên phải; tròn xanh mũi tên chéo trên đảo trái; bảng mũi tên vàng/trắng bên phải; mặt sau biển chỉ đường ở giữa | `priority/give_way/yes`, `mandatory/roundabout/yes`, `informative/pedestrian_crossing/yes`, `mandatory/keep_right/yes` (đảo giữa chiều ego). Hai biển xanh nhỏ phía xa bên kia giao lộ (≈ 385–402, 475–495 vuông qua đường; ≈ 603–614, 525–545 tròn mũi tên chéo trái), cao ~20 px: vẫn LABEL `informative/pedestrian_crossing` và `mandatory/keep_left`, relevance `unknown` + `needs_review`. Bảng vàng/trắng + mặt sau biển chỉ đường: IGNORE | mục 5, mục 6 (nhỏ/xa), mục 7 (đảo giữa = yes) |
| GTS05 | Góc phố: vuông xanh qua đường bên trái, tròn "30" giữa ảnh; cột bên phải chỉ thấy mặt sau tam giác + mặt sau biển tròn | `informative/pedestrian_crossing`, `prohibitory/speed_limit_30`; relevance: 2 biển ở góc đường ngang bên trái, không có bản lặp bên phải → `unknown` + `needs_review`. Mặt sau 2 biển: IGNORE | mục 5 (mặt sau), mục 7 (`unknown`) |
| GTS28 | Làng, chỉ có biển quán ăn / quảng cáo trên nhà | Không box; tag ảnh `no_target_sign` | mục 2, mục 5 |

## 10. Common mistakes

1. Box gồm cả cột hoặc biển phụ bên dưới → box chỉ ôm mặt biển; biển phụ là box riêng.
2. Đoán số tốc độ khi nhoè ("chắc là 50") → `speed_limit_*` chỉ khi đọc được, không thì `unknown`.
3. Vẽ biển chỉ đường vàng/xanh có tên địa điểm → IGNORE.
4. Vẽ mặt sau biển → IGNORE, dù thấy rõ hình tròn/tam giác.
5. Quên biển thứ hai cùng loại ở bên trái (STOP lặp hai bên) → mỗi biển một box.
6. Để `__undefined__` ở `relevant_to_ego` → luôn chọn `yes` / `no` / `unknown`.
7. Gắn `no_target_sign` cho ảnh đã có box → chỉ dùng khi ảnh không có box nào.
8. Tam giác có mũi tên đen dày dọc là `priority/priority_next_intersection`, **không** phải `danger`.

# Annotation guideline — Biển báo giao thông Việt Nam: nhóm biển → biển cụ thể + ego relevance

**Version:** v1.1

<!--
v1 = bản nháp đầu; v2 sau calibration; v3 sau blind handoff. Mỗi lần tăng version ghi một dòng vào 08_revision_log.md.
File này là thứ nhóm peer nhận nguyên văn trong blind pack và là Guide dán vào CVAT.
-->

Đọc hết một lượt (≈ 8 phút) trước khi vẽ. Chỗ nào guideline không đủ để quyết định thì dùng `unknown` +
`needs_review` theo mục 7, **đừng đoán**. Ảnh: camera hành trình trên đường Việt Nam, 1622×626.

## 0. Quy ước trái / phải (đọc trước)

Trong toàn bộ guideline, **trái / phải luôn tính theo góc nhìn của camera ego** — tức là trái/phải **trên ảnh**,
giống người lái nhìn qua kính chắn gió. Không tính theo mặt biển, không tính theo người đứng đối diện biển.

| Cụm từ | Nghĩa chính xác |
|---|---|
| **Lề phải** | Biển đứng bên phải mép phải của phần đường ego đang đi (trên ảnh: bên phải làn xe ego) |
| **Lề trái / dải phân cách bên trái** | Biển đứng bên trái phần đường ego: trên dải phân cách giữa, đảo giao thông, hoặc lề bên kia đường một chiều |
| **Treo trên làn ego** | Biển ở phía trên phần đường ego (giá long môn, dầm cầu vượt), không lệch hẳn sang bên nào |
| **Mũi tên chỉ trái / phải** (trên biển) | Hướng **đầu mũi tên trên ảnh**. Biển luôn được nhìn từ mặt trước nên không bị lật gương; đầu mũi tên chỉ sang trái ảnh = trái |

**Không có attribute riêng cho vị trí trái/phải** — vị trí đã nằm sẵn trong toạ độ box. Annotator chỉ dùng quy ước
này để (1) chọn đúng class có hướng (`keep_left`/`keep_right`, `no_turn_left`/`no_turn_right`, `turn_left_only`/
`turn_right_only`, `no_u_and_left_turn`/`no_u_and_right_turn`) và (2) quyết định `relevant_to_ego` ở mục 7.

Class có hướng được quyết định **chỉ bằng hướng đầu mũi tên**, không phụ thuộc biển đứng bên nào của đường: biển
mũi tên chỉ sang trái cắm ở lề phải vẫn là `keep_left`.

## 1. Objective + scope

Dữ liệu huấn luyện hệ thống nhận biển báo cho xe (nhắc tốc độ, cấm rẽ/quay đầu, đường cấm, biển công trường). Với
mỗi ảnh: (1) vẽ box cho **mọi biển báo trong scope**, (2) gán nhóm biển (`sign_family`) và biển cụ thể (`sign_class`),
(3) cho biết biển có áp dụng cho xe ego (xe gắn camera, đi theo hướng camera nhìn) không.

**Trong scope:** biển báo theo quy chuẩn Việt Nam (QCVN 41) nhìn thấy **mặt trước**, mặt biển cao ≥ 12 px: biển
cấm, biển nguy hiểm/cảnh báo, biển hiệu lệnh, biển chỉ dẫn luật (qua đường, một chiều, cầu vượt…), biển phụ gắn dưới
biển chính — **kể cả biển tạm** gắn trên rào/giá chắn công trường.

**Ngoài scope — không vẽ:** xem bảng mục 5.

## 2. Annotation unit

- Một box cho **một mặt biển vật lý**. Nhiều biển cùng một cột: mỗi mặt biển một box (biển chính và biển phụ là 2
  box).
- Biển làn (tấm chữ nhật xanh chia nhiều cột làn, có hình xe và/hoặc số tốc độ): **1 box cho cả tấm**, không vẽ từng
  cột.
- Biển khu vực (tấm chữ nhật trắng có chữ **ZONE** bao quanh một biển tròn): **1 box cho cả tấm**, class theo biển
  tròn bên trong (mục 4).
- Hai biển giống nhau hai bên đường: 2 box.
- Ảnh đã kiểm hết mà không có biển trong scope: tag ảnh `no_target_sign`, không vẽ box. Ảnh có box thì không gắn tag
  này.

## 3. Geometry rule

- **Draw new rectangle → label `traffic_sign` → Shape**.
- Box ôm sát **mặt biển nhìn thấy**, gồm viền màu. **Không** gồm cột, giá rào, biển phụ, bóng đổ.
- Biển tròn/tam giác: hình chữ nhật nhỏ nhất chứa toàn bộ biên ngoài.
- Bị che một phần: chỉ ôm phần thấy. Bị cắt mép ảnh: box chạy tới mép.
- Tolerance: mỗi cạnh lệch ≤ 2 px (biển cao < 30 px) hoặc ≤ 10 % chiều cao biển (biển lớn hơn). Zoom khi vẽ biển nhỏ.

## 4. Taxonomy

`sign_family` luôn gán được nếu thấy hình dạng + màu. `sign_class` chỉ gán khi **đọc được** ký hiệu/chữ số.

| `sign_family` | Nhận biết | `sign_class` cho phép |
|---|---|---|
| `prohibitory` (biển cấm) | Tròn, viền đỏ, nền trắng (hoặc nền xanh với cấm dừng/đỗ); hoặc tròn trắng có vạch chéo đen | `no_entry` (tròn đỏ, vạch trắng ngang — cấm đi ngược chiều), `road_closed` (tròn trắng viền đỏ, **trống** — đường cấm), `no_stopping_parking` (nền xanh, viền đỏ, gạch chéo X), `no_parking` (nền xanh, viền đỏ, 1 gạch), `no_turn_left`, `no_turn_right`, `no_u_turn` (một mũi tên chữ U bị gạch), `no_u_and_left_turn` / `no_u_and_right_turn` (mũi tên rẽ **và** chữ U), `no_motorbike`, `no_car`, `no_truck`, `no_overtaking`, `speed_limit_30/40/50/60/70/80`, `speed_limit_other` (số khác), `weight_limit` (số + "t"), `height_limit` (số + "m", mũi tên dọc), `end_of_prohibition` (vạch chéo đen trên biển hoặc trên tấm ZONE = hết lệnh cấm/hết khu vực), `prohibitory_other` |
| `danger` (nguy hiểm/cảnh báo) | Tam giác đỉnh lên, viền đỏ, nền vàng | `danger_intersection` (giao nhau), `danger_road` (đường cong, hẹp, dốc, trơn, gồ ghề), `danger_pedestrian` (người đi bộ, trẻ em), `danger_construction` (người xúc đất / công trường), `danger_slow` (chữ "ĐI CHẬM"), `danger_other` |
| `mandatory` (hiệu lệnh) | Tròn nền xanh, ký hiệu trắng; hoặc tấm chữ nhật xanh biển làn | `keep_right` (mũi tên chỉ xuống/sang **phải** — đi vòng bên phải), `keep_left` (mũi tên chỉ xuống/sang **trái**, chéo hoặc ngang — đi vòng bên trái), `ahead_only`, `turn_left_only`, `turn_right_only`, `roundabout`, `lane_vehicle_permission` (biển làn chỉ loại xe), `lane_vehicle_speed` (biển làn có loại xe + số tốc độ), `mandatory_other` |
| `informative` (chỉ dẫn) | Vuông/chữ nhật **xanh** có ký hiệu (không phải tên địa danh) | `pedestrian_crossing`, `one_way`, `overpass_route` (cầu vượt/hầm), `informative_other` (bến xe buýt, chợ, mũi tên hướng đi dưới biển chính…) |
| `supplementary` (biển phụ) | Tấm chữ nhật nhỏ (trắng, hoặc có hình xe/khoảng cách/giờ) gắn ngay dưới biển chính | `supplementary_plate` |
| `unknown` | Chỉ ở mức C/D mục 6.1: biết là biển nhưng không xác định được hình dạng hoặc màu | `unknown` |

Quy tắc:

- `sign_class=unknown` khi thấy nhóm biển nhưng không đọc được ký hiệu/chữ số. **Không đoán số tốc độ, số tấn, số
  mét.** Đọc được số nhưng không có trong danh sách: `speed_limit_other`.
- Class phải thuộc đúng family trong bảng.
- Mọi attribute mặc định `__undefined__`; còn `__undefined__` trong export = chưa gán = lỗi.

## 5. Inclusion / exclusion

| Thấy gì | Quyết định |
|---|---|
| Biển QCVN (bảng mục 4) mặt trước, cao ≥ 12 px — gồm biển tạm trên rào công trường | **LABEL** |
| Biển phụ gắn dưới biển chính | **LABEL** riêng `supplementary/supplementary_plate`, relevance = như biển chính |
| Bảng chỉ đường/địa danh (nền xanh lá/xanh dương có tên địa điểm, km), bảng trên giá long môn | **IGNORE** |
| Bảng thông tin dự án, bảng "CÔNG TRƯỜNG ĐANG THI CÔNG", băng rôn, bảng tuyên truyền | **IGNORE** (không phải biển QCVN, dù có hình biển nhỏ in bên trong) |
| Biển quảng cáo, biển quán, "BÁN ĐẤT", tờ rơi dán cột | **IGNORE** |
| Mặt sau biển; biển nhìn thấy từ cạnh (chỉ thấy một vệt mỏng) | **IGNORE** |
| Dây rào, cọc tiêu, barie, vạch sơn trên đường, đèn giao thông | **IGNORE** |
| Biển cao < 12 px | **IGNORE** |

## 6. Visibility / occlusion

- Bị che ≤ 50 %, còn đọc được: label bình thường, box ôm phần thấy.
- Bị che > 50 % hoặc chỉ còn thấy màu/hình: label, `sign_class=unknown`.
- Ngược sáng / chói / mờ do chuyển động: còn nhận được ký hiệu thì gán bình thường; không thì family theo hình dạng,
  class `unknown`.
- Nhỏ/xa 12–20 px: thường chỉ gán được family; class chỉ gán khi đọc được thật sự sau khi zoom.

### 6.1 Biển quá xa / quá mờ: gán đến mức nào

Trước khi quyết định, **zoom 200–400 %** (cuộn chuột trong CVAT) lên biển. Không suy từ ảnh khác hay từ "chỗ này
thường có biển gì". Sau khi zoom, xếp biển vào đúng một mức:

| Mức | Thấy được gì sau khi zoom | `sign_family` | `sign_class` | `needs_review` |
|---|---|---|---|---|
| A | Hình dạng + màu + **đọc được** ký hiệu/chữ số | theo bảng mục 4 | biển cụ thể | tắt |
| B | Hình dạng **và** màu rõ (tròn viền đỏ, tam giác vàng viền đỏ, tròn xanh, vuông xanh…) nhưng **không đọc được** ký hiệu | theo hình dạng + màu | `unknown` | tắt |
| C | Chắc chắn là **biển báo giao thông** (tấm biển gắn trên cột/giá biển, đứng cạnh đường, quay mặt về camera) nhưng **không xác định được hình dạng hoặc màu** (chỉ là một đốm mờ, ngược sáng thành bóng đen) | `unknown` | `unknown` | tắt |
| D | **Không chắc** đó là biển giao thông hay vật khác (đèn, gương, bảng quán nhỏ, tờ rơi) | — | — | vẽ box theo mức B hoặc C, **tick** `needs_review` |

Quy tắc đi kèm:

- Ngưỡng 12 px vẫn áp dụng trước mọi mức: mặt biển cao < 12 px → **IGNORE**, kể cả khi thấy rõ là biển.
- Mức C vẫn phải có box: model cần biết "ở đây có biển" dù không biết loại. Box ôm phần đốm/tấm biển thấy được.
- `relevant_to_ego` ở mức B/C vẫn gán theo **vị trí** (mục 7) — vị trí luôn nhìn thấy được kể cả khi không đọc được
  biển. Chỉ dùng `unknown` khi vị trí thật sự không cho biết (mục 7).
- Chỉ dùng `sign_family=unknown` ở mức C/D. Đã thấy tròn viền đỏ thì phải là `prohibitory`, không được để `unknown`.
- Nhiều biển xa dính nhau trên cùng một cột mà không tách được từng mặt: vẽ **1 box cho cả cụm**, mức C, tick
  `needs_review`.

## 7. Ambiguity / escalation

**`relevant_to_ego`** (xe đi bên phải đường; trái/phải theo quy ước mục 0):

- `yes`: biển quay mặt về camera và (a) ở lề **phải** đường ego, (b) trên dải phân cách / đảo giao thông ngay bên
  trái chiều đi của ego (biển ở đầu dải phân cách như cấm đi ngược chiều + đi vòng bên phải), (c) treo trên làn ego hoặc
  gắn trên dầm cầu vượt mà ego sắp chui qua, hoặc (d) trên rào chắn đặt trên chính đường ego.
- `no`: biển rõ ràng phục vụ đường khác — quay lệch hẳn sang đường ngang, ở phía chiều ngược lại bên kia dải phân cách.
- `unknown`: biển quay về camera nhưng đặt ở lề trái / góc giao lộ / dưới gầm cầu bên trái, không suy ra được nó
  phục vụ ego hay nhánh đường khác. **Luôn kèm `needs_review=true`.**

| Quyết định | Khi nào | Trong CVAT |
|---|---|---|
| LABEL | Biển trong scope, đủ bằng chứng | Box `traffic_sign` + đủ 3 attribute khác `__undefined__` |
| IGNORE | Vật trong bảng IGNORE mục 5 | Không vẽ gì |
| UNKNOWN | Không đọc được class, hoặc không suy ra được relevance | `sign_class=unknown` và/hoặc `relevant_to_ego=unknown` |
| ESCALATE (object) | Relevance `unknown`, hoặc phân vân LABEL/IGNORE | Vẫn vẽ box, tick `needs_review` |
| ESCALATE (ảnh) | Cả ảnh không đủ bằng chứng | Tag ảnh `image_escalate` |

Phân vân "có phải biển trong scope không" → **vẽ box**, gán theo thứ thấy được, tick `needs_review`.

## 8. Temporal rule

Không áp dụng — task ảnh tĩnh, dùng **Shape**, không dùng Track.

## 9. Examples

Ảnh ví dụ trong `data/vtsd/` (split example). Toạ độ (x, y) gần đúng trên ảnh 1622×626.

| sample_id | Thấy gì | Expected output | Rule áp dụng |
|---|---|---|---|
| VN01 | Cột bên phải: tròn "50" trên, tròn cấm rẽ trái dưới; dải cây bên trái: tròn cấm rẽ phải + tấm phụ hình xe tải; biển nhỏ xa ~14 px | Phải: `prohibitory/speed_limit_50/yes` (≈ 811–843, 195–226), `prohibitory/no_turn_left/yes` (≈ 804–839, 228–262). Trái: `prohibitory/no_turn_right` + `supplementary/supplementary_plate`, relevance `unknown` + `needs_review` (lề trái, không có bản lặp bên phải). Biển xa ≈ 672–686, 275–288: `prohibitory/unknown` | mục 2, mục 4 (không đoán), mục 7 |
| VN02 | Dải phân cách trái: biển làn xanh + cột có cấm dừng đỗ và biển tròn nhỏ; lề phải: biển làn có số tốc độ, cấm đỗ + vuông xanh mũi tên | Biển làn: 1 box cả tấm — `mandatory/lane_vehicle_permission` (trái) và `mandatory/lane_vehicle_speed` (phải ≈ 1021–1059, 332–393). `no_stopping_parking`, `no_parking` đọc theo hình. Vuông xanh mũi tên dưới cấm đỗ: `informative/informative_other` | mục 2 (biển làn), mục 4 |
| VN03 | Lề phải: biển vuông xanh "CHỢ – MARKET"; xa: tam giác giao nhau ~21 px; biển rất nhỏ < 12 px; bảng "BÁN TRÀ" | `informative/informative_other/yes`; tam giác xa: `danger/danger_intersection/yes`. Biển < 12 px và bảng quảng cáo: IGNORE | mục 5, mục 6 |
| VN04 | Đường ngoại ô, chỉ có bảng quán ("CẦM ĐỒ", "BÚN PHỞ CƠM") và bảng xanh địa danh nhỏ | Không box; tag ảnh `no_target_sign` | mục 2, mục 5 |

## 10. Common mistakes

1. Box gồm cả cột, giá rào hoặc biển phụ → box chỉ ôm mặt biển; biển phụ là box riêng.
2. Đoán số tốc độ/tấn/mét khi mờ → `unknown`.
3. Vẽ bảng "CÔNG TRƯỜNG ĐANG THI CÔNG", bảng dự án, bảng địa danh → IGNORE.
4. Bỏ qua biển tạm trên rào công trường vì "không cắm cột" → vẫn LABEL.
5. Nhầm `keep_left` / `keep_right`: nhìn **đầu mũi tên chỉ về phía nào** thì đi vòng phía đó.
6. Nhầm `road_closed` (tròn trắng trống) với `no_entry` (tròn đỏ vạch trắng).
7. Vẽ từng cột của biển làn → 1 box cả tấm.
8. Tấm ZONE có vạch chéo đen → `end_of_prohibition`, không phải biển cấm bên trong.
9. Để `__undefined__` ở `relevant_to_ego`; hoặc relevance `unknown` mà quên tick `needs_review`.
10. Không vẽ biển xa vì "không biết biển gì" → vẫn vẽ nếu ≥ 12 px, gán theo mức B/C mục 6.1.
11. Chọn `keep_left`/`keep_right` theo vị trí biển trên đường thay vì theo đầu mũi tên (mục 0).
12. Để `sign_family=unknown` dù đã thấy rõ hình dạng + màu → `unknown` chỉ dùng ở mức C/D.

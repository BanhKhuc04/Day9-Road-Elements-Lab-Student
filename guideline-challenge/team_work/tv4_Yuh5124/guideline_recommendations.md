# Đề xuất thay đổi guideline — góp ý của Thành viên 4 (Yuh5124)

- **Đối tượng rà soát:** `project/02_guideline.md` **v1.1** (commit `405b79a`), đối chiếu với `project/03_cvat_labels.json`
  và quy chuẩn biển báo **QCVN 41:2019/BGTVT**.
- **Người nhận:** nhóm trưởng (toilatrung) — người sửa chính `02_guideline.md`.
- **Mục đích:** gom các lỗ hổng cần sửa trước khi lên **v2** (sau calibration) và **freeze**.

> Guideline v1.1 và `03_cvat_labels.json` **khớp nhau** (không lệch tên class nào). Các mã số biển (P.xxx, R.xxx…) trong
> file này ghi theo QCVN 41:2019 từ hiểu biết của người rà soát, chưa đối chiếu lại văn bản gốc — nhóm nên tra lại
> trước khi đưa mã vào guideline.

## Tóm tắt

| Mức | Số mục | Nội dung chính |
|---|---|---|
| 🔴 Nghiêm trọng | 4 | Thiếu STOP / nhường đường / đường ưu tiên; tốc độ tối thiểu dễ nhầm tốc độ tối đa; biển tạm mâu thuẫn biển cố định; mâu thuẫn định nghĩa biển phụ |
| 🟠 Sai / chưa rõ so với QCVN | 6 | Phiên bản QCVN; lý do IGNORE biển chỉ dẫn; tấm tên cầu; biển cự ly tối thiểu; hạn chế kích thước/tải trục; cấm ô tô quay đầu |
| 🟡 Thiếu class hay gặp | 4 | Khu đông dân cư; biển ghép tốc độ nền trắng; các biển cấm hướng khác; tốc độ 90–120 |
| 🔵 Cải thiện khả dụng | 5 | Mã QCVN cho từng class; vật mảnh vắt qua biển; cách đo 12 px; ví dụ còn thiếu; căn cứ luật cho relevance |

---

## 🔴 1. Nghiêm trọng — có thể gây lỗi `critical`

### 1.1 Không có biển STOP, nhường đường, đường ưu tiên

- **Hiện trạng:** bản biển Đức có family `priority`; khi chuyển sang Việt Nam family này bị bỏ. Không có class nào cho:
  - **R.122 "Dừng lại"** — bát giác đỏ, chữ STOP.
  - **W.208 "Giao nhau với đường ưu tiên"** — tam giác **đỉnh xuống**, viền đỏ.
  - **I.401 / I.402 "Bắt đầu / hết đường ưu tiên"** — hình thoi vàng.
- **Vì sao sai:** gặp STOP, annotator không có family để chọn. Family `danger` ghi "tam giác **đỉnh lên**" nên tam giác
  ngược cũng không vào đâu được → buộc gán `unknown`. Đây đúng là failure (a) trong downstream contract (xe không dừng).
- **Đề xuất:**
  - Thêm class `stop` (family `mandatory`), `give_way` (family `danger`), `priority_road`, `end_priority_road`
    (family `informative`), kèm mô tả hình nhận biết.
  - Sửa mô tả family `danger`: "tam giác đỉnh lên — **trừ** tam giác đỉnh xuống là `give_way`".
  - Cập nhật `03_cvat_labels.json` và bảng ontology cho khớp.

### 1.2 Biển tốc độ tối thiểu (R.306) dễ bị gán thành tốc độ tối đa

- **Hiện trạng:** không có class cho biển **tròn nền xanh có số trắng** (tốc độ tối thiểu) và biển hết tốc độ tối thiểu.
- **Vì sao sai:** annotator thấy số "60" sẽ chọn `speed_limit_60` → hệ thống nhắc tốc độ hiểu ngược nghĩa. Đây là failure
  (b) trong downstream contract.
- **Đề xuất:**
  - Thêm class `min_speed` và `end_min_speed` vào family `mandatory`.
  - Thêm common mistake: *"Số trên nền **xanh** là tốc độ **tối thiểu**; số trên nền **trắng viền đỏ** là tốc độ **tối
    đa**."*

### 1.3 Không có quy tắc khi biển tạm mâu thuẫn biển cố định

- **Hiện trạng:** guideline cho LABEL biển tạm trên rào công trường (tốt), nhưng export không phân biệt biển tạm với biển
  cố định.
- **Căn cứ QCVN:** khi biển báo tạm thời có ý nghĩa khác biển cố định, người tham gia giao thông phải chấp hành biển tạm.
- **Ví dụ thật:** VN14 — `keep_left` tạm trên rào giữa đường và `keep_right` cố định ở đầu dải phân cách, cả hai đều
  `relevant_to_ego=yes`. Downstream không biết biển nào được ưu tiên.
- **Đề xuất:** thêm attribute `is_temporary` (`__undefined__` / `yes` / `no`, mặc định `__undefined__`); tối thiểu thì
  thêm một rule vào mục 7 giải thích cách xử lý.

### 1.4 Mâu thuẫn nội bộ: tấm gắn dưới biển chính là `supplementary` hay `informative_other`?

- **Hiện trạng:**
  - Mục 4, family `supplementary`: *"tấm chữ nhật nhỏ … gắn ngay dưới biển chính"*.
  - Mục 4, family `informative`: `informative_other` gồm *"mũi tên hướng đi **dưới biển chính**"* (ví dụ VN02).
- **Vì sao sai:** tấm xanh có mũi tên dưới biển cấm đỗ → hai annotator sẽ chọn hai class khác nhau. Theo QCVN, biển phụ
  (nhóm S, ví dụ S.503 "hướng tác dụng của biển") là tấm gắn dưới biển chính để giải thích biển đó.
- **Đề xuất:** chốt một rule — *"Tấm gắn ngay dưới biển chính và giải thích biển đó → luôn `supplementary`, bất kể màu
  nền."* Sửa lại ví dụ VN02 cho khớp.

---

## 🟠 2. Sai hoặc chưa rõ so với QCVN

| # | Chỗ trong guideline | Vấn đề | Đề xuất |
|---|---|---|---|
| 2.1 | Mục 1: "theo quy chuẩn Việt Nam (QCVN 41)" | Không ghi phiên bản. QCVN 41:2024/BGTVT đã có hiệu lực từ 01/01/2025 thay bản 2019; ảnh dataset chụp trước 2023 nên theo bản 2019 | Ghi rõ "QCVN 41:2019/BGTVT" và lý do |
| 2.2 | Mục 5: IGNORE "bảng chỉ đường/địa danh" | Theo QCVN, biển chỉ đường/địa danh **vẫn là biển chỉ dẫn (nhóm I)**. Loại chúng là quyết định scope, không phải vì "không phải biển QCVN" | Sửa lý do: *"ngoài scope vì downstream không dùng"* |
| 2.3 | Chưa có rule cho tấm tên cầu | VN11: tấm xanh "CẦU KIỆU — dài 38.9m — rộng 15.2m" gắn dưới biển cấm, có số mét → dễ gán `supplementary` hoặc `informative_other` | Thêm dòng vào bảng mục 5: *tấm tên cầu / tên đường → IGNORE* |
| 2.4 | `no_overtaking` | Biển tròn có **hai xe + số mét** (VN11) gần với **P.121 "cự ly tối thiểu giữa hai xe"**, không phải P.125 cấm vượt | Thêm class `min_distance`, hoặc ghi rõ biển có số mét → `prohibitory_other` |
| 2.5 | `height_limit` ("số + m, mũi tên dọc") | QCVN còn **hạn chế chiều ngang** (P.118), **chiều dài** (P.119), **tải trọng trục** (P.116) — cũng "số + m" / "số + t" → dễ nhầm với `height_limit` / `weight_limit` | Thêm class, hoặc mô tả phân biệt: mũi tên dọc = cao; ngang = rộng; hình trục xe = tải trục |
| 2.6 | `no_u_turn` | Chưa phân biệt P.124a (cấm quay đầu) và P.124b (cấm **ô tô** quay đầu, có hình ô tô) | Ghi rõ biển có hình xe bên trong thuộc `no_u_turn` hay `prohibitory_other` |

---

## 🟡 3. Thiếu class cho biển hay gặp, ảnh hưởng downstream

| # | Biển | Vì sao cần | Đề xuất |
|---|---|---|---|
| 3.1 | Bắt đầu / hết khu đông dân cư (R.420 / R.421) — tấm chữ nhật | **Đổi tốc độ tối đa** — hệ thống nhắc tốc độ rất cần | Thêm class (family `mandatory` hoặc `informative`, chốt một) |
| 3.2 | Biển ghép tốc độ theo loại xe / theo làn (P.127b/c) — tấm **chữ nhật nền trắng** chứa nhiều biển tròn | Guideline chỉ quy định "1 box cả tấm" cho biển làn nền **xanh** | Mở rộng mục 2: tấm ghép nền trắng cũng 1 box cả tấm; thêm class `speed_limit_by_vehicle` |
| 3.3 | Cấm đi thẳng, cấm rẽ cả trái lẫn phải, cấm đỗ ngày chẵn/lẻ | Hiện rơi vào `prohibitory_other` — chấp nhận được | Liệt kê trong guideline để peer không phân vân |
| 3.4 | Tốc độ 90 / 100 / 110 / 120 (quốc lộ, cao tốc) | Danh sách chỉ tới 80 | Ghi rõ các số này → `speed_limit_other` |

---

## 🔵 4. Cải thiện để dễ dùng hơn

1. **Thêm mã QCVN cho từng class** (ví dụ `road_closed` = P.101, `no_entry` = P.102, `keep_left` = R.302b): peer tự tra
   được khi phân vân; người chấm thấy taxonomy bám luật.
2. **Vật mảnh vắt qua mặt biển** (dây rào, cọc — VN14): ghi rõ *"vật mảnh vắt qua không tính là che; box vẫn ôm trọn
   biển"* để không lệch geometry.
3. **Cách đo ngưỡng 12 px trong CVAT:** mức A–D ở mục 6.1 rất tốt, nhưng mọi quyết định bắt đầu từ ngưỡng 12 px mà
   guideline chưa nói đo thế nào (ví dụ so với kích thước box vừa vẽ trong sidebar, hoặc so với một vật tham chiếu).
4. **Mục 9 còn thiếu ví dụ** cho: STOP / nhường đường; tốc độ tối thiểu; biển tạm mâu thuẫn biển cố định. Thêm từ ảnh
   split example hoặc calibration — **không** dùng ảnh blind.
5. **Dẫn căn cứ luật cho mục 7 (relevance):** QCVN quy định biển đặt **bên phải theo chiều đi**, có thể đặt bổ sung bên
   trái hoặc phía trên. Đây là lý do biển lề phải → `yes`, biển lề trái không có bản lặp → `unknown`.

---

## Thứ tự ưu tiên đề xuất

| Thời điểm | Mục | Lý do |
|---|---|---|
| **Trước freeze (lên v2)** | 1.1, 1.2, 1.4 | Có thể gây lỗi critical hoặc bất đồng lớn ở calibration/blind |
| **Nên làm cùng v2** | 1.3, 2.1, 2.2, 2.3 | Ảnh hưởng trực tiếp tới ảnh đã chọn (VN11, VN14) |
| **Để v3** | Các mục còn lại | Sửa theo bằng chứng từ blind test |

## Việc kéo theo nếu nhận đề xuất

- Sửa `project/02_guideline.md` (mục 4, 5, 7, 9, 10) và tăng `Version`.
- Sửa `project/03_cvat_labels.json` và bảng ontology trong `project/03_ontology_and_cvat_setup.md` cho khớp class /
  attribute mới.
- Ghi một dòng vào `project/08_revision_log.md` cho mỗi thay đổi, bằng chứng trỏ về file này.
- Nếu thêm attribute `is_temporary`: bổ sung decision tương ứng cho VN13 và VN14 trong gold **trước** `make freeze`.

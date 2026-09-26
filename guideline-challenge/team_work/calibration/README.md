# Calibration nội bộ — nhóm 2 (phút 120–140)

Calibration đo **bất đồng giữa các annotator trên cùng ảnh**, nên cả 4 thành viên label **cùng 7 ảnh** trong
`images/` (GTS02, GTS09, GTS11, GTS13, GTS17, GTS26, GTS27). Không chia ảnh cho từng người — chia ra thì không có gì
để so.

Làm **độc lập**: không nhìn màn hình nhau, không chốt chung cách xử lý ca mơ hồ trước khi export. Chỗ nào phân vân,
làm theo guideline mục 7 (`unknown` + `needs_review`) — chính những chỗ đó là thứ calibration cần bắt.

## Các bước (mỗi người trên CVAT máy mình)

1. `git pull` để lấy `project/02_guideline.md` và `project/03_cvat_labels.json` mới nhất (guideline **v1**).
2. CVAT → **Tasks → + → Create a new task**:
   - **Name:** `signs-calib-v1-tvN` (N = số thành viên của bạn).
   - **Labels → Raw:** xoá nội dung có sẵn, dán toàn bộ `project/03_cvat_labels.json`, **Save**. Sang **Constructor**
     kiểm: có `traffic_sign` (4 attribute), `no_target_sign`, `image_escalate`.
   - **Select files → My computer:** chọn cả 7 ảnh trong `team_work/calibration/images/`.
   - **Submit & Open**.
3. Trang task → **Edit** dưới Task description → dán toàn bộ `project/02_guideline.md` → **Submit** (nút **Guide**
   trong job sẽ mở lại được).
4. Label cả 7 ảnh theo guideline (Draw new rectangle → `traffic_sign` → Shape; gán đủ 3 attribute; tag ảnh nếu cần).
   **Ctrl+S** thường xuyên.
5. Export: **Actions → Export task dataset → CVAT for images 1.1**, **Save images: tắt**.
6. Đổi tên file đúng như bảng dưới, chép vào `project/06_calibration_exports/`, rồi
   `git add project/06_calibration_exports/tvN.zip && git commit -m "calibration tvN" && git push`.

| Thành viên | GitHub | Tên file export |
|---|---|---|
| Thành viên 1 | Chien27803 | `tv1.zip` |
| Thành viên 2 | BanhKhuc04 | `tv2.zip` |
| Thành viên 3 | congmanhbui0804 | `tv3.zip` |
| Thành viên 4 | Yuh5124 | `tv4.zip` |

Tool lấy tên file làm tên annotator, nên đặt đúng tên.

## Sau khi đủ file (nhóm trưởng chạy)

```bash
cd guideline-challenge
make calib FILES="project/06_calibration_exports/tv1.zip project/06_calibration_exports/tv2.zip project/06_calibration_exports/tv3.zip project/06_calibration_exports/tv4.zip"
```

Không có `make`: `python3 lab9.py calib project/06_calibration_exports/tv1.zip …`. Lệnh ghi
`project/06_calibration_measure.csv` và in các chỗ lệch nhiều nhất → chọn ≥ 3 chỗ ghi vào
`project/06_calibration_report.csv`, sửa guideline thành v2.

# Thành viên 4 — Yuh5124

Phần việc của bạn trong **gold set** (nhóm 2). Làm **một mình**, không xem file của người khác, không mở
`team_work/leader/`. Gửi nhóm trưởng (toilatrung) trước phút 150 để kịp freeze.

## Ảnh của bạn

`GTS23` — nằm trong `images/` của thư mục này (bản gốc ở `data/gtsdb/`). Đây là ảnh **blind**: không gửi, không
chụp cho nhóm peer.

## Việc cần làm

1. Đọc `project/02_guideline.md` (bản mới nhất) — gold phải theo **đúng rule đã viết**, không theo cảm giác.
2. Mở từng ảnh ở **kích thước gốc** (zoom 200 %), quét hết biển nhỏ / xa / bị che / ngược sáng, và cả những vật trông
   giống biển (biển chỉ đường, mặt sau biển, cột sọc, bảng quảng cáo). Gold bỏ sót một biển thì peer vẽ đúng vẫn bị
   chấm sai.
3. Điền `gold_part.csv`, mỗi dòng một decision (xem mẫu bên dưới):
   - `sample_id`: chỉ ảnh của bạn; `decision_id`: `d1`, `d2`… (không trùng trong cùng ảnh).
   - `expected`: viết sao cho người khác nhìn file export của peer là biết đúng/sai. Dạng gợi ý:
     `label=traffic_sign x2`, `sign_family=priority; sign_class=stop; relevant_to_ego=yes (STOP bên phải)`,
     `IGNORE: không có box trên biển chỉ đường vàng`, `geometry: box ôm mặt biển, không gồm cột và biển phụ`.
     **Không dùng dấu phẩy** trong `expected` và `rationale` (dùng `;`) để CSV không vỡ cột.
   - `severity`: `critical` (sai → xe không dừng / sai tốc độ / sai hướng), `major` (sai class hoặc relevance ít
     nguy hiểm, IGNORE sai), `minor` (geometry lệch, lỗi không ảnh hưởng quyết định lái).
   - `rationale`: vì sao — trỏ tới mục guideline.
   - Mỗi ảnh ≥ 2 decision; cả phần của bạn nên có ≥ 1 decision `critical` hoặc ghi rõ vì sao ảnh không có cơ hội
     critical; ≥ 1 decision `geometry:`.
4. Điền `cards_part.md`: 2 card: một card cho GTS23 (case critical), một card cho ảnh calibration GTS17 (relevance biển ở lối ra khu thương mại).
5. Thấy rule trong guideline không đủ để quyết định → **không tự chế rule**, ghi câu hỏi vào cuối `cards_part.md`
   mục "Câu hỏi cho nhóm trưởng".
6. `git pull`, commit **chỉ thư mục của bạn**, push: `git add team_work/tv4_Yuh5124 && git commit -m "gold part tv4_Yuh5124" && git push`.

## Mẫu dòng gold (ví dụ ảnh khác, không phải đáp án)

```csv
sample_id,decision_id,expected,severity,rationale
GTS18,d1,label=traffic_sign x2 (tam giác cua + tròn 30),major,mục 2: mỗi mặt biển một box
GTS18,d2,sign_family=prohibitory; sign_class=speed_limit_30; relevant_to_ego=yes,critical,sai số tốc độ làm ISA nhắc sai
GTS18,d3,IGNORE: không có box trên bảng trắng ở hàng rào,minor,mục 5: bảng thông báo tư nhân
GTS18,d4,geometry: box tròn 30 không gồm cột; cạnh lệch ≤ 10%,minor,mục 3
```

# Thành viên 3 — congmanhbui0804

Phần việc của bạn trong **gold set** (nhóm 2). Làm **một mình**, không xem file của người khác, không mở
`team_work/leader/`. Gửi nhóm trưởng (toilatrung) trước phút 150 để kịp freeze.

## Ảnh của bạn

`VN16` — nằm trong `images/` của thư mục này (bản gốc ở `data/vtsd/`). Đây là ảnh **blind**: không gửi, không
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
4. Điền `cards_part.md`: 2 card: một card cho VN16, một card cho ảnh calibration VN08 (biển bến xe buýt — có trong scope không).
5. Thấy rule trong guideline không đủ để quyết định → **không tự chế rule**, ghi câu hỏi vào cuối `cards_part.md`
   mục "Câu hỏi cho nhóm trưởng".
6. `git pull`, commit **chỉ thư mục của bạn**, push: `git add team_work/tv3_congmanhbui0804 && git commit -m "gold part tv3_congmanhbui0804" && git push`.

## Mẫu dòng gold (ví dụ ảnh khác, không phải đáp án)

```csv
sample_id,decision_id,expected,severity,rationale
VN01,d1,label=traffic_sign x2 ở cột phải (tròn 50 + cấm rẽ trái),major,mục 2: mỗi mặt biển một box
VN01,d2,sign_family=prohibitory; sign_class=speed_limit_50; relevant_to_ego=yes,critical,sai số tốc độ làm hệ thống nhắc sai
VN01,d3,IGNORE: không có box trên bảng quảng cáo,minor,mục 5
VN01,d4,geometry: box tròn 50 không gồm cột; cạnh lệch ≤ 10%,minor,mục 3
```

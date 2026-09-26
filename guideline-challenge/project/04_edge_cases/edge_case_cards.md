# Edge-case library

Tối thiểu **8 card**, khuyến nghị 10–12. Một edge case tốt là case mà hai annotator hợp lý có thể làm khác nhau nếu
guideline chưa rõ. Tám ảnh dễ có label rõ ràng không được tính là edge-case library.

Cần có đủ độ đa dạng: occlusion / truncation / small-far · ambiguous semantics · conflicting road elements · **một case
critical-risk** · **một case guideline cho phép escalation**.

File này là kho nội bộ của nhóm, **không gửi cho peer**. Card dùng ảnh example/calibration thì chép rule + ví dụ sang
`02_guideline.md` (mục 7 và 9) để peer đọc được. Card về ảnh blind chỉ nằm ở đây, và decision của nó phải có trong
`gold_decisions.csv` trước `make freeze`.

`make status` đếm số dòng `CASE ID:` đã điền (đã thay placeholder). Copy khối dưới cho mỗi case.

---

CASE ID: TV1-1
Sample: VN12
Scene: Đường đô thị cạnh cầu vượt, ban ngày; ego đi thẳng sát dải cây bên phải, gầm cầu vượt ở bên trái
Observation: Cột sọc đỏ-trắng trên dải cây bên phải có biển tròn viền đỏ lớn (≈ 1162–1253, 61–143) với một mũi tên hình chữ U bị gạch chéo; dưới gầm cầu bên trái xa có biển tròn đỏ vạch trắng rất nhỏ (≈ 570–578, 232–249, cao ~18 px); một biển xanh ở cột trái dưới gầm cầu chỉ thấy từ cạnh
Decision: LABEL 2 biển; IGNORE biển xanh nhìn từ cạnh
Expected: Biển lớn: `prohibitory / no_u_turn / relevant_to_ego=yes`, box ôm vành đỏ không gồm cột sọc. Biển nhỏ: `prohibitory / no_entry`, box ~18 px. Không có box trên biển xanh chỉ thấy cạnh
Rationale: Cấm quay đầu áp dụng cho làn ego (lề phải, quay mặt về camera) — bỏ sót hoặc gán sai class/relevance thì hệ thống cho phép quay đầu trái luật (downstream contract mục 3a). Biển nhỏ ≥ 12 px nên vẫn phải có box để detector học biển xa
Common mistake: Chọn `no_u_and_left_turn` vì mũi tên chữ U bắt đầu bằng đoạn rẽ trái — biển này chỉ có **một** mũi tên chữ U, không có mũi tên rẽ trái riêng; bỏ sót biển nhỏ dưới gầm cầu vì quá xa
Diversity: critical / small_far

---

CASE ID: TV1-2
Sample: VN15
Scene: Quốc lộ ngoại ô, ban ngày, lề phải dày đặc bảng quán ăn, bảng "BÁN ĐẤT", tờ rơi dán cột
Observation: Lề phải có tấm chữ nhật trắng chữ "ZONE" (≈ 931–1020, 97–247), bên trong là biển tròn nền xanh viền đỏ gạch chéo X (cấm dừng và đỗ), toàn tấm có các vạch chéo đen ở góc trên phải
Decision: LABEL (1 box cả tấm); IGNORE mọi bảng quảng cáo xung quanh
Expected: 1 box ôm **cả tấm ZONE**, `prohibitory / end_of_prohibition / relevant_to_ego=yes`. Không có box trên bảng "BÁN ĐẤT 700", "QUÁN NHẬU ÁNH THU", tờ rơi trên cột
Rationale: Vạch chéo đen nghĩa là **hết** khu vực cấm dừng đỗ; gán `no_stopping_parking` sẽ làm downstream cấm dừng đỗ ở đoạn đường đã hết cấm (hiểu ngược biển). Quảng cáo không phải biển QCVN, vẽ vào làm tăng false positive
Common mistake: Chỉ vẽ box quanh biển tròn bên trong và gán `no_stopping_parking`; vẽ box cho bảng "BÁN ĐẤT" vì có chữ đỏ, nền vàng giống biển
Diversity: ambiguity / conflict (biển khu vực giữa nhiều bảng quảng cáo)

---

CASE ID: TV2-1
Sample: VN13
Scene: Đường đô thị đang thi công rào chắn bên phải làn đường ego, có cụm biển tạm gắn trên rào chắn barie và bảng thông tin dự án lớn phía sau.
Observation: Rào chắn thi công lấn vào phần đường xe chạy bên phải, trên rào gắn 4 biển báo tạm QCVN (1 biển tròn xanh mũi tên đi vòng sang trái keep_left và 3 biển tam giác viền đỏ nền vàng: đường hẹp bên phải, người xúc đất công trường, chữ ĐI CHẬM). Phía trên rào có tấm biển chữ nhật màu xanh ghi "CÔNG TRƯỜNG ĐANG THI CÔNG", phía sau là pano lớn "THÔNG TIN DỰ ÁN". Phía bên trái ở cột dải phân cách/giá long môn có biển cấm đi ngược chiều và biển hiệu lệnh đi vòng bên phải.
Decision: LABEL đối với 4 biển tạm QCVN trên rào và 2 biển trên cột dải phân cách; IGNORE đối với bảng Thông tin dự án, biển "CÔNG TRƯỜNG ĐANG THI CÔNG", khung rào chắn barie và đèn xoay.
Expected: Vẽ 4 box riêng rẽ cho 4 biển tạm trên rào: Box 1 (mandatory/keep_left/yes), Box 2 (danger/danger_road/yes), Box 3 (danger/danger_construction/yes), Box 4 (danger/danger_slow/yes). Vẽ 2 box riêng ở cột bên trái: prohibitory/no_entry/yes và mandatory/keep_right/yes. Tuyệt đối không vẽ box trên bảng thông tin dự án, bảng công trường chữ nhật và thanh rào.
Rationale: Biển hiệu lệnh keep_left và các biển cảnh báo nguy hiểm trên rào chắn là các biển báo tạm thời có hiệu lực bắt buộc cho xe ego đang tiến tới chướng ngại vật; nếu bỏ sót hoặc nhầm hướng (ahead_only/keep_right) xe tự hành sẽ va chạm trực diện với rào thi công (vi phạm contract critical 3a). Ngược lại, bảng thông tin dự án và biển báo công trường ngoài chuẩn QCVN phải bị ignore để tránh làm sai lệch nhận diện của detector (vi phạm contract scope 2).
Common mistake: 1) Bỏ qua 4 biển tạm vì nghĩ gắn trên rào chắn không phải biển cắm cột chính thức; 2) Nhầm keep_left thành ahead_only hoặc keep_right; 3) Gán sai class cho 3 biển tam giác (chọn nhầm danger_crossroads hoặc danger_road_works không có trong taxonomy, hoặc nhầm danger_slow thành danger_other); 4) Vẽ trùm cả bảng "CÔNG TRƯỜNG ĐANG THI CÔNG" hoặc bảng "THÔNG TIN DỰ ÁN"; 5) Vẽ 1 box to bao toàn bộ cụm 4 biển và khung rào chắn thay vì tách 4 box riêng.
Diversity: critical / temporary / barrier / conflict

---

CASE ID: TV2-2
Sample: VN06
Scene: Ngã tư đô thị lớn gần trạm xăng COMECO, mật độ giao thông đông, có cột biển báo cấm xe tải kèm biển phụ bên phải lề đường và các biển làn/biển cấm/biển quảng cáo ở hậu cảnh phía xa.
Observation: Bên lề phải có cột biển báo gồm biển tròn viền đỏ cấm xe tải (no_truck) và biển phụ chữ nhật màu trắng ghi thông tin thời gian bên dưới (supplementary_plate). Phía xa bên trái ngã tư có biển làn xe hình chữ nhật màu xanh (lane_vehicle_permission), biển tròn cấm đỗ/dừng. Phía trên nóc nhà có biển quảng cáo lớn màu xanh lá in số điện thoại (090 7788144) và bảng tên trạm xăng COMECO.
Decision: LABEL đối với biển cấm xe tải và biển phụ trên cột bên phải (2 box riêng rẽ); LABEL biển làn và biển cấm xa nếu chiều cao >= 12 px (nếu mờ thì sign_class=unknown); IGNORE đối với bảng quảng cáo tấm lớn trên nóc nhà, bảng tên trạm xăng COMECO, các biển chữ nhật tên địa danh chỉ đường và các vật thể/biển nhỏ < 12 px.
Expected: Cột bên phải vẽ 2 box riêng biệt: Box trên là prohibitory/no_truck/yes, Box dưới là supplementary/supplementary_plate/yes. Biển làn phía xa (nếu >= 12 px) vẽ 1 box bao trọn cả tấm biển chữ nhật với mandatory/lane_vehicle_permission/yes. Không vẽ box cho bảng quảng cáo màu xanh lá, bảng tên trạm xăng COMECO và biển phụ không được gộp chung vào biển chính.
Rationale: Downstream classifier và parser cần tách rời biển chính và biển phụ để phân tích điều kiện giới hạn phương tiện (xe tải cấm theo khung giờ) theo mục 2 guideline; gộp chung làm hỏng aspect ratio và gây lỗi parser. Biển quảng cáo xanh lá dễ gây nhầm lẫn với biển chỉ dẫn luật (informative) hoặc biển làn, việc loại bỏ chính xác bảng quảng cáo bảo vệ precision của detector theo mục 5 guideline.
Common mistake: 1) Vẽ 1 box gộp chung cả biển cấm xe tải và biển phụ (hoặc vẽ ôm cả cột sắt); 2) Nhầm lẫn biển quảng cáo tấm lớn màu xanh lá trên nóc nhà hoặc bảng tên cây xăng COMECO thành biển chỉ dẫn (informative); 3) Vẽ từng cột riêng rẽ của biển làn thay vì vẽ 1 box bao cả tấm; 4) Cố đoán số hoặc chữ trên các biển nhỏ < 12 px ở xa thay vì ignore hoặc gán unknown.
Diversity: ambiguity / small_far / supplementary / scope

---

CASE ID: TV3-1
Sample: VN16
Scene: Giao lộ có dải phân cách và đèn tín hiệu giao thông, phía xa có dầm cầu vượt bắc ngang làn ego; ảnh có 4 biển đều nhỏ/xa/mờ, hai trong số đó (735.84-760.57;469.50-485.60 và 849.89-860.27;484.86-496.95) rất dễ đoán sai nhóm biển nếu không zoom kỹ.
Observation: Biển tại (849.89-860.27;484.86-496.95) ban đầu bị gán `sign_family=informative`, nhưng khi zoom 400% và kiểm màu pixel thì viền lại là màu đỏ, dạng tròn — đúng đặc điểm nhóm `prohibitory` ("tròn, viền đỏ") chứ không phải hình vuông/chữ nhật xanh của `informative`. Biển tại (735.84-760.57;469.50-485.60) gắn trên cột ngay cạnh đèn tín hiệu, nền xanh dương, còn thấy dạng mũi tên/chữ mờ phía trong nhưng không đọc được nội dung.
Decision: LABEL (cả hai)
Expected: (849.89-860.27;484.86-496.95): `sign_family=prohibitory; sign_class=unknown; relevant_to_ego=yes` — không phải `informative`. (735.84-760.57;469.50-485.60): `sign_family=informative; sign_class=unknown; relevant_to_ego=yes` — vuông/chữ nhật xanh có ký hiệu, không phải bảng tên địa danh nên không IGNORE theo mục 5.
Rationale: gắn với downstream contract ở `project/01_problem_statement.md` mục Output annotation (`sign_family` "luôn gán được khi thấy hình dạng"); guideline mục 4 (bảng nhận biết theo hình dạng + màu) và mục 6.1 mức B (hình dạng/màu rõ, ký hiệu không đọc được -> class=unknown).
Common mistake: Đoán `sign_family` theo cảm giác vị trí/ngữ cảnh (gần đèn tín hiệu, gần biển chỉ dẫn khác) thay vì đọc đúng hình dạng + màu viền sau khi zoom; dễ lẫn biển cấm tròn mờ với biển informative nếu không kiểm màu viền kỹ.
Diversity: occlusion, small_far, ambiguity, conflict (giữa 2 gán ban đầu và giá trị đúng)

---

CASE ID: TV3-2
Sample: VN08
Scene: Vỉa hè bên trái đường, có người ngồi cạnh gốc cây, phía xa là làn xe và dải phân cách; đây là ảnh calibration để chốt phạm vi cho biển/bảng liên quan đến xe buýt.
Observation: Trụ tại khoảng (300-380;55-210) mang 2 tấm bảng ghép chồng: tấm trên nền sáng có nhiều dòng chữ nhỏ + một ô màu xanh nhỏ (giống khung quảng cáo/tiêu đề), tấm dưới nền xanh dương đậm có nhiều dòng chữ vàng/trắng (giống bảng số hiệu tuyến / giờ chạy) — không phải một pictogram đơn giản.
Decision: IGNORE
Expected: Không vẽ box `traffic_sign` cho cụm bảng này. Đây là bảng thông tin/lộ trình nhà chờ xe buýt (nhiều dòng chữ, có phần giống bảng quảng cáo), khác với biển `informative/informative_other` mẫu "bến xe buýt" mà guideline mô tả — biển đó là hình vuông xanh chỉ có một icon đơn, còn bảng này là bảng thông tin nhiều nội dung.
Rationale: gắn với downstream contract ở `project/01_problem_statement.md` mục Output annotation, kết hợp guideline mục 5 "Bảng thông tin dự án... -> IGNORE (không phải biển QCVN, dù có hình biển nhỏ in bên trong)" và mục 4 (chỉ liệt kê `informative_other` là pictogram đơn, không phải bảng nhiều dòng chữ).
Common mistake: Thấy icon/chữ liên quan xe buýt rồi LABEL cả cụm bảng là `informative/informative_other`, trong khi bảng thực chất là bảng thông tin/lộ trình nhiều dòng chữ chứ không phải biển pictogram QCVN.
Diversity: ambiguity, conflict (ranh giới giữa biển QCVN dạng pictogram và bảng thông tin công cộng), calibration

---

CASE ID: TV4-1
Sample: VN14
Scene: Đường ngoại ô 4 làn có dải phân cách; chiều của ego bị chặn bằng rào công trường ngang đường; nắng gắt ban ngày.
Observation: Đầu dải phân cách bên trái: cột có cấm đi ngược chiều (≈556–587;161–191) trên và tròn xanh mũi tên chéo xuống phải (≈558–589;192–221) dưới. Rào giữa đường: tam giác vàng hai vạch đứng (≈929–975;319–361); tròn xanh mũi tên ngang chỉ sang trái (≈970–1021;323–375) bị cọc rào che một phần nhỏ; tam giác vàng chữ ĐI CHẬM (≈1007–1058;327–372). Rào làn phải: tròn trắng viền đỏ trống (≈1357–1452;368–438) có dây rào vắt qua; tam giác vàng người xúc đất (≈1463–1562;387–457). Vật dễ nhầm: rào sắt; dây đỏ-trắng; cọc tiêu; tấm tối nhỏ ở lề trái xa (mặt sau biển); bảng tím thấp nhỏ ở lề phải xa.
Decision: LABEL 7 biển (kể cả 5 biển tạm trên rào); IGNORE rào / dây / cọc / mặt sau biển / bảng tím.
Expected: road_closed (prohibitory) / keep_left (mandatory) / no_entry (prohibitory) / keep_right (mandatory) / danger_road / danger_slow / danger_construction (danger); cả 7 đều relevant_to_ego=yes và needs_review=false; box đường cấm ôm trọn vòng tròn gồm viền đỏ và không gồm khung rào.
Rationale: Failure (a) trong `project/01_problem_statement.md`: bỏ sót hoặc gán relevance sai cho đường cấm / cấm đi ngược chiều / hiệu lệnh đi vòng làm xe đi vào đường cấm hoặc sai hướng quanh chướng ngại. Hai biển ở đầu dải phân cách là yes theo mục 7(b); biển trên rào chắn đường ego là yes theo mục 7(d).
Common mistake: Bỏ qua biển tạm vì gắn trên rào không có cột (mistake 4); gán road_closed thành no_entry (mistake 6); nhìn nhầm hướng mũi tên nên đổi keep_left và keep_right (mistake 5); gán cấm ngược chiều ở dải phân cách là no hoặc unknown vì biển nằm bên trái; box đường cấm dính cả khung rào.
Diversity: critical / conflict (keep_left trên rào và keep_right ở dải phân cách trong cùng ảnh) / edge (biển tạm công trường)

---

CASE ID: TV4-2
Sample: VN11
Scene: Phố thương mại đông xe máy, ban ngày; lề phải có một cột biển trước lối lên cầu, mặt tiền cửa hàng phía sau có chữ và hình trang trí
Observation: Cột lề phải có 3 tấm từ trên xuống: tròn viền đỏ "13 t" (≈ 1210–1300, 165–258); tròn viền đỏ có hai ô tô, vạch chéo đỏ và "30 m" (≈ 1220–1310, 258–360); tấm chữ nhật xanh "CẦU KIỆU — DÀI 38.9 m — RỘNG 15.2 m" (≈ 1238–1312, 355–425). Mặt tiền cửa hàng có hình thoi vàng trang trí và băng rôn xanh bên trái
Decision: LABEL 2 biển tròn; IGNORE tấm tên cầu, hình trang trí, băng rôn
Expected: `prohibitory / weight_limit / relevant_to_ego=yes` cho tấm "13 t"; `prohibitory / min_distance / relevant_to_ego=yes` cho tấm "30 m" hai ô tô. Không có box trên tấm tên cầu (không phải biển phụ vì không giải thích biển chính), hình thoi trang trí trên cửa hàng, băng rôn tuyên truyền
Rationale: Tải trọng và cự ly tối thiểu là giới hạn cho xe ego trước khi lên cầu (failure b trong `project/01_problem_statement.md`: sai giá trị tải trọng → xe quá tải lên cầu). Tấm tên cầu có số mét dễ bị đọc nhầm thành biển phụ hoặc `height_limit`, làm downstream hiểu sai giới hạn
Common mistake: Gán biển hai ô tô + "30 m" thành `no_overtaking` (biển cấm vượt không có số mét); vẽ tấm tên cầu thành `supplementary_plate` hoặc `informative_other`; gộp 3 tấm vào 1 box; đọc "38.9 m" trên tấm tên cầu thành `height_limit`
Diversity: conflict / ambiguity (biển có số mét: cự ly tối thiểu vs cấm vượt vs tên cầu)

---

# Edge-case cards — Thành viên 2 — BanhKhuc04

Copy khối dưới, điền hết chữ TODO. Không đổi dòng `CASE ID:`.

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

## Câu hỏi cho nhóm trưởng

(không có thì để trống)

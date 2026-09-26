# Peer feedback + owner response

Phần 1 do **nhóm peer** trả lời (gửi kèm file export). Phần 2 do **nhóm owner** điền. Thay mọi placeholder mới là xong (gate G5).

- **Nhóm peer:** Nhóm 5
- **Người label blind:** Nguyễn Hoàng Nam

## 1. Peer trả lời

1. **Rule nào rõ nhất / giúp quyết định nhanh nhất?**  
   Quy ước trái/phải ở mục 0 và quy tắc biển tạm công trường ở mục 1 & 4. Việc định nghĩa rõ hướng đầu mũi tên quyết định class `keep_left`/`keep_right` (không phụ thuộc biển cắm bên nào) và quy định biển trên rào chắn ego áp dụng `relevant_to_ego=yes` giúp xử lý các ảnh rào công trường phức tạp như VN13, VN14 rất dứt khoát và tự tin, không bị nhầm lẫn giữa `keep_left` và `keep_right`.

2. **Rule nào mơ hồ hoặc phải tự suy diễn?**  
   Quy tắc phân định lề trái (mục 7 dòng 1 so với dòng 6): Ở ảnh VN16, biển cắm ở cột lề trái phía dưới gầm cầu vượt không biết nên coi là "phía chiều ngược lại bên kia dải phân cách -> `no`" hay "đường dưới gầm cầu / nhánh rẽ -> `unknown` + `needs_review`". Ngoài ra, việc xác định màu viền đỏ của biển nhỏ < 15 px ở xa cạnh cột đèn tín hiệu cũng rất dễ suy đoán nhầm sang `informative` do thiên kiến vị trí.

3. **Sample nào khiến guideline "vỡ"?**  
   Sample VN16 (dưới gầm cầu vượt): Vừa có dầm cầu vượt, vừa có nhánh đường dưới gầm và giao lộ có đèn, khiến việc xác định phạm vi áp dụng (`relevant_to_ego`) của biển bên trái và việc xác định family của biển nhỏ xa rất dễ phân vân.

4. **Attribute / default nào trong CVAT dễ gây thao tác sai?**  
   Attribute `needs_review` dạng checkbox mặc định là `false`. Khi chọn `relevant_to_ego=unknown`, người gán nhãn rất dễ quên tick `needs_review=true` vì phải thực hiện thêm một thao tác click riêng.

5. **Một thay đổi cụ thể giúp annotator mới ít hỏi hơn?**  
   Bổ sung hướng dẫn trực quan phóng to zoom 400% cho biển mờ gần đèn ở giao lộ; làm rõ ranh giới khi nào biển lề trái là `no` và khi nào là `unknown` + `needs_review` dưới gầm cầu; và ghi đậm quy tắc cấm vẽ box lồng bên trong tấm ZONE ngay ở mục 2.

## 2. Owner phân loại

Owner không tranh luận để bảo vệ guideline. Mỗi feedback và mỗi decision peer làm sai được xếp vào một hướng xử lý.

| Feedback / decision sai | Nguyên nhân (guideline gap / data ambiguity / execution error) | Xử lý (accept + revise / reject with evidence / add escalation rule) | Bằng chứng |
|---|---|---|---|
| VN16 d2: Gán `relevant_to_ego=no` thay vì `unknown` + `needs_review=true` cho biển tròn viền đỏ ở cột lề trái dưới gầm cầu | **guideline gap**: Mục 7 chưa làm rõ ranh giới giữa "chiều ngược lại có dải phân cách cứng rõ rệt" và "khu vực chân cầu vượt / gầm cầu có luồng giao thông hỗn hợp/khuất tầm nhìn" | **accept + revise**: Sửa mục 7 dòng 6 và bổ sung quy tắc: mọi biển dưới gầm cầu hoặc trên đảo lề trái khi ego chuẩn bị chui qua gầm cầu/giao lộ mà không có dải phân cách ngăn cách tuyệt đối phải gán `relevant_to_ego=unknown` và tick `needs_review=true` | Dòng VN16 d2 trong `transfer_score.csv`; câu trả lời số 2 & 3 của peer |
| VN16 d5: Gán `sign_family=informative` thay vì `prohibitory` cho biển tròn nhỏ mờ (850-860; 485-497) gần đèn tín hiệu | **execution error** (thiên kiến ngữ cảnh: gần đèn tín hiệu ngỡ là biển chỉ dẫn) kết hợp **guideline gap** (chưa có quy tắc cảnh báo cụ thể cho biển đặt cạnh cột đèn) | **accept + revise**: Bổ sung vào mục 6.1 và mục 10: "Cấm suy diễn family từ vị trí cạnh cột đèn tín hiệu; bắt buộc zoom 400% kiểm tra viền ngoài: nếu viền có pixel màu đỏ/sẫm thì bắt buộc gán `prohibitory`" | Dòng VN16 d5 trong `transfer_score.csv`; câu hỏi số 2 trong `clarification_log.csv` |
| VN15 d1: Vẽ 2 box lồng nhau trên tấm ZONE (1 box cả tấm ZONE và 1 box vẽ thêm biển tròn bên trong) | **execution error** (thói quen gán nhãn chi tiết) kết hợp **guideline gap** (chưa ghi cảnh báo cấm vẽ lồng) | **accept + revise**: Nhấn mạnh rõ ở mục 2 và mục 10 (Lỗi thường gặp 8): "1 tấm ZONE = ĐÚNG 1 BOX DUY NHẤT cho cả tấm; TUYỆT ĐỐI KHÔNG vẽ thêm box phụ cho biển tròn bên trong" | Dòng VN15 d1 trong `transfer_score.csv`; câu hỏi số 1 trong `clarification_log.csv` |
| Feedback 4: Checkbox `needs_review` dễ quên tick khi chọn `relevant_to_ego=unknown` | **data ambiguity / execution error** (giao diện CVAT tách rời dropdown và checkbox) | **add escalation rule**: Thêm bước bắt buộc trong "Quy trình mỗi ảnh" (bước 6) và QA Gate: lọc tự động trong CVAT / export mọi box có `relevant_to_ego=unknown` mà `needs_review=false` để yêu cầu sửa trước khi hoàn thành task | Câu trả lời số 4 của peer; mục Checklist trong `02_guideline.md` và Gate QA trong `05_qa_plan.md` |
| Feedback 5: Cần hướng dẫn trực quan cho giao lộ phức tạp dưới cầu vượt | **guideline gap**: Bộ ví dụ mục 9 mới chỉ có ví dụ rời rạc, chưa có ví dụ tổng hợp cho giao lộ gầm cầu vượt | **accept + revise**: Bổ sung phân tích tình huống gầm cầu vượt VN16 vào mục 9 guideline v3 và cập nhật các thẻ trường hợp khó (edge-case cards) | Câu trả lời số 5 của peer; sample VN16 |

# Quá trình hoạt động

## 26/10: Bắt đầu dự án

## Mục tiêu Tháng 1
Tuần 1: Tìm hiểu tổng quan về GA, tìm hiểu những công cụ cần thiết để áp dụng GA vào giải quyết bài toán
Tuần 2: Tiếp tục tìm hiểu về GA, thử nghiệm ý tưởng 1, đánh giá, bổ sung
Tuần 3: Hoàn thiện GUI, dùng GUI để minh họa thuật toán
Tuần 4: Sử dụng các cách crossover và selection khác để cải thiện thuật toán

### 28/10: 
- Tìm hiểu tổng quan về GA, tham khảo một số dự án đơn giản ứng dụng GA
- Đề xuất kế hoạch ban đầu:
  - ~~Build game để tạo lập môi trường~~
  - ~~Tìm hiểu những features của game và tạo ra một AI model (neural network)~~
  - ~~Train AI dùng GA~~

### 29/10: 
= Tìm hiểu về GA (tiếp tục) https://ticklabchallenge.slack.com/files/T0217SCR8HJ/F048H0X6G22
- Ý tưởng 1: 
  - Biến map thành dãy 1 chiều, bắt đầu từ ô đầu tiên bên trái, đánh số 1 ở những ô được bước lên 1 lần, 2 ở những ô bước lên 2 lần, ô bắt đầu và ô flag
  - Từ ô bắt đầu, cho máy ngẫu nhiên trừ đi 1 ở một trong những ô thỏa điều kiện:
  - Ô đó phải mang giá trị khác 0
  - Ô đó phải là ô kế cận với ô hiện tại
Kết thúc nếu không còn ô nào thỏa điều kiện

### 30/10
- Tìm hiểu về GA (tiếp tục)
- Ý tưởng 2: (áp dụng với map 6x6)
  - Cho máy chọn ngẫu nhiên các dãy có giá trị từ 1-36 (là số thứ tự bước đi) (ô 1 và ô 36 cố định, các giá trị không bị trùng lặp)
  - Objective function: với mỗi ô, +1 fitness point nếu các ô kế cận mang giá trị của ô hiện tại +-1
- Học OOP với Python
    https://ticklabchallenge.slack.com/files/T0217SCR8HJ/F048SEN3UMC

### 1/11
- Học OOP với Python (tiếp tục)

### 2/11 & 3/11
- Viết chương trình cho map level 8

### 4/11
- Hoàn thành chương trình cho map level 8 nhưng kết quả chưa khả quan https://ticklabchallenge.slack.com/files/T0217SCR8HJ/F049H1K9VQC

### 5/11
- Học một số thao tác cơ bản để làm việc với git và Github

### 6/11 
- Upload được code lên Github
- Tiếp tục tìm hiểu về GA và tìm cách tối ưu hóa ý tưởng. - Một số cách có thể dùng để tối ưu hóa ý tưởng: 
  - Partially Mapped Crossover: 
    - Chọn ngẫu nhiên 2 split point:
        [2,5 || 3,6,4 || 7,1] và [6,1 || 7,2,5 || 3,4]
trao đổi chéo [2,5 || 7,2,5 || 7,1] và [6,1 || 3,6,4 || 3,4]
    - tìm mối liên hệ giữa các gen dựa trên 2 đoạn gen trao đổi chéo: 7 <-> 3, 2 <-> 6,  5 <-> 4
hợp thức hóa phần gen không thực hiện trao đổi chéo:
[2,5 || 7,2,5 || 7,1] --> [6,4,7,2,5,3,1]
[6,1 || 3,6,4 || 3,4]  --> [2,1,3,6,4,7,5]
  - Restricted Tournament Selection (RTS): randomly choose w parents and the newly generated child will replace the most similar parent if it has the higher fitness score that that parent (mục đích là để đảm bảo tính đa dạng của các cá thể)
  - Convergence Based Gene Insertion Strategy: after an elapsed time S, the gene frequency in each chromosome from the best individuals is evaluated, if the frequency of a certain gene is higher than a parameter c, then the gene will be inserted as a fixed gene in the chromosome till the end of the evolution
- Ban đầu em dự định sẽ tìm cách tối ưu hóa ý tưởng 1 trước rồi mới thử những ý tưởng sau. Nhưng sau khi suy nghĩ lại thì em quyết định sẽ thử thêm 1 vài ý tưởng nữa, xem cái nào khả thi hơn rồi mới tìm cách tối ưu hóa nó.

### 7/11 & 8/11
- Code ý tưởng 2: gán các giá trị 1, 2, 3 ,4 (up, down, left, right) cho các gene trong chromosome (còn một số lỗi, chưa chạy được)

### 15/11 & 16/11 & 17/11
- Build UI cho game

### 19/11
- Hoàn thiện cơ bản UI
- Hoàn thiện code cho ý tưởng 2 (kết quả khả quan hơn ý tưởng 1, chạy được khoảng 40 trên 64 điểm trong 5 phút)

### 21/11
- Tích hợp được UI vào game

### 22/11 & 23/11
- Tiếp tục tìm hiểu về Genetic Algorithm để cải thiện thuật toán đã sử dụng
- Tích hợp được matplotlib vào chương trình để vẽ đồ thị trực quan

### 24/11
- Cập nhật file README.md mô tả chương trình

### 25/11
- Em thử nghiệm cách sau để đảm bảo sự đa dạng cho quần thể: sau khi generate thế hệ con thì thay vì thay tất cả con vào quần thể cũ, ta sẽ xem trong quần thể cá thể nào có chromosom giống cá thể con nhất, so sánh cá thể đó với cá thể con rồi lấy cá thể có điểm số cao hơn. Đây là đoạn code của em:
  ```Python
  def child_selection(children, pop, objective, scores):
    children_scores = [objective(n_columns, flag_pos, start, chrom, map)[0] for chrom in children]
    for k in range(len(children)):
        diff_min = len(children[k])
        selected, selected_num = [], 0
        for i in range(len(pop)):   #loop through each parent in current pop
            diff = 0
            for j in range(len(children[k])):  
                if children[k][j] != pop[i][j]:
                    diff = diff + 1
            if diff < diff_min:
                diff_min = diff
                selected, selected_num = pop[i], i
        if children_scores[k] > scores[selected_num]:
            pop[selected_num] = children[k]
  ```
- Sau khi thử nghiệm thì em thấy cách này không hiệu quả:
  - Những cá thể có điểm fitness thấp nhưng có kiểu gen khác với các cá thể con sẽ không bị thay thế
  - Việc lựa chọn ra cá thể có kiểu hình giống với cá thể con nhất trong quần thể mất nhiều thời gian

### 26/11
- Em chạy thuật toán của mình cho màn 5 thì thấy kết quả khá khả quan (đến được flag sau khoảng 500 thế hệ)

### 27/11
- Hoàn thiện gui (bố sung thêm các map khác, bổ sung những ô đi lên 3 lần)

## 28/11
- Em thử các map từ 4 đến 8 thì map 4, 5, 6 thuật toán chạy ổn, đến map 7 phức tạp hơn một chút thì nó bị stuck, có những trường hợp không thắng nhưng chỉ còn sót lại 1, 2 ô

## 29/11
- Em thử thêm map 10 và 11 thì map 10 thuật toán chạy ổn, map 11 thì giống như map 7,8 chưa đạt được global optimum
- Em thử thêm vào một bước selection sau khi crossover và một bước tăng r_mut nếu sau n thế hệ mà số điểm cao nhất vẫn không đổi, em cho chạy thử với map 11 thì nó đạt global optimum ở khoảng thế hệ từ 2000 đến 3000

## 2/12
- Khắc phục một số chỗ để chương trình chạy nhanh hơn

## 3/12
- Sửa lại hàm objective, trừ đi điểm ở những ô chưa bước lên

# 4/12
- Em chạy lại chương trình cho các màn từ 4 đến 12 (trừ màn 9) thì đều chạy được nhưng tốn khá nhiều thời gian (mỗi thế hệ của em chạy khoảng 1 phút, màn 7, 11 thường thắng sau 9000 thế hệ, màn 8, 12 thường thắng sau 40000 thế hệ hoặc hơn)

# 5/12
- Em thử nghiệm ý tưởng kéo dài chromosome ra thì thuật toán đạt global optimum nhanh hơn rất nhiều ^^. Em sẽ build lại UI và chỉnh sửa chương trình lại theo hướng này

# 6/12 & 7/12
- Viết báo cáo, bổ sung thêm một vài map, chỉnh sửa lại UI

# 10/12
- Báo cáo giữa kỳ

# 12/12
- Hoàn thiện code giai đoạn 1, cập nhật file README.md
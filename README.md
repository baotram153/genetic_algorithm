# Genetic Algorithm

## 1. Môi trường
- Em dùng map level 8 của game Reach the flag
  <img src="https://github.com/baotram153/genetic_algorithm/blob/main/RTF_level8.png" width="750" height="550">
- Về map
	- Đây là một map 6x6. Em biến cả map thành một mảng gồm 36 phần tử (mỗi phần tử là một ô lần lượt từ ô trên cùng bên trái đến ô cuối cùng bên phải). Mỗi ô lại là một mảng gồm 2 phần tử, những ô mang 2 phần tử có giá trị 0 nghĩa là ô đó có thể được bước lên 2 lần, những ô mang 1 phần tử giá trị 0 và một phần tử giá trị -1 nghĩa là ô đó có thể được bước lên một phần, những ô mang 2 phần tử -1 nghĩa là không tồn tại ô (không bước lên được)
	-  Ví dụ hàng thứ 2 của map gồm 4 ô được bước lên 1 lần, rồi 1 ô được bước lên 2 lần, rồi 1 ô  được bước lên một lần nên sẽ được setup như sau:
		- \[\[0,-1], \[0,-1], \[0,-1], \[0,-1], \[0,0], \[0,-1]]
	- Ô bắt đầu sẽ mặc định mang giá trị 1 và ô kết thúc sẽ mặc định mang giá trị 33, ta sẽ thay các giá trị 0 ở mỗi ô thành các số từ 2 đến 32 là số thứ tự bước đi
	- Ví dụ: nhân vật sẽ di chuyển từ trái sang phải nếu giá trị mỗi ô như sau:
		- \[\[3,-1], \[4,-1], \[5,-1], ...]

## 2. Các biến và hàm sử dụng trong Genetic Algorithm
- Về pop_map
	- pop_map sẽ thuận lợi cho việc tính điểm fitness của từng cá thể
- Về pop_arr
	- Để thuận tiện cho việc crossover và mutation thì em lập thêm một list chứa cá thể nhưng dưới dạng mảng 1 chiều
- Về crossover
	- Em áp dụng một cách Crossover sao cho thế hệ sau vẫn đảm bảo được tính không lặp lại của số thứ tự bước đi. Cách crossover của em như sau
		- Giả sử 2 dãy cần cross là:
			- \[2, 5, 3 || 4, 6, 1]
			- \[5, 6, 4 || 3, 1, 2]
		- Nếu trao đổi chéo như thông thường thì ta sẽ thu được 2 con như sau
			- \[2, 5, 3 || 3, 1, 2]
			- \[5, 6, 4 || 4, 6, 1] --> các dãy giá trị bị lặp lại, không thỏa điều kiện ràng buộc
		- Cách cross của em là lấy các giá trị từ đầu dãy đến điểm split point ở con 1, rồi từ con 2 lấy theo thứ tự những giá trị không trùng với con 1
			- \[2, 5, 3] + \[~~5~~, 6, 4, ~~3~~, 1,~~2~~] = \[2, 5, 3, 6, 4, 1]
			- \[5, 6, 4] +  \[2, ~~5~~, 3, ~~4~~, ~~6~~, 1] = \[5, 6, 4, 2, 3, 1]
- Về mutation
	- Cũng vì điều kiện ràng buộc nên không thể dùng mutation bằng cách thay một giá trị bằng một giá trị khác ngẫu nhiên. Nên em áp dụng mutaion bằng cách thay đổi vị trí của 2 giá trị bất kì trong dãy
		- Ví dụ:  \[2, **5**, 3, 6, **1**, 4]  -->  \[2, **1**, 3, 6, **5**, 4]
- Về cách tính fitness point
	- Với mỗi ô trong map, cộng 1 điểm fitness nếu giá trị ở các ô liền kề bằng giá trị của ô hiện tại +-1
		- Ở ví dụ sau, giả sử 2 ô \[4, 6] và \[5,-1]  nằm trên cùng một cột
			- \[...\[4,6], \[7,-1], ...
			   ...\[5,-1], ...]
		- Điểm fitness được tính như sau:
			- Ô \[4,6] đối với giá trị 4 ta cộng 1 điểm (do có giá trị 5 liền kề), đối với giá trị 6 ta cộng 2 điểm (do có giá trị 5 và 7 liền kề)
			- Ô \[7,-1] đối với giá trị 7 ta cộng 1 điểm (do có giá trị 6 liền kề), tương tự với ô \[5,-1]
- Về cách chọn các cá thể bố mẹ thì em chọn ngẫu nhiên 4 cá thể, chọn cá thể có điểm cao nhất, lặp lại n lần với n là số cá thể generate ban đầu
- Về hàm insert: Là hàm chuyển đổi từ dãy (pop_arr) sang map (pop_map)

## 3. Các thông số
- n_pop = 500 là số cá thể mỗi thế hệ
- r_cross = 0.8 là tỉ lệ crossover
- r_mut = 0.05 là tỉ lệ mutation
- n_iter = 1000 là số lần lặp lại

## 4. Các vấn đề chưa giải quyết được
- Kết quả thu được chưa khả quan. Điểm tối đa cần đạt phải là 64 (33x2-2) nhưng các lần chạy chỉ đạt được dưới 22 điểm
- Map trả về ở "Current best" có số điểm đúng nhưng map trả về ở cuối cùng lại có số điểm không đúng (em đang tìm xem lỗi ở đâu)
	- Ví dụ map trả về cuối cùng hiện số điểm là 20 nhưng điểm đúng chỉ có 4, trong khi map trả về ở "Current best" thì có số điểm đúng như số điểm đã hiện

## 5. Một số điều dự định cải thiện
- Em cảm thấy thuật toán Crossover của mình chưa tối ưu, em sẽ thử một vài cách khác
- Map level 8 chưa có sự xuất hiện của các ô trắng (các ô có thể bước lên nhiều lần)


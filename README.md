# README
- [README](#readme)
  - [Tổng quan về game Reach The Flag](#tổng-quan-về-game-reach-the-flag)
  - [Ý tưởng](#ý-tưởng)
  - [Mô tả chương trình](#mô-tả-chương-trình)
    - [Các thư viện sử dụng](#các-thư-viện-sử-dụng)
    - [Map setup](#map-setup)
    - [Objective funtion](#objective-funtion)
    - [Mutation](#mutation)
    - [Crossover](#crossover)
    - [Selection](#selection)
    - [Genetic Algorithm](#genetic-algorithm)
    - [Các biến số](#các-biến-số)
    - [Các Hyperparameter](#các-hyperparameter)
  - [Các vấn đề chưa giải quyết được](#các-vấn-đề-chưa-giải-quyết-được)

## Tổng quan về game Reach The Flag
- Luật chơi: Người chơi điều khiển nhân vật đi qua tất cả các ô trước khi đến được ô cắm cờ. 
- Các ô màu vàng sẽ rơi xuống khi nhân vật bước lên 1 lần, ô màu vàng đậm sẽ rơi xuống khi nhân vật bước lên 2 lần, ô màu xám cho phép nhân vật bước lên vô số lần
## Ý tưởng
- Em dùng map level 8 của Reach the Flag để làm môi trường chạy cho thuật toán
  <img src="https://github.com/baotram153/genetic_algorithm/blob/main/RTF_level8.png" width="750" height="550">
- Ý tưởng của em là biến map thành dãy một chiều (bắt đầu từ ô đầu tiên bên trái, lần lượt từ trái sang phải, trên xuống dưới, kết thúc ở ô cuối cùng bên phải), những ô bước lên 1 lần được đánh số 1, những ô bước lên 2 lần được đánh số 2, những ô không bước lên được đánh số -1 (sẽ giải thích ở phần mô tả chương trình)
  - Ví dụ với map phía trên, hàng thứ 4 sẽ được mã hóa [...,1,1,-1,1,1,1,...]
- Các cá thể (chromosom) là các dãy mà mỗi phần tử (gene) là các số từ 1 đến 4 (lần lượt là up, down, left, right)
  - Ví dụ: [4,1,1,3] là right $\rightarrow$ up $\rightarrow$ up $\rightarrow$ left
- Dựa vào các chromosom, ta sẽ lần lượt trừ đi 1 ở những ô đã bước lên 
- Cách tính fitness point cho mỗi cá thể: lấy số bước đi được cộng với điểm được tích lũy ở ô cờ mỗi lần bước lên ô cờ (ban đầu set điểm cho ô cờ là số âm để khuyến khích các cá thể không đến ô cờ trước), sau đó trừ đi tổng khoảng các các ô chưa bước lên đến ô cờ
  - Ví dụ: set điểm cho ô cờ là -10, cá thể đi được 15 bước và bước lên ô cờ vào 2 lần: lần thứ nhất ở bước thứ 6, lần thứ 2 ở bước thứ 13, điểm fitness của cá thể đó sẽ là: 15 + (-10+6) + (-10+13) = 14 điểm


## Mô tả chương trình
### Các thư viện sử dụng
- Numpy (sử dụng các hàm randint(), rand())
- PySimpleGUI (build UI)
- matplotlib (vẽ đồ thị)


### Map setup
- Map đang sử dụng là 1 map 6x6, tuy nhiên ta sẽ cộng thêm 1 dãy vào mỗi phía của map (để phát hiện và kết thúc nếu nhân vật vượt khỏi phạm vi của map), các ô cộng thêm (các ô không đi được / ngoài phạm vi của map) được gán giá trị 0
- Những ô bước lên 1 lần được gán giá trị 1, bước lên 2 lần được gán giá trị 2. Ví dụ:
  ```Python 
  map1 = [0,0,0,0,0,0,0,0,
  0,1,1,1,1,2,0,0,
  0,1,1,1,1,2,1,0,
  0,1,1,1,1,1,1,0,
  0,1,1,0,1,1,1,0,
  0,1,2,1,1,1,1,0,
  0,0,1,1,0,0,0,0,
  0,0,0,0,0,0,0,0]
  ```


### Objective funtion
- Vị trí ban đầu ở ô start (start = 52), điểm ban đầu của ô cờ là -16, set điểm tổng và số bước là 0 
```Python
    pos = start
    flag_pt, point = -16, 0
    n_steps = 0
```
- Từ các gen 1,2,3,4 ở chromosome, ta lần lượt cho nhân vật di chuyển trong map
  - n_columns là số cột ở mỗi hàng trong map chuẩn (6+2 cột), map đã setup là mảng một chiều nên ta sẽ dùng +-n_columns để di chuyển trong map
    - Ví dụ: số 1 là up, để "di chuyển lên" trong map thì ta trừ đi n_colums (trừ đi tổng số ô trong một hàng, trong trường hợp này là 8)
  - Sau khi di chuyển đến 1 ô trong map, kiểm tra xem đó có phải là ô bước lên được hay không: ô bước lên được sẽ mang giá trị >0, ô không bước lên được sẽ mang giá trị =0, nếu ô di chuyển đến là ô mang giá trị 0 (không bước lên được), ta di chuyển ngược trở lại và tiếp tục với gen tiếp theo
    - Ví dụ trong trường hợp gen = 1:
    ```Python
    if gen ==1:
            pos = pos - n_columns
            if map[pos] == 0:
                pos = pos + n_columns
    ```
  - Nếu như ô đó là ô bước lên được (ô mang giá trị > 0), trừ 1 điểm ở ô đó
    ```Python
    if gen ==1:
          pos = pos - n_columns
          map[pos] = map[pos] -1
    if gen ==2:
          pos = pos + n_columns
          map[pos] = map[pos] -1
    ```
  - Tương tự với khi gene = 3,4, để di chuyển sang trái, phải thì ta +=1
    ```Python
    if gen ==3:
            pos = pos -1
            map[pos] = map[pos] -1
        if gen ==4:
            pos = pos +1
            map[pos] = map[pos] -1
    ```
- Khi đi đến ô cờ, cộng thêm điểm đã tích lũy trong ô cờ (điểm tích lũy ở ô cờ là khác nhau dựa trên số bước đã đi trước khi đến ô cờ)
  ```Python
  if pos == flag_pos:
      point = point + flag_pt
  ```
- Mỗi khi di chuyển được 1 bước, cộng một cho số bước và cho ô cờ
  ```Python
  flag_pt = flag_pt + 1
  n_steps = n_steps + 1
  ```
- Sau khi đã đi qua hết các gen trong chromosom, ta tiến hành cộng điểm fitness của cá thể:
  ```Python
  point = point + n_steps - round(block_distance/2)
  ```
    - Với n_steps là số bước đi được và block_distance là tổng khoảng cách của những ô còn lại (những ô chưa bước lên) đến ô cờ, được tính như sau:
    ```Python
    for i in range(len(map)):
        if map[i]==1 or map[i]==2:
            block_distance = block_distance + (((i-flag_pos)/n_columns)**2 + (flag_pos%n_columns - i%n_columns)**2)**0.5
    ```

### Mutation
- Mutation em đang sử dụng là thay đổi giá trị một gene bất kì
  - n_mut_max là số gen tối đa trong một chromosom thực hiện mutation
  - Ta random số gen sẽ thay đổi giá trị, sau đó random các điểm bất kì trên chromosom để thực hiện mutation
    ```Python
      n_mut = randint(0,n_mut_max+1)
      for i in range(n_mut):
          child[randint(0,gen_num)] = randint(1,5)
      return child
    ```

### Crossover
- Tương tự như mutation, nếu rand() nhỏ hơn tỉ lệ crossover (r_cross) thì ta tiến hành crossover tạo ra 2 cá thể con c1 và c2
  - Split point sẽ được chọn ngẫu nhiên từ 1 đến số thứ tự gene mà cá thể không đi tiếp được trong map (giúp việc crossover hiệu quả hơn)
  ```Python
  if rand() < r_cross:
        pt = randint(1, max(objective(n_columns, flag_pos, start, p1, map)[1], objective(n_columns, flag_pos, start, p2, map)[1],2))
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1,c2]
  ```
- Nếu rand() nhỏ hơn tỉ lệ crossover thì ta giữ nguyên kiểu gen của bố mẹ làm kiểu gen của đời con

### Selection
- Sử dụng tournament selection để chọn ra 1 cá thể tốt nhất trong 5 cá thể bất kì
  ```Python
  def selection(scores, pop, k=3):
    selection_ix = randint(len(pop))
    for i in [randint(len(pop)) for _ in range(k)]:
        if scores[i] > scores[selection_ix]:
            selection_ix = i
    return pop[selection_ix]
  ```

### Genetic Algorithm
- Khởi tạo quần thể ban đầu với số gen trong mỗi chromosom là gen_num (sẽ được đề cập ở phần hyperparameter), thiết lập điểm tốt nhất, gen tốt nhất về 0, n_counter là biến dùng để đếm số thế hệ đã tạo ra
  ```Python
    pop = [randint(1,5,gen_num) for _ in range(n_pop)] 
    global n_mut_max
    best, best_eval = [], 0
    n_counter = 0
  ```
- Trong mỗi lần lặp lại:
  - Tính số điểm cho mỗi cá thể trong quần thể
    ```Python
     scores = [objective(n_columns, flag_pos, start, chrom, map)[0] for chrom in pop]
    ```
  - Dựa vào số điểm để
    - Tìm ra cá thể tốt nhất trong quần thể ở thế hệ hiện tại
      ```Python
      if scores[k]> gen_best_eval:
            gen_best_eval, gen_best = scores[k], pop[k]
      ```
    - Tìm ra cá thể tốt nhất
      ```Python
      if scores[k] > best_eval:
            best, best_eval = pop[k], scores[k]
      ```
    - Thêm các giá trị thu được vào x (thế hệ hiện tại), y1 (độ phù hợp cao nhất của thế hệ hiện tại), y2 (số bước đi được cao nhất của thế hệ hiện tại) để vẽ đồ thị trực quan
      ```Python
      x.append(i)
      y1.append(gen_best_eval)
      y2.append(objective(gen_best, map)[1])
      ```
    - Chọn n_pop cá thể bố mẹ tốt nhất (n_pop là số cá thể trong quần thể, một cá thể có điểm fitness cao có thể được chọn nhiều lần)
      ```Python
      selected = [selection(scores, pop) for _ in range(n_pop)]
      ```
    - Tiến hành crossover và mutation
      ```Python
      children = list()
        for j in range(0, n_pop, 2):
            p1 = selected[j]
            p2 = selected[j+1]
            for c in crossover(p1, p2, r_cross, map):
                children.append(mutation(c,r_mut))
      ```
    - Cuối cùng thay thế toàn bộ con đã tạo ra vào quần thể
      ```Python
      pop = children
      ```
    - Ngoài ra, em thêm một cơ chế khởi tạo lại quần thể nếu như độ phù hợp cao nhất của mỗi thế hệ không tăng trong n_max_gen thế hệ (với n_max_gen thiết lập = 2000)
      ```Python
      if n_counter == n_max_gen:
          gui(refine(best, map), map_num)
          print(f"Regenerate population at generation no.{i}")
          pop = [randint(1,5,gen_num) for _ in range(n_pop)] 
          best_eval = 0
          n_counter = 0
      ```

### Các biến số
- Set-up vị trí ô cờ, ô bắt đầu, tổng số bước đi, số cột trong map đã thiết lập, độ phù hợp cao nhất có thể đạt được, số gen trong một nhiễm sắc thể
- x, y1, y2 là các mảng dùng để vẽ đồ thị
  ```Python
  flag_pos = maps2.flag(map_num)
  start_pos = maps2.start(map_num)
  total_step = maps2.steps_calc(map)
  n_columns = maps2.columns(map_num)
  map_best = maps2.best(map_num)
  gen_num = round(total_step*3/2)
  x, y1, y2 = [], [], []
  ```

### Các Hyperparameter
- n_pop là số cá thể trong quần thể
- n_mut_max là số gen tối đa sẽ thay đổi giá trị khi tiến hành đột biến 1 nhiễm sắc thể
- r_cross là tỉ lệ crossover
- n_iter là số lần lặp lại / số thế hệ
- n_max_gen là số thế hệ lặp lại tối đa với độ phù hợp không đổi trước khi khởi tạo lại quần thể
  ```Python
    n_pop = 100
    n_mut_max = 3
    r_cross = 0.7
    n_iter = 10000
    n_max_gen = 2000
      ```

## Các vấn đề chưa giải quyết được
- GUI bị chậm khi đi được một nửa map
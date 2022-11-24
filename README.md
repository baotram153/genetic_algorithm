# README
- [README](#readme)
  - [Ý tưởng](#ý-tưởng)
  - [Mô tả chương trình](#mô-tả-chương-trình)
    - [Các thư viện sử dụng](#các-thư-viện-sử-dụng)
    - [Map setup](#map-setup)
    - [Steps calculation](#steps-calculation)
    - [Objective funtion](#objective-funtion)
    - [Mutation](#mutation)
    - [Crossover](#crossover)
    - [Selection](#selection)
    - [Genetic Algorithm](#genetic-algorithm)
    - [Các Hyperparameter](#các-hyperparameter)
  - [Các vấn đề chưa giải quyết được](#các-vấn-đề-chưa-giải-quyết-được)


## Ý tưởng
- Em dùng map level 8 của Reach the Flag để làm môi trường chạy cho thuật toán
<img src="https://github.com/baotram153/genetic_algorithm/blob/main/RTF_level8.png" width="750" height="550">
- Ý tưởng của em là biến map thành dãy một chiều (bắt đầu từ ô đầu tiên bên trái, lần lượt từ trái sang phải, trên xuống dưới, kết thúc ở ô cuối cùng bên phải), những ô bước lên 1 lần được đánh số 1, những ô bước lên 2 lần được đánh số 2, những ô không bước lên được đánh số -1 (sẽ giải thích ở phần mô tả chương trình)
  - Ví dụ với map phía trên, hàng thứ 4 sẽ được mã hóa [...,1,1,-1,1,1,1,...]
- Các cá thể (chromosom) là những dãy mà mỗi phần tử (gene) là các số từ 1 đến 4 (lần lượt là up, down, left, right)
  - Ví dụ: [4,1,1,3] là right $\rightarrow$ up $\rightarrow$ up $\rightarrow$ left
- Dựa vào các chromosom, ta sẽ lần lượt trừ đi 1 ở những ô đã bước lên 
- Cách tính fitness point cho mỗi cá thể: lấy số bước đi được cộng với điểm được tích lũy ở ô cờ mỗi lần bước lên ô cờ (ban đầu set điểm cho ô cờ là số âm để khuyến khích các cá thể không đến ô cờ trước)
  - Ví dụ: set điểm cho ô cờ là -10, cá thể đi được 15 bước và bước lên ô cờ vào 2 lần: lần thứ nhất ở bước thứ 6, lần thứ 2 ở bước thứ 13, điểm fitness của cá thể đó sẽ là: 15 + (-10+6) + (-10+13) = 14 điểm


## Mô tả chương trình
### Các thư viện sử dụng
- Numpy (sử dụng các hàm randint(), rand())
- PySimpleGUI (build UI)
- matplotlib (vẽ đồ thị)

### Map setup
- Map đang sử dụng là 1 map 6x6, tuy nhiên ta sẽ cộng thêm 1 dãy vào mỗi phía của map (để phát hiện và kết thúc nếu nhân vật vượt khỏi phạm vi của map), các ô cộng thêm (các ô không đi được / ngoài phạm vi của map) được gán giá trị 0
- Những ô bước lên 1 lần được gán giá trị 1, bước lên 2 lần được gán giá trị 2
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

### Steps calculation
- Hàm này dùng để tính tổng số bước cần phải đi với map đã setup, nhằm tính số gene cần random trong 1 chromosom
  ```Python
    def steps_calc(map):
    steps = 0
    for i in range(len(map)):
        if map[i]>0:
            steps = steps + map[i]
    return steps
  ```

### Objective funtion
- Vị trí ban đầu ở ô start (start = 52), điểm ban đầu của ô cờ là -16, set điểm tổng và số bước là 0 
```Python
    pos = start
    flag_pt, point = -16, 0
    n_steps = 0
```
- Từ các gene 1,2,3,4 ở chromosome, ta lần lượt cho nhân vật di chuyển trong map
  - n_columns là số cột ở mỗi hàng trong map chuẩn (6+2 cột), map đã setup là mảng một chiều nên ta sẽ dùng +-n_columns để di chuyển trong map
    - Ví dụ: số 1 là up, để "di chuyển lên" trong map thì ta trừ đi n_colums (trừ đi tổng số ô trong một hàng, trong trường hợp này là 8)
  - Sau khi di chuyển đến 1 ô trong map, trừ 1 điểm ở ô đó
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
- Sau mỗi lần di chuyển, check xem nhân vật có bước vào ô không được đi hay không, nếu có thì tiến hành cộng điểm fitness: điểm fitness là tổng số ô đã tính được ở trên (nếu nhân vật đã đi vào ô cờ) cộng với số bước đã đi được (n_steps) 
  ```Python
  for block in map:
          if block ==-1:
              point = point + n_steps
              return point, n_steps
  ```

### Mutation
- Mutation em đang sử dụng là thay đổi giá trị một gene bất kì bởi 1 trong 3 giấ trị còn lại
  - Với mỗi gene trong chromosom, random 1 giá trị bất kì từ 0 đến 1, nếu giá trị random được nhỏ hơn tỉ lệ mutation (r_mut) thì tiến hành mutation
    ```Python
      for i in range(len(child)):
            if rand() < r_mut:
    ```
  - Random giá trị bất kì từ 1 đến 4, nếu trùng với giá tri gene hiện tại thì ta tiếp tục random giá trị mới
    ```Python
            gen = randint(1,5)  # random from 1 to 4
            while gen == child[i]:    
                gen = randint(1,5)
            child[i] = gen
    return child
    ```

### Crossover
- Đời con ban đầu mặc định giống với đời bố mẹ
  ```Python
    c1 = p1.copy()
    c2 = p2.copy()
  ```
- Tương tự như mutation, nếu rand() nhỏ hơn tỉ lệ crossover (r_cross) thì ta tiến hành crossover với 2 cá thể con c1 và c2
  - Split point sẽ được chọn ngẫu nhiên từ 1 đến số thứ tự gene mà cá thể không đi tiếp được trong map (giúp việc crossover hiệu quả hơn)
  ```Python
  if rand() < r_cross:
        pt = randint(1, max(objective(n_columns, flag_pos, start, p1, map)[1], objective(n_columns, flag_pos, start, p2, map)[1],2))
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1,c2]
  ```

### Selection
- Sử dụng tournament selection để chọn ra 1 cá thể tốt nhất trong 3 cá thể bất kì
  ```Python
  def selection(scores, pop, k=3):
    selection_ix = randint(len(pop))
    for i in [randint(len(pop)) for _ in range(k)]:
        if scores[i] > scores[selection_ix]:
            selection_ix = i
    return pop[selection_ix]
  ```

### Genetic Algorithm
- Tính số bước đi (tương ứng với số gene trong một chromosom) cần phải đi trong map, khởi tạo quần thể ban đầu, set điểm tốt nhất, gen tốt nhất về 0
  ```Python
    steps =steps_calc(map)
    pop = [randint(1,5,steps) for _ in range(n_pop)] 
    best, best_eval = 0, 0
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
    - Thêm các giá trị thu được vào x, y để vẽ đồ thị trực quan
      ```Python
      x.append(i)
        y.append(objective(n_columns, flag_pos, start, gen_best, map)[1])
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

### Các Hyperparameter
- n_pop là số cá thể trong quần thể
- r_mut là tỉ lệ mutation
- r_cross là tỉ lệ crossover
- n_columns là số cột trong một hàng (của map hiện tại)
- flag_pos, start là vị trí ô flag, vị trí ô start trong map đã setup
- n_iter là số lần lặp lại / số thế hệ
- x, y là các mảng dùng để vẽ đồ thị
```Python
  n_pop = 200
  r_mut = 0.05
  r_cross = 0.9
  n_columns = 8
  flag_pos = 13
  start = 52
  n_iter = 500
  x, y = [], []
```
## Các vấn đề chưa giải quyết được
- Các chromosom về cuối không giữ được tính đa dạng và bị mắc lại ở local optimum, do những chromosom có triển vọng đạt global optimum nhưng điểm ban đầu không cao dẫn đến bị loại bỏ từ sớm
- Chưa tìm được cách tính điểm phù hợp để khuyến khích các cá thể vừa đi được nhiều bước vừa đến ô flag cuối cùng

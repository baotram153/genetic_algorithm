#OUTLINE:
#   -map setup: an array with the value of each element is the number of steps the character can step on that block
#   -each string is randomed from 1 to 4 (4 values Up, Down, Left, Right)
#   -mutation: change 1 bit
#   -crossover: normal crossover
#   -objective function: -1 each time the character steps on a block, loop through the array once every turn, if there's any block = -1, over,
#+1 point for the Flag block every steps the character make, the charater will earn that much point when step on the Flag block
#   -How to make U,R,L,D steps legit?
#       + outline = 0 --> over when there's a -1 or a -3
#       + if outline = 0 --> difficulte to calculate fitness point
#--------

from numpy.random import randint
from numpy.random import rand

import PySimpleGUI as sg
import time
from time import time
from time import sleep

import matplotlib.pyplot as plt

#GUI
def gui(best):
    # overall
    CANVAS_SIZE = 500
    CELL_NUM = 6
    CELL_SIZE = CANVAS_SIZE / CELL_NUM

    # omitted cells
    om_cell_pos = [(0,0),(4,0),(5,0),(2,2),(5,5)]
    for i in range (CELL_NUM+1):
        om_cell_pos.extend([(i, CELL_NUM), (CELL_NUM, i), (-1, i), (i,-1)]) # window close when out of range
    # double cells
    doub_cell_pos = [(1,1),(4,4)]

    #flag
    flag_pos = (4,5)

    # character
    START_CELL = (3,0)
    char_pos = (START_CELL[0]*CELL_SIZE + CELL_SIZE/2, START_CELL[1]*CELL_SIZE + CELL_SIZE/2)
    char_coord = (round((char_pos[0]-CELL_SIZE/2)/CELL_SIZE, 0), round((char_pos[1]-CELL_SIZE/2)/CELL_SIZE,0))
    DIRECTIONS = {'left' : (-1,0), 'right': (1,0), 'up': (0,1), 'down': (0,-1)}
    direction = (0,0)

    #convert position to pixel
    def convert_pos_to_pixel(cell):
        bl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
        tr = bl[0] + CELL_SIZE, bl[1] + CELL_SIZE
        return bl, tr

    field = sg.Graph(canvas_size=(CANVAS_SIZE, CANVAS_SIZE), 
            graph_bottom_left=(0,0), graph_top_right=(CANVAS_SIZE, CANVAS_SIZE))

    layout = [[sg.Text(f'Score:', font='Courier 20'),sg.Text('0', font='Courier 20', expand_x =True, key = '-SCORE-'),
        sg.Text(f'Time:', font='Courier 20'), sg.Text(0, font = 'Courier 20', key = '-TIME-')],
        [field]]

    window = sg.Window('Reach the Flag', layout)

    #set up timer
    start_time = time()
    score = 0
    normal_cell = [(50,50)]


    while True:
        #keyboard and score
        for gene in best:
            event, values = window.read(timeout = 10)
            if gene == 3:
                direction = DIRECTIONS['left']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                    else:
                        normal_cell = [(50,50)]
            elif gene == 1:
                direction = DIRECTIONS['up']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                    else:
                        normal_cell = [(50,50)]
            elif gene == 4:
                direction = DIRECTIONS['right']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                    else:
                        normal_cell = [(50,50)]
            elif gene == 2:
                direction = DIRECTIONS['down']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                    else:
                        normal_cell = [(50,50)]
            else: 
                direction = (0,0)
                pre_coord = (50,50)
            window['-SCORE-'].update(score)


            #update position
            char_pos = (char_pos[0] + direction[0]*CELL_SIZE, char_pos[1] + direction[1]*CELL_SIZE)
            char_coord = (round((char_pos[0]-CELL_SIZE/2)/CELL_SIZE, 0), round((char_pos[1]-CELL_SIZE/2)/CELL_SIZE,0))

            #update map
            for cell in om_cell_pos:
                if char_coord == cell:
                    window.close()
                    return
            om_cell_pos.append(pre_coord)
            for cell in doub_cell_pos:
                if char_coord == cell:
                    doub_cell_pos.remove(cell)
                    normal_cell.clear()
                    normal_cell.append(cell)

            #draw map
            for i in range(CELL_NUM):   #normal blocks
                for j in range(CELL_NUM):
                    bl,tr = convert_pos_to_pixel((i,j))
                    field.DrawRectangle(bl, tr, fill_color = 'goldenrod', line_color = 'slategrey')
            for i in om_cell_pos:   #omitted blocks
                bl_om, tr_om = convert_pos_to_pixel(i)
                field.DrawRectangle(bl_om, tr_om, fill_color = 'slategrey', line_color = 'slategrey')
            for i in doub_cell_pos:
                bl_doub, tr_doub = convert_pos_to_pixel(i)
                field.DrawRectangle(bl_doub, tr_doub, fill_color='darkgoldenrod', line_color='slategrey')
            bl_fl, tr_fl = convert_pos_to_pixel(flag_pos)   #flag
            field.DrawRectangle(bl_fl, tr_fl, fill_color = 'indianred', line_color = 'slategrey')

            #draw_character
            field.DrawCircle(char_pos , radius = CELL_SIZE/2.5, fill_color = 'darkslategrey', line_color='slategrey')


            #time
            elapsed_time = round(time() - start_time, 1)
            window['-TIME-'].update(elapsed_time)

        #break
        if event == sg.WIN_CLOSED:
            break

    window.close()

#plot
def plot(x,y):
    plt.rcParams['font.size'] = 10
    plt.rcParams['font.family'] = "serif"
    tdir = 'in'
    major = 4.0
    minor = 2.0
    plt.rcParams['xtick.direction'] = tdir
    plt.rcParams['ytick.direction'] = tdir
    plt.rcParams['xtick.major.size'] = major
    plt.rcParams['xtick.minor.size'] = minor
    plt.rcParams['ytick.major.size'] = major
    plt.rcParams['ytick.minor.size'] = minor
    plt.xlabel('generation')
    plt.ylabel('fitness point')
    plt.scatter(x, y, s=20)
    plt.show()

# objective function
    # 1: U  2: D    3: L    4: R
def objective(n_columns, flag_pos, start, chrom, map):
    map = map1.copy()
    pos = start
    flag_pt, point = -16, 0
    n_steps = 0  #calculate actual steps
    for gen in chrom:
        if gen ==1:
            pos = pos - n_columns
            map[pos] = map[pos] -1
        if gen ==2:
            pos = pos + n_columns
            map[pos] = map[pos] -1
        if gen ==3:
            pos = pos -1
            map[pos] = map[pos] -1
        if gen ==4:
            pos = pos +1
            map[pos] = map[pos] -1
        if pos == flag_pos:
            point = point + flag_pt   #if reach flag: +flag point
        flag_pt = flag_pt + 1
        n_steps = n_steps + 1
        for block in map:
            if block ==-1:
                point = point + n_steps
                return point, n_steps    #int



# map setup
map1 = [0,0,0,0,0,0,0,0,
0,1,1,1,1,2,0,0,
0,1,1,1,1,2,1,0,
0,1,1,1,1,1,1,0,
0,1,1,0,1,1,1,0,
0,1,2,1,1,1,1,0,
0,0,1,1,0,0,0,0,
0,0,0,0,0,0,0,0]


#steps calculation
    #steps = number of bit in a string
def steps_calc(map):
    steps = 0
    for i in range(len(map)):
        if map[i]>0:
            steps = steps + map[i]
    return steps    #int


#mutation
def mutation(child, r_mut):
    for i in range(len(child)):
        if rand() < r_mut:
            gen = randint(1,5)  # random from 1 to 4
            while gen == child[i]:    #make sure that new gene != current gene
                gen = randint(1,5)
            child[i] = gen
    return child    #array


#crossover
def crossover(p1, p2, r_cross, map):
    p1 = list(p1)
    p2 = list(p2)
    c1 = p1.copy()
    c2 = p2.copy()
    if rand() < r_cross:
        pt = randint(1, max(objective(n_columns, flag_pos, start, p1, map)[1], objective(n_columns, flag_pos, start, p2, map)[1],2))
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1,c2]  # 2d-array


#selection
def selection(scores, pop, k=3):
    selection_ix = randint(len(pop))
    for i in [randint(len(pop)) for _ in range(k)]:
        if scores[i] > scores[selection_ix]:
            selection_ix = i
    return pop[selection_ix]


#genetic algorithm
def genetic_algorithm(n_pop, r_mut, r_cross, n_columns, flag_pos, start, map, objective):
    steps =steps_calc(map)
    pop = [randint(1,5,steps) for _ in range(n_pop)] 
    best, best_eval = 0, 0

    #iteration
    for i in range(n_iter):
        gen_best_eval, gen_best = 0, 0
        scores = [objective(n_columns, flag_pos, start, chrom, map)[0] for chrom in pop]   #array
        for k in range(len(scores)):
            #print best of generation
            if scores[k]> gen_best_eval:
                gen_best_eval, gen_best = scores[k], pop[k]
            #print overall best
            if scores[k] > best_eval:
                best, best_eval = pop[k], scores[k]
                print(f'Current best: {best_eval} || {best}')
                gui(best)
        print(f'Best of generation no.{i}: {gen_best_eval} || {gen_best}')

        #plot
        x.append(i)
        y.append(objective(n_columns, flag_pos, start, gen_best, map)[1])

        #selection
        selected = [selection(scores, pop) for _ in range(n_pop)]

        #crossover and mutation
        children = list()
        for j in range(0, n_pop, 2):
            p1 = selected[j]
            p2 = selected[j+1]
            for c in crossover(p1, p2, r_cross, map):
                children.append(mutation(c,r_mut))
        pop = children
    return best, best_eval


#hyperparameters
n_pop = 200
r_mut = 0.05
r_cross = 0.9
n_columns = 8
flag_pos = 13
start = 52
n_iter = 500
x, y = [], []

#display
best, best_eval = genetic_algorithm(n_pop, r_mut, r_cross, n_columns, flag_pos, start, map1, objective)
print("Done!")
print(f"Current best: {best_eval} || {best}")
plot(x,y)

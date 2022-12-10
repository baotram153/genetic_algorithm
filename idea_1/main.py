#OUTLINE:
#   -map setup: an array with the value of each element is the number of steps the character can step on that block
#   -each string is randomed from 1 to 4 (4 values Up, Down, Left, Right)
#   -mutation: change 1 bit
#   -crossover: normal crossover
#   -objective function: -1 each time the character steps on a block, loop through the array once every turn, if there's any block = -1, over,
# +1 point for the Flag block every steps the character make, the charater will earn that much point when step on the Flag block
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

import maps
import guis
from guis import gui

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
    plt.ylabel('number of steps')
    plt.scatter(x, y, s=20)
    plt.show()

# objective function
    # 1: U  2: D    3: L    4: R
def objective(n_columns, flag_pos, start_pos, chrom, map, total_step):
    map = map.copy()
    pos = start_pos
    flag_pt, point = (-round(total_step/2)), 0
    n_steps, distance, block_distance = 0, 0, 0  #calculate actual steps
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
        for block in map:
            if block ==-1:
                #distance = round(abs((flag_pos-pos)/n_columns)) + abs(flag_pos%n_columns - pos%n_columns)
                #point = point + n_steps - distance
                for i in range(len(map)):
                    if map[i]==1 or map[i]==2:
                        block_distance = block_distance + (((i-flag_pos)/n_columns)**2 + (flag_pos%n_columns - i%n_columns)**2)**0.5
                point = point + n_steps - round(block_distance/2)
                return point, n_steps    #array
        flag_pt = flag_pt + 1
        n_steps = n_steps + 1 
        for block in map:
            if n_steps == total_step:
                point = point + n_steps
                return point, n_steps


#mutation
def mutation(child, r_mut):
    for i in range(len(child)):
        if rand() < r_mut: 
            gen = randint(1,5)
            while gen == child[i]:    #make sure that new gene != current gene
                gen = randint(1,5)
            child[i] = gen
    return child    #array


#crossover 1

def crossover(p1, p2, r_cross, map):
    p1 = list(p1)
    p2 = list(p2)
    c1 = p1.copy()
    c2 = p2.copy()
    if rand() < r_cross:
        #pt = randint(1, max(objective(n_columns, flag_pos, start_pos, p1, map, total_step)[1], objective(n_columns, flag_pos, start_pos, p2, map, total_step)[1],2))
        pt = randint(len(p1))
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1,c2]  # 2d-array

'''
#crossover 2
def crossover(p1, p2, r_cross, map):
    p1 = list(p1)
    p2 = list(p2)
    c1 = p1.copy()
    c2 = p2.copy()
    children = [c1,c2]
    if rand() < r_cross:
        pt = randint(1, max(objective(n_columns, flag_pos, start_pos, p1, map, total_step)[1], objective(n_columns, flag_pos, start_pos, p2, map, total_step)[1],2))
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
        children = [c1, c2, p1, p2]
        for k in range(2):
            scores = [objective(n_columns, flag_pos, start_pos, chrom, map, total_step)[1] for chrom in children]
            worst, c_worst = scores[0], children[0]
            for i in range(len(children)):
                if scores[i] < worst:
                    worst = scores[i]
                    c_worst = children[i] 
            children.remove(c_worst)  
    return children
'''

#parents selection
def selection(scores, pop, k=5):
    selection_ix = randint(len(pop))
    for i in [randint(len(pop)) for _ in range(k)]:
        if scores[i] > scores[selection_ix]:
            selection_ix = i
    return pop[selection_ix]

# children selection and pop replacement


#genetic algorithm
def genetic_algorithm(n_pop, r_mut, r_cross, n_columns, flag_pos, start_pos, map, objective, total_step):
    pop = [randint(1,5,total_step) for _ in range(n_pop)] 
    best, best_eval = [], -50
    n_counter = 0
    #iteration
    for i in range(n_iter):
        gen_best_eval, gen_best = -50, []
        scores = [objective(n_columns, flag_pos, start_pos, chrom, map, total_step)[0] for chrom in pop]   #array

        #select best of generation
        for k in range(len(scores)):
            if scores[k]> gen_best_eval:
                gen_best_eval, gen_best = scores[k], pop[k]

        #plot
        x.append(i)
        y.append(objective(n_columns, flag_pos, start_pos, gen_best, map, total_step)[1])

        #if new best = old best: n_counter++
        if gen_best_eval <= best_eval:
            n_counter +=1
        else:
            n_counter = 0

        #select overall best
        if gen_best_eval > best_eval:
            best, best_eval = gen_best, gen_best_eval
            print(f'Current best: {best_eval} || {best}')
            gui(best, map_num)

        #announce winning
        if best_eval >= map_best :
            print("Reach The Flag!")
            print(f"Best: {best}")
            plot(x,y)
            exit()

        #return r_mut to normal value
        if r_mut > 0.8: 
           r_mut = r_mut - 0.8
    
        # shake population
        if n_counter == n_max_gen:
            r_mut = r_mut + 0.8
            n_counter = 0
            gui(gen_best, map_num)

        print(f'Best of generation no.{i}: {gen_best_eval} || {gen_best}')


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

#map setup
map_num = 1
map = maps.select_map(map_num)
flag_pos = maps.flag(map_num)
start_pos = maps.start(map_num)
total_step = maps.steps_calc(map)
n_columns = maps.columns(map_num)
gui = guis.gui
map_best = maps.best(map_num)

#hyperparameters
n_pop = 500
r_mut = 2.2/total_step
r_cross = 0.2
n_iter = 50000
n_max_gen = 2000
x, y = [], []

#display
best, best_eval = genetic_algorithm(n_pop, r_mut, r_cross, n_columns, flag_pos, start_pos, map, objective, total_step)
print("Done!")
print(f"Current best: {best_eval} || {best}")
#plot(x,y)
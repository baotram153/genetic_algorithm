#OUTLINE:
#   -map setup: an array with the value of each element is the number of steps the character can step on that block
#   -each string is randomed from 1 to 4 (4 values Up, Down, Left, Right)
#   -mutation: change 1 bit
#   -crossover: normal crossover
#   -objective function: -1 each time the character steps on a block, loop through the array once every turn, if there's any block = -1, over,
# +1 point for the Flag block every steps the character make, the charater will earn that much point when step on the Flag block
#   -How to make U,R,L,D steps legit?
#       + outline = 0 --> over when there's a
#--------

from numpy.random import randint
from numpy.random import rand

import PySimpleGUI as sg
import time
from time import time
from time import sleep

import matplotlib.pyplot as plt

import maps2
import guis2
from guis2 import gui

#plot
def plot1(x,y):
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
    #plt.ylabel('number of steps')
    plt.scatter(x, y, s=20)
    plt.show()

def plot2(x,y):
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
    #plt.ylabel('fitness point')
    plt.ylabel('number of steps')
    plt.scatter(x, y, s=20)
    plt.show()

# objective function
    # 1: U  2: D    3: L    4: R
def objective(chrom, map):
    map = map.copy()
    pos = start_pos
    flag_pt, point = (-round(total_step/2)), 0
    n_steps, distance, block_distance = 0, 0, 0  #calculate actual steps
    for gen in chrom:
        if gen ==1:
            pos = pos - n_columns
            if map[pos] == 0:
                pos = pos + n_columns
            else:
                map[pos] = map[pos] -1
                n_steps = n_steps + 1
                flag_pt = flag_pt + 1
        elif gen ==2:
            pos = pos + n_columns
            if map[pos] == 0:
                pos = pos - n_columns
            else:
                map[pos] = map[pos] -1
                n_steps = n_steps + 1
                flag_pt = flag_pt + 1
        elif gen ==3:
            pos = pos -1
            if map[pos] == 0:
                pos = pos + 1
            else:
                map[pos] = map[pos] -1
                n_steps = n_steps + 1
                flag_pt = flag_pt + 1
        elif gen ==4:
            pos = pos +1
            if map[pos] == 0:
                pos = pos - 1
            else:
                map[pos] = map[pos] -1
                n_steps = n_steps + 1
                flag_pt = flag_pt + 1
        if pos == flag_pos:
            point = point + flag_pt   #if reach flag: +flag point
            flag_pt = 0
                #distance = round(abs((flag_pos-pos)/n_columns)) + abs(flag_pos%n_columns - pos%n_columns)
                #point = point + n_steps - distance
    for i in range(len(map)):
        if map[i]==1 or map[i]==2:
            block_distance = block_distance + (((i-flag_pos)/n_columns)**2 + (flag_pos%n_columns - i%n_columns)**2)**0.5
    point = point + n_steps - round(block_distance/2)
    return point, n_steps


#mutation
def mutation(child):
    for i in range(gen_num):
        if rand() < r_mut: 
            gen = randint(1,5)
            while gen == child[i]:    #make sure that new gene != current gene
                gen = randint(1,5)
            child[i] = gen
    return child    #array


#crossover 1

def crossover(p1, p2):
    p1 = list(p1)
    p2 = list(p2)
    c1 = p1.copy()
    c2 = p2.copy()
    if rand() < r_cross:
        #pt = randint(1, max(objective(n_columns, flag_pos, start_pos, p1, map, total_step)[1], objective(n_columns, flag_pos, start_pos, p2, map, total_step)[1],2))
        pt = randint(gen_num)
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
    selection_ix = randint(n_pop)
    for i in [randint(n_pop) for _ in range(k)]:
        if scores[i] > scores[selection_ix]:
            selection_ix = i
    return pop[selection_ix]

# children selection and pop replacement

#refine best solution to draw gui
def refine(best, map):
    map = map.copy()
    pos = start_pos
    best_refined = []
    for gen in best:
        if gen ==1:
            pos = pos - n_columns
            if map[pos] == 0:
                pos = pos + n_columns
            else:
                map[pos] = map[pos] -1
                best_refined.append(gen)
        elif gen ==2:
            pos = pos + n_columns
            if map[pos] == 0:
                pos = pos - n_columns
            else:
                map[pos] = map[pos] -1
                best_refined.append(gen)
        elif gen ==3:
            pos = pos -1
            if map[pos] == 0:
                pos = pos + 1
            else:
                map[pos] = map[pos] -1
                best_refined.append(gen)
        elif gen ==4:
            pos = pos +1
            if map[pos] == 0:
                pos = pos - 1
            else:
                map[pos] = map[pos] -1
                best_refined.append(gen)
    return best_refined
#genetic algorithm
def genetic_algorithm(map, objective):
    pop = [randint(1,5,gen_num) for _ in range(n_pop)] 
    global r_mut
    best, best_eval = [], 0
    n_counter = 0
    #iteration
    for i in range(n_iter):
        gen_best_eval, gen_best = 0, []
        scores = [objective(chrom, map)[0] for chrom in pop]   #array

        #select best of generation
        for k in range(len(scores)):
            if scores[k]> gen_best_eval:
                gen_best_eval, gen_best = scores[k], pop[k]

        #plot
        x.append(i)
        y1.append(gen_best_eval)
        #y2.append(objective(gen_best, map)[1])

        #if new best = old best: n_counter++
        if gen_best_eval <= best_eval:
            n_counter +=1
        else:
            n_counter = 0

        #select overall best
        if gen_best_eval > best_eval:
            best, best_eval = gen_best, gen_best_eval
            print(f'Current best: {best_eval} || {best} || Generation no.{i}')
            #gui(best, map_num)

        #announce winning
        if best_eval >= map_best :
            print("Reach The Flag!")
            print(f"Best: {best}")
            
            # refine best answer
            best_refined = refine(best, map)
            print(best_refined)
            
            # use refined best answer to draw gui
            gui(best_refined, map_num)
            plot1(x,y1)
            #plot2(x,y2)
            exit()

        #return r_mut to normal value
        if r_mut > 0.8:
            r_mut -=0.8
    
        # shake population
        if n_counter == n_max_gen:
            gui(refine(best, map), map_num)
            r_mut += 0.8
            print(f"Shake population at generation no.{i}")
            best_eval = 0
            n_counter = 0
            #gui(gen_best, map_num)

        #print(f'Best of generation no.{i}: {gen_best_eval} || {gen_best}')

        #selection
        selected = [selection(scores, pop) for _ in range(n_pop)]

        #crossover and mutation
        children = list()
        for j in range(0, n_pop, 2):
            p1 = selected[j]
            p2 = selected[j+1]
            for c in crossover(p1, p2):
                children.append(mutation(c))
        pop = children
    return best, best_eval

#map setup
map_num = 13
map = maps2.select_map(map_num)
flag_pos = maps2.flag(map_num)
start_pos = maps2.start(map_num)
total_step = maps2.steps_calc(map)
n_columns = maps2.columns(map_num)
gui = guis2.gui
map_best = maps2.best(map_num)
gen_num = round(total_step*3/2)

#hyperparameters
n_pop = 500
r_mut = 3/gen_num
r_cross = 0.3
n_iter = 10000
n_max_gen = 1000
x, y1, y2 = [], [], []

#display
genetic_algorithm(map, objective)
#print("Done!")
#print(f"Current best: {best_eval} || {best}")
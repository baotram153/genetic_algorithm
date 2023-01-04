import numpy as np
from numpy import random
from time import time
import copy

# map setup
def select_map(map_num):
  if map_num == 8:
            map = [0,0,0,0,0,0,0,0,
            0,1,1,1,1,1,0,0,        #flag = 13
            0,1,1,1,1,2,1,0,
            0,1,1,1,1,1,1,0,
            0,1,1,0,1,1,1,0,
            0,1,2,1,1,1,1,0,
            0,0,1,1,0,0,0,0,
            0,0,0,0,0,0,0,0]

  if map_num == 5:
            map = [0,0,0,0,0,0,0,0, 
            0,0,0,0,0,0,0,0,        #start = 13
            0,0,0,0,0,1,0,0,
            0,0,0,0,0,1,0,0,
            0,1,3,1,1,3,1,0,        #flag = 34
            0,0,1,0,0,1,0,0,
            0,0,0,0,0,0,0,0,]

  if map_num == 4:
            map = [0,0,0,0,
            0,0,0,0,        #start = 5
            0,1,0,0,
            0,1,0,0,
            0,2,1,0,
            0,1,0,0,        #flag = 21
            0,0,0,0]
        
  if map_num == 6:
            map = [0,0,0,0,0,0,0, 
            0,1,1,0,0,0,0,      #start = 10
            0,1,1,1,1,0,0,      #flag = 18
            0,1,1,1,1,1,0,
            0,1,1,1,1,1,0,
            0,0,0,0,0,0,0]

  if map_num == 7:
            map = [0,0,0,0,0,0,0,0,
            0,0,0,1,1,0,0,0,
            0,0,0,1,1,0,0,0,
            0,1,1,1,1,1,1,0,        #flag = start = 30
            0,1,1,1,1,1,1,0,        
            0,0,0,1,1,1,0,0,
            0,0,0,1,1,1,0,0,
            0,0,0,0,0,0,0,0]

  if map_num == 10:
            map = [0,0,0,0,0,0,0,0,      
            0,0,0,0,1,1,0,0,        
            0,0,1,1,2,2,1,0,        #start = 17
            0,0,0,0,1,2,1,0,
            0,0,0,0,0,1,0,0,
            0,0,0,0,0,1,0,0,
            0,0,0,0,0,1,0,0,        #flag = 53
            0,0,0,0,0,0,0,0]

  if map_num == 11:
            map = [0,0,0,0,0,0,0,0,0,    
            0,0,0,1,1,1,1,0,0,      
            0,0,0,1,2,2,2,0,0,      #start = 25
            0,1,1,1,1,2,1,0,0,      #flag = 28
            0,0,0,1,1,1,0,0,0,
            0,0,0,0,0,0,0,0,0]

  if map_num == 12:
            map = [0,0,0,0,0,0,0,0,0,0, 
            0,0,0,0,0,1,1,0,0,0,    #start = 14
            0,0,0,1,2,2,1,0,0,0,
            0,0,1,2,2,1,1,1,0,0,
            0,1,1,1,1,0,1,2,1,0,    #flag = 41
            0,0,0,1,1,1,1,2,1,0,
            0,0,0,0,0,1,1,1,0,0,
            0,0,0,0,0,0,0,0,0,0]

  if map_num == 9:
            map = [0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,    #start = 11
            0,0,1,2,1,0,0,0,
            0,1,2,1,1,0,0,0,
            0,1,1,1,1,0,0,0,
            0,0,1,2,1,1,0,0,
            0,1,2,1,1,1,0,0,
            0,1,1,0,1,1,1,0,    #flag = 62
            0,0,0,1,2,1,0,0,
            0,0,0,1,1,0,0,0,
            0,0,0,0,0,0,0,0]

  if map_num == 13:
            map = [0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,      #start = 16
            0,0,0,0,1,2,1,0,0,0,0,
            0,0,0,0,1,2,2,1,0,0,0,
            0,0,0,0,0,1,1,2,1,0,0,
            0,1,1,1,1,1,1,1,1,1,0,      #flag = 56
            0,0,1,2,2,0,0,0,1,1,0,
            0,0,0,1,2,1,2,2,1,0,0,
            0,0,0,0,0,0,1,1,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0]     

  if map_num == 20:
            map = [0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,        #start = 18
            0,0,0,0,0,1,1,1,0,0,0,0,
            0,0,0,0,0,2,1,1,0,0,0,0,
            0,0,0,1,2,2,2,2,2,1,0,0,
            0,0,1,1,2,1,1,1,1,2,2,0,        #flag = 70
            0,0,1,2,3,1,3,1,1,1,1,0,
            0,1,1,1,1,3,1,2,0,0,0,0,
            0,1,1,2,2,1,1,2,1,0,0,0,
            0,0,0,0,0,1,1,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0]

  if map_num == 24:    # map 11x11
            map = [0,0,0,0,0,0,0,0,0,0,0,0,0,   
            0,0,0,0,0,0,0,0,0,0,0,0,0,      # start = 20
            0,0,0,0,0,0,0,2,1,0,0,0,0,
            0,0,0,0,0,0,1,1,0,0,0,0,0,
            0,0,0,0,1,1,1,2,1,0,0,0,0,
            0,0,0,0,1,2,2,2,2,2,2,2,0,      # flag = 76
            0,0,1,1,0,1,1,1,1,0,3,1,0,
            0,1,1,1,2,1,1,0,0,1,1,0,0,
            0,2,1,0,2,1,2,1,1,1,0,0,0,
            0,2,2,0,2,2,2,1,0,0,0,0,0,
            0,0,1,1,4,1,1,1,0,0,0,0,0,
            0,0,0,1,1,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0]
  return map

def columns(num):
        if num == 8:
            n_column = 8
        if num == 5:
            n_column = 8
        if num == 4:
            n_column = 4
        if num == 6:
            n_column = 7
        if num == 7:
            n_column = 8
        if num == 10:
            n_column = 8
        if num == 11:
            n_column = 9
        if num == 12:
            n_column = 10
        if num == 9:
            n_column = 8
        if num == 13: 
            n_column = 11
        if num == 20:
            n_column = 12
        if num == 24:
            n_column = 13
        return n_column

def start(num):
        if num == 8:
            start = 52
        if num == 5:
            start = 13
        if num == 4:
            start = 5
        if num == 6:
            start = 10
        if num == 7:
            start = 30
        if num == 10:
            start = 17
        if num == 11:
            start = 25
        if num == 12:
            start = 14
        if num == 9:
            start = 11
        if num == 13:
            start = 16
        if num == 20:
            start = 18
        if num == 24:
            start = 20
        return start

def flag(num):
        if num == 8:
            flag = 13
        if num == 5:
            flag = 34
        if num == 4:
            flag = 21
        if num == 6:
            flag = 18
        if num == 7:
            flag = 30
        if num == 10:
            flag = 53
        if num == 11:
            flag = 28
        if num == 12:
            flag = 41
        if num == 9:
            flag = 62
        if num == 13: 
            flag = 56
        if num == 20:
            flag = 70
        if num == 24:
            flag = 76
        return flag

def best_score(num):
        if num == 8:
            best = 48
        if num == 5:
            best = 20
        if num == 4:
            best = 8
        if num == 6:
            best = 24
        if num == 7:
            best = 32
        if num == 10:
            best = 24
        if num == 11:
            best = 31
        if num == 12:
            best = 50
        if num == 9:
            best = 52
        if num == 13:
            best = 62
        if num == 20:
            best = 90
        if num == 24:
            best = 103
        return best     # objective function: n_steps + flag_pt - block_distance

#steps calculation
    #steps = number of bit in a string
def steps_calc(map):
    steps = 0
    for i in range(len(map)):
        if map[i]>0:
            steps = steps + map[i]
    steps = steps + 1
    return steps    #int

"""### Main program

#### Objective function
"""

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
    for i in range(len(map)):
        if map[i]==1 or map[i]==2:
            block_distance = block_distance + (((i-flag_pos)/n_columns)**2 + (flag_pos%n_columns - i%n_columns)**2)**0.5
    point = point + n_steps - round(block_distance/2)
    return point, n_steps

"""#### Mutation"""

def mutation(child, n_mut_max):
    n_mut = random.randint(0,n_mut_max+1)
    for i in range(n_mut):
        child[random.randint(0,gen_num)] = random.randint(1,5)
    return child

"""#### Crossover"""

def crossover(p1, p2, r_cross):
    p1 = list(p1)
    p2 = list(p2)
    if random.rand() < r_cross:
        #pt = randint(1, max(objective(n_columns, flag_pos, start_pos, p1, map, total_step)[1], objective(n_columns, flag_pos, start_pos, p2, map, total_step)[1],2))
        pt = random.randint(gen_num)
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
        return [c1,c2]  # 2d-array
    else:
        return[p1,p2]

"""#### Selection"""

def selection(scores, pop, n_pop, k=5):
    selection_ix = random.randint(n_pop)
    for i in [random.randint(n_pop) for _ in range(k)]:
        if scores[i] > scores[selection_ix]:
            selection_ix = i
    return pop[selection_ix]

"""#### Genetic Algorithm (put everything together)"""

def genetic_algorithm(n_pop, n_mut_max, r_cross):
    start_time = time()
    pop = [random.randint(1,5,gen_num) for _ in range(n_pop)] 
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

        time_elapsed = time() - start_time
        if time_elapsed > time_limit:
            return best, best_eval, time_elapsed

        #select overall best
        if gen_best_eval > best_eval:
            best, best_eval = gen_best, gen_best_eval
            # print(f'Current best: {best_eval} || {best} || Generation no.{i} || {int(time_elapsed/60)} min {round(time_elapsed-(int(time_elapsed/60))*60,2)} sec')

        #announce winning
        if best_eval >= map_best :
            return best, best_eval, time_elapsed
    
        # regenerate population
        if time_elapsed > time_limit/2 and n_counter == 0:  
            # print(f"Regenerate population at generation no.{i}")
            pop = [random.randint(1,5,gen_num) for _ in range(n_pop)] 
            best_eval = 0
            n_counter = 1

        #selection
        selected = [selection(scores, pop, n_pop) for _ in range(n_pop)]

        #crossover and mutation
        children = list()
        for j in range(0, n_pop, 2):
            p1 = selected[j]
            p2 = selected[j+1]
            for c in crossover(p1, p2, r_cross):
                children.append(mutation(c, n_mut_max))
        pop = children

"""#### Variables and Hyperparameter"""

#hyperparameters
n_iter = 20000


"""## Hyperparameter tuning

### Objective function
"""

# objective: time minimized
def objective2(ind):
    n_pop, r_cross, n_mut_max = ind #unpack ind
    best, best_eval, time_elapsed = genetic_algorithm(n_pop, n_mut_max, r_cross)
    if best_eval < map_best:
        print(f"Hyperparameter set {ind} unfinished in {time_limit} sec")
        return 'pass'
    else:
        print(f"Hyperparameter set {ind} finished in {time_elapsed}")
        return time_elapsed

"""#### Uniform crossover"""

def crossover2(p1, p2, r_cross):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)
    for i in range (3):
        if random.rand() < r_cross:
            c1[i], c2[i] = p2[i], p1[i]
    return c1, c2


"""#### Mutation
- Current value incremented/decremented by search step
"""

def mutation2(c, n_max_mut):
    n_mut = random.randint(0, n_max_mut+1)
    for i in range(n_mut):
        k = random.randint(0,3)
        if k == 0:
            c[0] = round(c[0] + random.randint(-2,3)*pop_step,2)   # + or - step
            if c[0] > pop_upper:    # put c[0] back to range if out of range
                c[0] = pop_upper
            if c[0] < pop_lower:
                c[0] = pop_lower
        elif k == 1: 
            c[1] = round(c[1] + random.randint(-2,3)*cross_step,2)
            if c[1] > cross_upper:
                c[1] = cross_upper
            if c[1] < cross_lower:
                c[1] = cross_lower
        elif k == 2:
            c[2] = round(c[2] + random.randint(-2,3)*mut_step,2)
            if c[2] > mut_upper:
                c[2] = mut_upper
            if c[2] < mut_lower:
                c[2] = mut_lower
    return c

"""#### Selection
- Ranking
"""

def selection2(pop_copy, k):
    selected = []
    for ind in pop_copy[:k]:
        selected.append(ind)
    return selected

"""### Genetic Algorithm"""

def genetic_algorithm_2(n_pop, n_max_mut, r_cross, k):
    curr_time = time()
    pop = []    # 2-dimensional array with chromosomes and their scores
    
    while (len(pop) < n_pop):
        ind = [random.choice(pop_spc), round(random.choice(cross_spc),2), random.choice(mut_spc)]
        ind_score = objective2(ind)
        if ind_score != 'pass':
            pop.append([ind, ind_score])
            print(f'Current population: {pop}')

    #sort population based on time (fitness score)
    pop_sorted = sorted(pop, key = lambda x:x[1])
    
    for i in range(n_iter):
        print(f'Population in generation no.{i+1}: {pop_sorted}')

        #selection
        pop_copy = copy.deepcopy(pop_sorted)
        selected = selection2(pop_copy, k)
        print(f'Parents seleted in this generation: {selected}')

        #crossover
        children = [] # 1-dimensional array
        for j in range(3):
            children.extend(crossover2(selected[random.randint(0,k)][0], selected[random.randint(0,k)][0], r_cross))
        print(f'Children after Crossover: {children}')
        
        #mutation and selection
        for c in children:
            c_mut = mutation2(c, n_max_mut)
            c_score = objective2(c)
            if c_score != 'pass':
                pop_sorted.append([c_mut, c_score])
                pop_sorted = sorted(pop_sorted, key = lambda x:x[1])[:-1]
        print(f'Best solution after {i+1} generation(s): {pop_sorted[0]}\n')

"""### Variables and Hyperparameters"""

#map setup
map_num = 24
map = select_map(map_num)
flag_pos = flag(map_num)
start_pos = start(map_num)
total_step = steps_calc(map)
n_columns = columns(map_num)
map_best = best_score(map_num)
gen_num = round(total_step*3/2)

# set restrictions
pop_step = 100
pop_lower = 100
pop_upper = 1000
pop_spc = np.arange(pop_lower, pop_upper, pop_step)
cross_step = 0.1
cross_lower = 0.1
cross_upper = 1
cross_spc = np.arange(cross_lower, cross_upper, 0.1)
mut_step = 1
mut_lower = 1
mut_upper = 10
mut_spc = np.arange(mut_lower, mut_upper, 1)

# hyperparameters
k2 = 3
n_max_mut2 = 3
n_pop2 = 5
r_cross2 = 0.5
n_iter2 = 5
time_limit = 30

"""### Run everything"""

genetic_algorithm_2(n_pop2, n_max_mut2, r_cross2, k2)
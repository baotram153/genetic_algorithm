import numpy as np
from numpy import random 
from main import genetic_algorithm
from main import map_best
import copy
from time import time

# objective: time minimized
def objective(ind):
    n_pop, n_mut_max, r_cross = ind #unpack ind
    best, best_eval, time_elapsed = genetic_algorithm(n_pop, n_mut_max, r_cross)
    if best_eval < map_best:
        return 'pass'
    else:
        return time_elapsed

# crossover: 2-point crossover
'''
def crossover(p1, p2, r_cross):
    if random.rand() < r_cross:
        ptA, ptB = random.randint(0, len(p1)), random.randint(0, len(p1))
        pt1, pt2 = min(ptA, ptB), max(ptA, ptB)
        c1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
        c2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:]
        return c1,c2
    else:
        return p1,p2
'''

#crossover: uniform crossover
def crossover(p1, p2, r_cross):
    c1 = copy.deepcopy(p1)
    c2 = copy.deepcopy(p2)
    for i in range (3):
        if random.rand() < r_cross:
            c1[i], c2[i] = p2[i], p1[i]
    return c1, c2


# mutation 1: random value in search space
'''
def mutation(c, n_max_mut):
    n_mut = random.randint(0,n_max_mut+1)
    for i in range(n_mut):
        k = random.randint(0,3)
        if k == 0:
            c[0] = random.choice(pop_spc)
        elif k == 1: 
            c[1] = random.choice(cross_spc)
        elif k == 2:
            c[2] = random.choice(mut_spc)
    return c
'''
# mutation 2: current value +- search step
def mutation(c, n_max_mut):
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

# selection: ranking
def selection(pop_copy, k):
    selected = []
    for ind in pop_copy[:k]:
        selected.append(ind)
    return selected

# genetic algorithm
def genetic_algorithm_2(n_pop, n_max_mut, r_cross, k):
    # curr_time = time()
    pop = []    # 2-dimensional array with chromosomes and their scores
    
    while (len(pop) < n_pop):
        ind = [random.choice(pop_spc), round(random.choice(cross_spc),2), random.choice(mut_spc)]
        ind_score = objective(ind)
        if ind_score != 'pass':
            pop.append([ind, ind_score])
            print(f'Current population: {pop}')
    

    #sort population based on time (fitness score)
    pop_sorted = sorted(pop, key = lambda x:x[1])
    # print(time()-curr_time)
    # exit()

    for i in range(n_iter):
        print(f'Population in generation no.{i}: {pop_sorted}')

        #selection
        pop_copy = copy.deepcopy(pop_sorted)
        selected = selection(pop_copy, k)
        print(f'Parents seleted in this generation: {selected}')

        #crossover
        children = [] # 1-dimensional array
        for j in range(3):
            children.extend(crossover(selected[random.randint(0,k)][0], selected[random.randint(0,k)][0], r_cross))
        print(f'Children after Crossover: {children}')
        
        #mutation and selection
        for c in children:
            c_mut = mutation(c, n_max_mut)
            print(f'Hyperparameter set: {c_mut}')
            c_score = objective(c)
            if c_score != 'pass':
                pop_sorted.append([c_mut, c_score])
                pop_sorted = sorted(pop_sorted, key = lambda x:x[1])[:-1]
        print(f'Best solution after {i+1} generation(s): {pop_sorted[0]}')
    
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
k=3
n_max_mut = 3
n_pop = 5
r_cross = 0.5
n_iter = 5

genetic_algorithm_2(n_pop, n_max_mut, r_cross, k)
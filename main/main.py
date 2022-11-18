import numpy
from numpy.random import randint
from numpy.random import rand
from numpy import random
from numpy import size

#set up level 8 map
map1 = [[0,-1],[0,-1],[0,-1],[0,-1],[33,-1],[-1,-1],
[0,-1],[0,-1],[0,-1],[0,-1],[0,0],[0,-1],
[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],
[0,-1],[0,-1],[-1,-1],[0,-1],[0,-1],[0,-1],
[0,-1],[0,0],[0,-1],[0,-1],[0,-1],[0,-1],
[-1,-1],[0,-1],[0,-1],[1,-1],[-1,-1],[-1,-1]]


# total steps to make
def steps(map):
    steps = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                steps = steps + 1
    return steps #int


# make a shuffle list out of the number of available blocks
def ran_list(steps): #int
    ran_arr = (numpy.arange(2,steps+2))
    random.shuffle(ran_arr)
    return ran_arr #array


#insert a shuffle list to our array
def insert(ran_arr, map ,steps): #array (used for crossover and mutation)
    ran_arr_iterator = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]!=-1 and map[i][j]!=1 and map[i][j]!=steps+2:
                map[i][j]= ran_arr[ran_arr_iterator]
                ran_arr_iterator = ran_arr_iterator + 1
    return map  #two dimensional array (used for calculating fitness point)


#calculate fitness point
def fit_func(map):  #two dimensional array
    n_rows = 6
    scores = 0
    for i in range(len(map)):
        if i==0:    #top-left
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i+1][k]+1 or map[i][j] == map[i+n_rows][k]+1 or map[i][j] == map[i+1][k]-1 or map[i][j] == map[i+n_rows][k]-1:
                        scores = scores + 1
        elif i==n_rows-1:
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i-1][k]+1 or map[i][j] == map[i+n_rows][k]+1 or map[i][j] == map[i-1][k]-1 or map[i][j] == map[i+n_rows][k]-1:
                        scores = scores + 1
        elif i==len(map)-1:
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i-1][k]+1 or map[i][j] == map[i-n_rows][k]+1 or map[i][j] == map[i-1][k]-1 or map[i][j] == map[i-n_rows][k]-1:
                        scores = scores + 1
        elif i==len(map)-n_rows:
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i+1][k]+1 or map[i][j] == map[i-n_rows][k]+1 or map[i][j] == map[i+1][k]-1 or map[i][j] == map[i-n_rows][k]-1:
                        scores = scores + 1
        elif i%n_rows == 0:
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i-n_rows][k]+1 or map[i][j] == map[i+n_rows][k]+1 or map[i][j] == map[i+1][k]+1 or map[i][j] == map[i+n_rows][k]-1 or map[i][j] == map[i-n_rows][k]-1 or map[i][j] == map[i+1][k]-1:
                        scores = scores + 1
        elif (i%n_rows == n_rows-1):
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i+n_rows][k]+1 or map[i][j] == map[i-n_rows][k]+1 or map[i][j] == map[i-1][k]+1 or map[i][j] == map[i+n_rows][k]-1 or map[i][j] == map[i-n_rows][k]-1 or map[i][j] == map[i][j] == map[i-1][k]-1:
                        scores = scores + 1
        elif (i <= 5):
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i+1][k]+1 or map[i][j] == map[i-1][k]+1 or map[i][j] == map[i+n_rows][k]+1 or map[i][j] == map[i+1][k]-1 or map[i][j] == map[i-1][k]-1 or map[i][j] == map[i+n_rows][k]-1:
                        scores = scores + 1
        elif (i >= len(map)-6):
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i+1][k]+1 or map[i][j] == map[i-1][k]+1 or map[i][j] == map[i-n_rows][k]+1 or map[i][j] == map[i+1][k]-1 or map[i][j] == map[i-1][k]-1 or map[i][j] == map[i-n_rows][k]-1:
                        scores = scores + 1
        else: 
            for j in range(len(map[i])):
                for k in range(len(map[i])):
                    if map[i][j] == map[i+1][k]+1 or map[i][j] == map[i-1][k]+1 or map[i][j] == map[i-n_rows][k]+1 or map[i][j] == map[i+n_rows][k]+1 or map[i][j] == map[i+1][k]-1 or map[i][j] == map[i-1][k]-1 or map[i][j] == map[i-n_rows][k]-1 or map[i][j] == map[i+n_rows][k]-1:
                        scores = scores + 1
    return scores   #int


#ordered-chromosome crossover
def crossover(p1, p2, r_cross): # 2 one dimensional list, 1 float
    p1=list(p1)
    p2=list(p2)
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination:
    if rand() < r_cross:
		# select crossover point that is not on the end of the string
        pt = randint(1, len(p1)-1)
        c1 = p1[:pt]
        c2 = p2[:pt]
        for x1 in c1:
            p2.remove(x1)
        for x2 in p2:
            c1.append(x2)
        for x3 in c2:
            p1.remove(x3)
        for x4 in p1:
            c2.append(x4)
    return [c1, c2] #array of 2 child


#mutation (change position of 2 genes)
def mutation(children, r_mut):   # 1 child array, 1 float
    for i in range(len(children)):
        # check for a mutation
        if rand() < r_mut:
        #change position
            a = randint(len(children))
            b = randint(len(children)) #future update: b!=a
            c = children[a]
            children[a] = children[b]
            children[b] = c
    return children

#tournament selection
def selection(pop, scores, k=3):    # 1 two dimensional array, 2 ints
    selection_i = randint(len(pop))
    for i in randint(0, len(pop), k):
        if scores[i] > scores[selection_i]:
            selection_i = i
    return pop[selection_i]


#genetic algorithm
def genetic_algorithm(map, objective, n_pop, r_cross, r_mut, n_iter):
    #initialize population
    n_steps = steps(map)
    pop_arr = [ran_list(n_steps) for _ in range(n_pop)]     #pop[i] is a random array
    pop_map = [insert(arr, map, n_steps) for arr in pop_arr]     #convert arrays into maps
    best, best_eval = pop_map[0], objective(pop_map[0])
    
    #iteration
    for i in range(n_iter):
        #selection
        scores = [objective(m) for m in pop_map]
        for j in range(n_pop):
            if scores[j] > best_eval:
                best, best_eval = pop_map[j].copy(), scores[j]
                print(f"Current best: {scores[j]} | {pop_map[j]}")
        selected = [selection(pop_arr,scores) for _ in range(n_pop)]
        #children
        children_arr = list()
        children_map = list()
        for k in range(0, n_pop, 2):
            p1, p2 = selected[k], selected[k+1]
            for c in crossover(p1, p2, r_cross):
                mutation(c, r_mut)
                children_arr.append(c)
        #replace population
        pop_arr = children_arr
        children_map=[insert(arr, map, n_steps) for arr in children_arr]
        pop_map = children_map

    return best_eval, best
        
#define some hyperparameters
map = map1
n_pop = 200
r_cross = 0.8
r_mut = 0.05
n_iter = 500

#perform GA and display
best_eval, best = genetic_algorithm(map, fit_func, n_pop, r_cross, r_mut, n_iter)

print("Done!")
print(best, best_eval)
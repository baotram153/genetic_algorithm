#OUTLINE:
#   -map setup: an array with the value of each element is the number of steps the character can step on that block
#   -each string is randomed from 1 to 4 (4 values Up, Down, Left, Right)
#   -mutation: change 1 bit
#   -crossover: normal crossover
#   -objective function: -1 each time the character steps on a block, loop through the array once every turn, if there's any block = -1, over,
#+1 point for the Flag block every steps the character make, the charater will earn that much point when step on the Flag block
#   -How to make U,R,L,D steps legit?
#       + outline = -2 --> over when there's a -1 or a -3
#       + if outline = 0 --> difficulte to calculate fitness point
#--------

from numpy import random
from numpy.random import randint
from numpy.random import rand

# objective function
    # 1: U  2: D    3: L    4: R
def objective(n_rows, flag_pos, start, chrom, map):
    map = map1_2.copy()
    pos = start
    flag_pt, point = 0, 0
    def scores(map):
        point = 0
        for block in map:
            if block == 0:
                point = point + 1
        return point
    for gen in chrom:
        if gen ==1:
            pos = pos - n_rows
            map[pos] = map[pos] -1
        if gen ==2:
            pos = pos + n_rows
            map[pos] = map[pos] -1
        if gen ==3:
            pos = pos -1
            map[pos] = map[pos] -1
        if gen ==4:
            pos = pos +1
            map[pos] = map[pos] -1
        if pos == flag_pos:
            point = point + flag_pt   #if reach flag: +flag point
            flag_pt = 0
        flag_pt = flag_pt + 1
        for block in map:
            if block ==-1 or block ==-3:
                point = point + scores(map)
                return point  #int
        


# map setup
map1 = [-2,-2,-2,-2,-2,-2,-2,-2,
-2,1,1,1,1,2,-2,-2,
-2,1,1,1,1,2,1,-2,
-2,1,1,1,1,1,1,-2,
-2,1,1,-2,1,1,1,-2,
-2,1,2,1,1,1,1,-2,
-2,-2,1,1,0,-2,-2,-2,
-2,-2,-2,-2,-2,-2,-2,-2]
print (map1)

map1_2 = map1.copy()


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
def crossover(p1, p2, r_cross):
    p1 = list(p1)
    p2 = list(p2)
    c1 = p1.copy()
    c2 = p2.copy()
    if rand() < r_cross:
        pt = randint(1, len(p1))
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
def genetic_algorithm(n_pop, r_mut, r_cross, n_rows, flag_pos, start, map, objective):
    steps =steps_calc(map)
    pop = [randint(1,5,steps) for _ in range(n_pop)] 
    best, best_eval = 0, 0
    for i in range(n_iter):
        scores = [objective(n_rows, flag_pos, start, chrom, map) for chrom in pop]   #array
        for k in range(len(scores)):
            if scores[k]> best_eval:
                best, best_eval = pop[k], scores[k]
                print(f"Current best: {best_eval} || {best}")

        #selection
        selected = [selection(scores, pop) for _ in range(n_pop)]

        #crossover and mutation
        children = list()
        for j in range(0, n_pop, 2):
            p1 = selected[j]
            p2 = selected[j+1]
            for c in crossover(p1, p2, r_cross):
                children.append(mutation(c,r_mut))
        pop = children
    return best, best_eval


#hyperparameters
n_pop = 200
r_mut = 0.05
r_cross = 0.9
n_rows = 8
flag_pos = 13
start = 52
n_iter = 500

#display
best, best_eval = genetic_algorithm(n_pop, r_mut, r_cross, n_rows, flag_pos, start, map1, objective)
print("Done!")
print(f"Current best: {best_eval} || {best}")
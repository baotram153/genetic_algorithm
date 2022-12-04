# children selection and replacement based on difference

def child_selection(children, pop, objective, scores):
    children_scores = [objective(n_columns, flag_pos, start, chrom, map)[0] for chrom in children]
    for k in range(len(children)):
        diff_min = len(children[k])
        selected, selected_num = [], 0
        for i in range(len(pop)):   #loop through each parent in current pop
            diff = 0
            for j in range(len(children[k])):  
                if children[k][j] != pop[i][j]:
                    diff = diff + 1
            if diff < diff_min:
                diff_min = diff
                selected, selected_num = pop[i], i
        if children_scores[k] > scores[selected_num]:
            pop[selected_num] = children[k]


# crossover with selection
def crossover(p1, p2, r_cross, map):
    p1 = list(p1)
    p2 = list(p2)
    c1 = p1.copy()
    c2 = p2.copy()
    if rand() < r_cross:
        pt = randint(1, max(objective(n_columns, flag_pos, start_pos, p1, map, total_step)[1], objective(n_columns, flag_pos, start_pos, p2, map, total_step)[1],2))
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
        children = [c1, c2, p1, p2]
        for k in range(2):
            scores = [objective(n_columns, flag_pos, start_pos, chrom, map, total_step)[1] for chrom in children]
            worst = scores[0]
            for i in range(len(children)):
                if scores[i] < worst:
                    worst = scores[i]
                    c_worst = children[i] 
            children.remove(c_worst)  
    return children

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
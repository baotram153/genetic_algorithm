# map setup

def select_map(map_num):

    map1 = [0,0,0,0,0,0,0,0,    #level 8
    0,1,1,1,1,2,0,0,
    0,1,1,1,1,2,1,0,
    0,1,1,1,1,1,1,0,
    0,1,1,0,1,1,1,0,
    0,1,2,1,1,1,1,0,
    0,0,1,1,0,0,0,0,
    0,0,0,0,0,0,0,0]

    map2 = [0,0,0,0,0,0,0,0,    #level 5
    0,0,0,0,0,0,0,0,        #start = 13
    0,0,0,0,0,1,0,0,
    0,0,0,0,0,1,0,0,
    0,1,3,1,1,3,1,0,        #flag = 34
    0,0,1,0,0,1,0,0,
    0,0,0,0,0,0,0,0,]

    map3 = [0,0,0,0,       #level 4
    0,0,0,0,        #start = 5
    0,1,0,0,
    0,1,0,0,
    0,2,1,0,
    0,1,0,0,        #flag = 21
    0,0,0,0]

    map4 = [0,0,0,0,0,0,0,      #level 6
    0,1,1,0,0,0,0,      #start = 10
    0,1,1,1,1,0,0,      #flag = 18
    0,1,1,1,1,1,0,
    0,1,1,1,1,1,0,
    0,0,0,0,0,0,0]

    map5 = [0,0,0,0,0,0,0,0,        #level 7
    0,0,0,1,1,0,0,0,
    0,0,0,1,1,0,0,0,
    0,1,1,1,1,1,2,0,        #flag = start = 30
    0,1,1,1,1,1,1,0,        
    0,0,0,1,1,1,0,0,
    0,0,0,1,1,1,0,0,
    0,0,0,0,0,0,0,0]

    map6 = [0,0,0,0,0,0,0,0,        #level 10
    0,0,0,0,1,1,0,0,        
    0,0,1,1,2,2,1,0,        #start = 17
    0,0,0,0,1,2,1,0,
    0,0,0,0,0,1,0,0,
    0,0,0,0,0,1,0,0,
    0,0,0,0,0,1,0,0,        #flag = 53
    0,0,0,0,0,0,0,0]

    map7 = [0,0,0,0,0,0,0,0,0,      #level 11
    0,0,0,1,1,1,1,0,0,      
    0,0,0,1,2,2,2,0,0,      #start = 25
    0,1,1,1,1,2,1,0,0,      #flag = 28
    0,0,0,1,1,1,0,0,0,
    0,0,0,0,0,0,0,0,0]
    
    maps = [None, map1, map2, map3, map4, map5, map6, map7]
    return maps[map_num]

def columns(num):
    columns = [None, 8, 8, 4, 7, 8, 8, 9]
    return columns[num]

def start(num):
    start = [None, 52, 13, 5, 10, 30, 17, 25]
    return start[num]

def flag(num):
    flag = [None, 13, 34, 21, 18, 30, 53, 28]
    return flag[num]

def best(num):
    best = [None, 50, 26, 8, 23, 50, 23, 31]
    return best[num]

#steps calculation
    #steps = number of bit in a string
def steps_calc(map):
    steps = 0
    for i in range(len(map)):
        if map[i]>0:
            steps = steps + map[i]
    return steps    #int
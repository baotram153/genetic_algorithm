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

    map2 = [0,0,0,0,0,0,0,0,    #level 8
    0,0,0,0,0,0,0,0,        #start = 13
    0,0,0,0,0,1,0,0,
    0,0,0,0,0,1,0,0,
    0,1,3,1,1,3,1,0,        #flag = 34
    0,0,1,0,0,1,0,0,
    0,0,0,0,0,0,0,0,]

    
    maps = [None, map1, map2]
    return maps[map_num]

def columns(num):
    columns = [None, 8, 8]
    return columns[num]

def start(num):
    start = [None, 52, 13]
    return start[num]

def flag(num):
    flag = [None, 13, 34]
    return flag[num]

#steps calculation
    #steps = number of bit in a string
def steps_calc(map):
    steps = 0
    for i in range(len(map)):
        if map[i]>0:
            steps = steps + map[i]
    return steps    #int
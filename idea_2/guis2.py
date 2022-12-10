import PySimpleGUI as sg
import time
from time import time
from time import sleep
import random

def cell_nums(map):
    match map:
        case 8:
            cell_nums = 6
        case 5:
            cell_nums = 6
        case 4:
            cell_nums = 6
        case 6:
            cell_nums = 5
        case 7:
            cell_nums = 6
        case 10:
            cell_nums = 6
        case 11:
            cell_nums = 7
        case 12:
            cell_nums = 8
        case 9:
            cell_nums = 9
        case 13:
            cell_nums = 9
        case 20:
            cell_nums = 10
        case 24: 
            cell_nums = 11
    return cell_nums

def om_cell_poss(map):
    match map:
        case 8:
            om_cell_pos = [(0,0),(4,0),(5,0),(2,2),(5,5)]
        case 5:
            om_cell_pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(2,1),(3,1),(5,1),(0,3),(1,3),(2,3),(3,3),(5,3),
                            (0,4),(1,4),(2,4),(3,4),(5,4),(0,5),(1,5),(2,5),(3,5),(5,5)]
        case 4:
            om_cell_pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(3,1),(4,1),(5,1),(0,2),(1,2),(4,2),(5,2),(0,3),(1,3),(3,3),(4,3),
                            (5,3),(0,4),(1,4),(3,4),(4,4),(5,4),(0,5),(1,5),(3,5),(4,5),(5,5)]
        case 6:
            om_cell_pos = [(4,2),(3,3),(4,3),(0,4),(1,4),(2,4),(3,4),(4,4)]
        case 7:
            om_cell_pos = [(0,0),(1,0),(5,0),(0,1),(1,1),(5,1),(0,4),(1,4),(4,4),(5,4),(0,5),(1,5),(4,5),(5,5)]
        case 10:
            om_cell_pos = [(0,0),(1,0),(2,0),(3,0),(5,0),(0,1),(1,1),(2,1),(3,1),(5,1),(0,2),(1,2),(2,2),(3,2),(5,2),(0,3),(1,3),(2,3),
                            (0,5),(1,5),(2,5),(5,5)]
        case 11:
            om_cell_pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(0,1),(1,1),(5,1),(6,1),(6,2),(0,3),(1,3),(0,4),(1,4),(6,4),
                            (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6)]
        case 12:
            om_cell_pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(0,1),(1,1),(2,1),(3,1),(7,1),(0,2),(1,2),(4,3),(0,4),(7,4),
                            (0,5),(1,5),(6,5),(7,5),(0,6),(1,6),(2,6),(6,6),(7,6),(7,0),(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]
        case 9:
            om_cell_pos = [(0,8),(1,8),(2,8),(4,8),(5,8),(6,8),(7,8),(8,8),(0,7),(1,7),(5,7),(6,7),(7,7),(8,7),
                            (0,6),(5,6),(6,6),(7,6),(8,6),(0,5),(5,5),(6,5),(7,5),(8,5),(0,4),(1,4),(6,4),(7,4),(8,4),
                            (0,3),(6,3),(7,3),(8,3),(0,2),(3,2),(7,2),(8,2),(0,1),(1,1),(2,1),(6,1),(7,1),(8,1),
                            (0,0),(1,0),(2,0),(5,0),(6,0),(7,0),(8,0)]
        case 13:
            om_cell_pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(7,0),(8,0),(0,1),(1,1),(8,1),(0,2),(4,2),(5,2),(6,2),
                            (0,4),(1,4),(2,4),(3,4),(8,4),(0,5),(1,5),(2,5),(7,5),(8,5),(0,6),(1,6),(2,6),(6,6),(7,6),(8,6),
                            (0,7),(1,7),(2,7),(3,7),(5,7),(6,7),(7,7),(8,7),(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)]
        
        case 20:
            om_cell_pos = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(0,1),(1,1),(2,1),(3,1),(6,1),(7,1),(8,1),(9,1),
                            (8,2),(9,2),(7,3),(8,3),(9,3),(0,4),(0,5),(0,6),(1,6),(9,6),(0,7),(1,7),(2,7),(3,7),(7,7),(8,7),(9,7),
                            (0,8),(1,8),(2,8),(3,8),(7,8),(8,8),(9,8),(0,9),(1,9),(2,9),(3,9),(4,9),(6,9),(7,9),(8,9),(9,9)]
                        
        case 24:
            om_cell_pos = [(0,0),(1,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(0,1),(7,1),(8,1),(9,1),(10,1),
                            (2,2),(7,2),(8,2),(9,2),(10,2),(2,3),(9,3),(10,3),(6,4),(7,4),(10,4),(0,5),(3,5),(8,5),
                            (0,6),(1,6),(2,6),(0,7),(1,7),(2,7),(8,7),(9,7),(10,7),(0,8),(1,8),(2,8),(3,8),(4,8),(7,8),(8,8),(9,8),(10,8),
                            (0,9),(1,9),(2,9),(3,9),(4,9),(5,9),(8,9),(9,9),(10,9),(0,10),(1,10),(2,10),(3,10),(4,10),(5,10),(7,10),(8,10),(9,10),(10,10)]

    return  om_cell_pos

def doub_cell_poss(map):
    match map:
        case 8:
            doub_cell_pos = [(1,1),(4,4)]
        case 5:
            doub_cell_pos = [(50,50)]
        case 4:
            doub_cell_pos = [(2,2)]
        case 6:
            doub_cell_pos = [(50,50)]
        case 7:
            doub_cell_pos = [(50,50)]
        case 10:
            doub_cell_pos = [(3,4),(4,4)]
        case 11:
            doub_cell_pos = [(4,2),(3,3),(4,3),(5,3)]
        case 12:
            doub_cell_pos = [(6,2),(6,3),(2,4),(3,4),(3,5),(4,5)]
        case 9:
            doub_cell_pos = [(4,1),(2,3),(3,4),(2,6),(3,7)]
        case 13: 
            doub_cell_pos = [(3,1),(5,1),(6,1),(2,2),(3,2),(6,4),(4,5),(5,5),(4,6)]
        case 20:
            doub_cell_pos = [(2,2),(3,2),(6,2),(6,3),(2,4),(3,5),(8,5),(3,6),(4,6),(5,6),(6,6),(7,6),(4,7)]
        case 24:
            doub_cell_pos = [(0,2),(1,2),(3,2),(4,2),(5,2),(0,3),(3,3),(5,3),(3,4),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(6,7),(6,9)]
    return doub_cell_pos

def trip_cell_poss(map):
    match map:
        case 8:
            trip_cell_pos = [(50,50)]
        case 5:
            trip_cell_pos = [(1,2), (4,2)]
        case 4:
            trip_cell_pos = [(50,50)]
        case 6:
            trip_cell_pos = [(50,50)]
        case 7:
            trip_cell_pos = [(50,50)]
        case 10:
            trip_cell_pos = [(4,3)]
        case 11:
            trip_cell_pos = [(50,50)]
        case 12:
            trip_cell_pos = [(50,50)]
        case 9:
            trip_cell_pos = [(50,50)]
        case 13:
            trip_cell_pos = [(50,50)]
        case 20:
            trip_cell_pos = [(4,3),(3,4),(5,4)]
        case 24:
            trip_cell_pos = [(3,1),(9,5)]
    return trip_cell_pos

def flag_poss(map):
    match map:
        case 8:
            flag_pos = (4,5)
        case 5:
            flag_pos = (1,2)
        case 4:
            flag_pos = (2,1)
        case 6:
            flag_pos = (3,2)
        case 7:
            flag_pos = (5,3)
        case 10:
            flag_pos = (4,0)
        case 11:
            flag_pos = (0,2)
        case 12:
            flag_pos = (0,3)
        case 9:
            flag_pos = (6,2)
        case 13:
            flag_pos = (0,3)
        case 20:
            flag_pos = (9,5)
        case 24:
            flag_pos = (10,6)
    return flag_pos


def start_poss(map):
    match map:
        case 8:
            start_pos = (3,0)
        case 5:
            start_pos = (4,5)
        case 4:
            start_pos = (2,5)
        case 6:
            start_pos = (2,3)
        case 7:
            start_pos = (5,3)
        case 10:
            start_pos = (0,4)
        case 11:
            start_pos = (6,3)
        case 12:
            start_pos = (3,6)
        case 9:
            start_pos = (3,8)
        case 13:
            start_pos = (4,7)
        case 20:
            start_pos = (5,9)
        case 24:
            start_pos = (6,10)
    return start_pos


#GUI
def gui(best, map_num):
    # overall
    CANVAS_SIZE = 500
    CELL_NUM = cell_nums(map_num)
    CELL_SIZE = CANVAS_SIZE / CELL_NUM

    # omitted cells
    om_cell_pos = om_cell_poss(map_num)
    for i in range (CELL_NUM+1):
        om_cell_pos.extend([(i, CELL_NUM), (CELL_NUM, i), (-1, i), (i,-1)])     # window close when out of range

    # double cells
    doub_cell_pos = doub_cell_poss(map_num)

    #triple cells
    trip_cell_pos = trip_cell_poss(map_num)

    #flag
    flag_pos = flag_poss(map_num)

    # character
    start_pos = start_poss(map_num)
    char_pos = (start_pos[0]*CELL_SIZE + CELL_SIZE/2, start_pos[1]*CELL_SIZE + CELL_SIZE/2)
    char_coord = (round((char_pos[0]-CELL_SIZE/2)/CELL_SIZE, 0), round((char_pos[1]-CELL_SIZE/2)/CELL_SIZE,0))
    DIRECTIONS = {'left' : (-1,0), 'right': (1,0), 'up': (0,1), 'down': (0,-1)}
    direction = (0,0)

    #convert position to pixel
    def convert_pos_to_pixel(cell):
        bl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
        tr = bl[0] + CELL_SIZE, bl[1] + CELL_SIZE
        return bl, tr

    field = sg.Graph(canvas_size=(CANVAS_SIZE, CANVAS_SIZE), 
            graph_bottom_left=(0,0), graph_top_right=(CANVAS_SIZE, CANVAS_SIZE))

    layout = [[sg.Text(f'Score:', font='Courier 20'),sg.Text('0', font='Courier 20', expand_x =True, key = '-SCORE-'),
        sg.Text(f'Level:', font='Courier 20'), sg.Text(0, font = 'Courier 20', key = '-LEVEL-')],
        [field]]

    window = sg.Window('Reach the Flag', layout)

    #set up timer
    #start_pos_time = time()
    score = 0
    normal_cell = [(50,50)]


    #while True:
        #keyboard and score
    best.append(1)  # append 1 element for the circle to move to flag
    for gene in best:
        event, values = window.read(timeout = 10)
        if gene == 3:
            direction = DIRECTIONS['left']
            for cell in normal_cell:
                if char_coord != cell:
                    pre_coord = char_coord
                else:
                    normal_cell = [(50,50)]
        elif gene == 1:
            direction = DIRECTIONS['up']
            for cell in normal_cell:
                if char_coord != cell:
                    pre_coord = char_coord
                else:
                    normal_cell = [(50,50)]
        elif gene == 4:
            direction = DIRECTIONS['right']
            for cell in normal_cell:
                if char_coord != cell:
                    pre_coord = char_coord
                else:
                    normal_cell = [(50,50)]
        elif gene == 2:
            direction = DIRECTIONS['down']
            for cell in normal_cell:
                if char_coord != cell:
                    pre_coord = char_coord
                else:
                    normal_cell = [(50,50)]
        else: 
            direction = (0,0)
            pre_coord = (50,50)

        #update position
        
        #if character position = omitted cells --> continue
        '''
        bool_var = False
        for cell in om_cell_pos:
            if (char_coord[0] + direction[0], char_coord[1] + direction[1]) == cell:
                bool_var = True
        if bool_var == True:
            continue
        '''
        
        char_pos = (char_pos[0] + direction[0]*CELL_SIZE, char_pos[1] + direction[1]*CELL_SIZE)
        char_coord = (round((char_pos[0]-CELL_SIZE/2)/CELL_SIZE, 0), round((char_pos[1]-CELL_SIZE/2)/CELL_SIZE,0))
        score +=1
        window['-SCORE-'].update(score)

        #update map
        #for cell in om_cell_pos:
        #    if char_coord == cell:
        #        window.close()
        #if bool_var == False:

        if pre_coord != flag_pos:
            om_cell_pos.append(pre_coord)
        for cell in doub_cell_pos:
            if char_coord == cell:
                doub_cell_pos.remove(cell)
                normal_cell.clear()
                normal_cell.append(cell)
        for cell in trip_cell_pos:
            if char_coord == cell:
                normal_cell.clear()
                normal_cell.append(cell)

        #draw map
        for i in range(CELL_NUM):   #normal blocks
            for j in range(CELL_NUM):
                bl,tr = convert_pos_to_pixel((i,j))
                field.DrawRectangle(bl, tr, fill_color = 'goldenrod', line_color = 'slategrey')
        for i in om_cell_pos:   #omitted blocks
            bl_om, tr_om = convert_pos_to_pixel(i)
            field.DrawRectangle(bl_om, tr_om, fill_color = 'slategrey', line_color = 'slategrey')
        for i in doub_cell_pos:
            bl_doub, tr_doub = convert_pos_to_pixel(i)
            field.DrawRectangle(bl_doub, tr_doub, fill_color='darkgoldenrod', line_color='slategrey')
        for i in trip_cell_pos:
            bl_trip, tr_trip = convert_pos_to_pixel(i)
            field.DrawRectangle(bl_trip, tr_trip, fill_color='honeydew3', line_color='slategrey')
        bl_fl, tr_fl = convert_pos_to_pixel(flag_pos)   #flag
        field.DrawRectangle(bl_fl, tr_fl, fill_color = 'indianred', line_color = 'slategrey')

        #draw_character
        field.DrawCircle(char_pos , radius = CELL_SIZE/2.5, fill_color = 'darkslategrey', line_color='slategrey')

        #time
        #elapsed_time = round(time() - start_pos_time, 1)
        #window['-TIME-'].update(elapsed_time)

        #break when close window
        #if event == sg.WIN_CLOSED:
            #break
    window.close()
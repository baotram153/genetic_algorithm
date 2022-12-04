import PySimpleGUI as sg
import time
from time import time
from time import sleep

def cell_nums(map):
    cell_num = [None, 6, 6, 6, 5, 6, 6, 7, 8, 9]
    return cell_num[map]

def om_cell_poss(map):
    om_cell_pos = [None,
                [(0,0),(4,0),(5,0),(2,2),(5,5)],
                [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(2,1),(3,1),(5,1),(0,3),(1,3),(2,3),(3,3),(5,3),
                    (0,4),(1,4),(2,4),(3,4),(5,4),(0,5),(1,5),(2,5),(3,5),(5,5)],
                [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(3,1),(4,1),(5,1),(0,2),(1,2),(4,2),(5,2),(0,3),(1,3),(3,3),(4,3),
                    (5,3),(0,4),(1,4),(3,4),(4,4),(5,4),(0,5),(1,5),(3,5),(4,5),(5,5)],
                [(4,2),(3,3),(4,3),(0,4),(1,4),(2,4),(3,4),(4,4)],
                [(0,0),(1,0),(5,0),(0,1),(1,1),(5,1),(0,4),(1,4),(4,4),(5,4),(0,5),(1,5),(4,5),(5,5)],
                [(0,0),(1,0),(2,0),(3,0),(5,0),(0,1),(1,1),(2,1),(3,1),(5,1),(0,2),(1,2),(2,2),(3,2),(5,2),(0,3),(1,3),(2,3),
                    (0,5),(1,5),(2,5),(5,5)],
                [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(0,1),(1,1),(5,1),(6,1),(6,2),(0,3),(1,3),(0,4),(1,4),(6,4),
                    (0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6)],
                [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(0,1),(1,1),(2,1),(3,1),(7,1),(0,2),(1,2),(4,3),(0,4),(7,4),
                (0,5),(1,5),(6,5),(7,5),(0,6),(1,6),(2,6),(6,6),(7,6),(7,0),(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)],
                [(0,8),(1,8),(2,8),(4,8),(5,8),(6,8),(7,8),(8,8),(0,7),(1,7),(5,7),(6,7),(7,7),(8,7),
                (0,6),(5,6),(6,6),(7,6),(8,6),(0,5),(5,5),(6,5),(7,5),(8,5),(0,4),(1,4),(6,4),(7,4),(8,4),
                (0,3),(6,3),(7,3),(8,3),(0,2),(3,2),(6,2),(7,2),(8,2),(0,1),(1,1),(2,1),(6,1),(7,1),(8,1),
                (0,0),(1,0),(2,0),(5,0),(6,0),(7,0),(8,0)]
                ]
    return om_cell_pos[map]

def doub_cell_poss(map):
    double_cell_pos = [0,
                        [(1,1),(4,4)], [(50,50)], [(2,2)], [(50,50)], [(50,50)], [(3,4),(4,4)], [(4,2),(3,3),(4,3),(5,3)], 
                        [(6,2),(6,3),(2,4),(3,4),(3,5),(4,5)], [(4,1),(2,3),(3,4),(2,6),(3,7)]]
    return double_cell_pos[map]

def trip_cell_poss(map):
    trip_cell_pos = [None, [(50,50)], [(1,2), (4,2)], [(50,50)], [(50,50)], [(50,50)], [(4,3)], [(50,50)], [(50,50)], [(50,50)]]
    return trip_cell_pos[map]

def flag_poss(map):
    flag_pos = [None, (4,5), (1,2), (2,1), (3,2), (5,3), (4,0), (0,2), (0,3), (6,2)]
    return flag_pos[map]

def start_pos_CELLs(map):
    start_pos_CELL = [None, (3,0), (4,5), (2,5), (2,3), (5,3), (0,4), (6,3), (3,6), (3,8)]
    return start_pos_CELL[map]

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
    start_pos_CELL = start_pos_CELLs(map_num)
    char_pos = (start_pos_CELL[0]*CELL_SIZE + CELL_SIZE/2, start_pos_CELL[1]*CELL_SIZE + CELL_SIZE/2)
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
        sg.Text(f'Time:', font='Courier 20'), sg.Text(0, font = 'Courier 20', key = '-TIME-')],
        [field]]

    window = sg.Window('Reach the Flag', layout)

    #set up timer
    start_pos_time = time()
    score = 0
    normal_cell = [(50,50)]


    while True:
        #keyboard and score
        for gene in best:
            event, values = window.read(timeout = 10)
            if gene == 3:
                direction = DIRECTIONS['left']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                    else:
                        normal_cell = [(50,50)]
            elif gene == 1:
                direction = DIRECTIONS['up']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                    else:
                        normal_cell = [(50,50)]
            elif gene == 4:
                direction = DIRECTIONS['right']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                    else:
                        normal_cell = [(50,50)]
            elif gene == 2:
                direction = DIRECTIONS['down']
                score = score + 1
                for cell in normal_cell:
                    if char_coord != cell:
                        pre_coord = char_coord
                else:
                    normal_cell = [(50,50)]
            else: 
                direction = (0,0)
                pre_coord = (50,50)
            window['-SCORE-'].update(score)


            #update position
            char_pos = (char_pos[0] + direction[0]*CELL_SIZE, char_pos[1] + direction[1]*CELL_SIZE)
            char_coord = (round((char_pos[0]-CELL_SIZE/2)/CELL_SIZE, 0), round((char_pos[1]-CELL_SIZE/2)/CELL_SIZE,0))

            #update map
            for cell in om_cell_pos:
                if char_coord == cell:
                    window.close()
                    return
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
            elapsed_time = round(time() - start_pos_time, 1)
            window['-TIME-'].update(elapsed_time)

        #break
        #if event == sg.WIN_CLOSED:
            #break

    window.close()
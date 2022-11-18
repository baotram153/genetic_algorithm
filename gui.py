import PySimpleGUI as sg
from time import time
from random import randint

# overall
CANVAS_SIZE = 500
CELL_NUM = 6
CELL_SIZE = CANVAS_SIZE / CELL_NUM

# omitted cells
om_cell_pos = [(0,0),(4,0),(5,0),(2,2),(5,5)]

# double cells
doub_cell_pos = [(1,1),(4,4)]

#flag
flag_pos = (4,5)

# character
START_CELL = (3,0)
char_pos = (START_CELL[0]*CELL_SIZE + CELL_SIZE/2, START_CELL[1]*CELL_SIZE + CELL_SIZE/2)
char_coord = (round((char_pos[0]-CELL_SIZE/2)/CELL_SIZE, 0), round((char_pos[1]-CELL_SIZE/2)/CELL_SIZE,0))
DIRECTIONS = {'left' : (-1,0), 'right': (1,0), 'up': (0,1), 'down': (0,-1)}
direction = (0,0)

def convert_pos_to_pixel(cell):
	bl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
	tr = bl[0] + CELL_SIZE, bl[1] + CELL_SIZE
	return bl, tr

field = sg.Graph(canvas_size=(CANVAS_SIZE, CANVAS_SIZE), 
        graph_bottom_left=(0,0), graph_top_right=(CANVAS_SIZE, CANVAS_SIZE))

layout = [[sg.Text(f'Score: ', font=''),sg.Text('0',expand_x =True, key = '-SCORE-'), sg.Text(f'Time:'), sg.Text(0, key = '-TIME-')],
        [field]]

window = sg.Window('convert position to pixel', layout, return_keyboard_events = True)

#set up timer
start_time = time()
score = 0
normal_cell = [[0,0]]


while True:
    event, values = window.read(timeout = 10)

    #keyboard and score
    if event == 'Left:37':
        direction = DIRECTIONS['left']
        score = score + 1
        for cell in normal_cell:
            if char_coord != cell:
                pre_coord = char_coord
            else:
                normal_cell.clear()
                normal_cell.append([0,0])
    elif event == 'Up:38':
        direction = DIRECTIONS['up']
        score = score + 1
        for cell in normal_cell:
            if char_coord != cell:
                pre_coord = char_coord
            else:
                normal_cell.clear()
                normal_cell.append([0,0])
    elif event == 'Right:39':
        direction = DIRECTIONS['right']
        score = score + 1
        for cell in normal_cell:
            if char_coord != cell:
                pre_coord = char_coord
            else:
                normal_cell.clear()
                normal_cell.append([0,0])
    elif event == 'Down:40':
        direction = DIRECTIONS['down']
        score = score + 1
        for cell in normal_cell:
            if char_coord != cell:
                pre_coord = char_coord
            else:
                normal_cell.clear()
                normal_cell.append([0,0])
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
    om_cell_pos.append(pre_coord)
    for cell in doub_cell_pos:
        if char_coord == cell:
            doub_cell_pos.remove(cell)
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
    bl_fl, tr_fl = convert_pos_to_pixel(flag_pos)   #flag
    field.DrawRectangle(bl_fl, tr_fl, fill_color = 'indianred', line_color = 'slategrey')

    #draw_character
    field.DrawCircle(char_pos , radius = CELL_SIZE/2.5, fill_color = 'darkslategrey', line_color='slategrey')

    #time
    elapsed_time = round(time() - start_time, 1)
    window['-TIME-'].update(elapsed_time)
    
    #break
    if event == sg.WIN_CLOSED:
        break
window.close()
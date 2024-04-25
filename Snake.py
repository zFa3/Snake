#!usr/bin/env Python
# zFa3
# Python3 - Snake in Tkinter

# TODO
# add variants
# make snake go in diagonals?
# make game over screen
# main menu

import tkinter as tk, random as rd, time as tm

#important consts
SIDE_LEN = 600 # in pixels
TILE_SIZE = 20 # in pixels
LINE_WID = 1
DELAY = 0.1 # in seconds
PRNT_GRID = False
DEF_LEN = 40
INVINCIBILITY_PERIOD = 3
AREA = [i for i in range(SIDE_LEN)]
toggle = False

# important variables
snake = []
posX = posY = 18
snake_head = [(SIDE_LEN)//2 + 10, (SIDE_LEN)//2 + 10]
apple = [posX * TILE_SIZE + 10, posY * TILE_SIZE + 10]
snake_length = DEF_LEN
gameRunning = True
# all directions snake can go in
# right, left, down, up
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# index in directions list
dir = 2 

# Tkinter things
root = tk.Tk()
root.geometry(f"{SIDE_LEN}x{SIDE_LEN}")
game_canvas = tk.Canvas(root)
game_canvas.config(background="#838383")

def draw():
    global game_canvas
    game_canvas.config(width=SIDE_LEN, height=SIDE_LEN)
    game_canvas.delete("all")
    game_canvas.create_text(SIDE_LEN//2, SIDE_LEN//2, text = str(snake_length - 1), font=("Courier new", 350, "bold"), fill="#C0FFEE")
    if PRNT_GRID:
        for line in range(SIDE_LEN//TILE_SIZE):
            # iterates creating the vertical lines
            game_canvas.create_line(line * TILE_SIZE, 0, line*TILE_SIZE, SIDE_LEN, width = LINE_WID)
        for line in range(SIDE_LEN//TILE_SIZE):
            # create the horizontal lines
            game_canvas.create_line(0, line * TILE_SIZE, SIDE_LEN, line*TILE_SIZE, width = LINE_WID)
    for index, item in enumerate(snake):
        ind_row, ind_col = item[0], item[1]
        game_canvas.create_rectangle(ind_row - 10, ind_col - 10, (ind_row + TILE_SIZE//2), (ind_col + TILE_SIZE//2), fill=(f"#{(hex(0)[2:]):02}{hex(max(int(255 * (index/len(snake))), 0))[2:]:02}{hex(0)[2:]:02}"), outline="")
    game_canvas.create_rectangle(apple[0] - 10, apple[1] - 10, (apple[0] + TILE_SIZE//2), (apple[1] + TILE_SIZE//2), fill="red", outline="")
    game_canvas.update()
    game_canvas.pack()

def keypress(event):
    global dir, toggle
    keycodes = {68:0,87:3,65:1,83:2,37:1,38:3,39:0,40:2}
    invalids = {0:1, 1:0, 2:3, 3:2}
    try:
        if dir != invalids[keycodes[event.keycode]] and toggle:
            dir = keycodes[event.keycode]
            toggle = False
    except: pass
def main():
    global gameRunning, DELAY
    root.bind("w", keypress)
    root.bind("a", keypress)
    root.bind("s", keypress)
    root.bind("d", keypress)
    root.bind("<Down>", keypress)
    root.bind("<Up>", keypress)
    root.bind("<Right>", keypress)
    root.bind("<Left>", keypress)
    global snake_head, apple, snake_length, toggle
    tm.sleep(DELAY*2)
    for i in range(INVINCIBILITY_PERIOD):
        draw()
        tm.sleep(DELAY)
        snake_head[0] += directions[dir][0] * TILE_SIZE
        snake_head[1] += directions[dir][1] * TILE_SIZE
        snake.append(snake_head[:])
        #print(snake)
        if len(snake) >= snake_length:
            snake.pop(0)
        if snake[-1][0] == apple[0] and snake[-1][1] == apple[1]:
            posX, posY = rd.randint(0, 29), rd.randint(0, 29)
            apple = [posX * TILE_SIZE + 10, posY * TILE_SIZE + 10]
            snake_length += 1
        toggle = True
    while gameRunning:
        toggle = True
        draw()
        tm.sleep(DELAY)
        snake_head[0] += directions[dir][0] * TILE_SIZE
        snake_head[1] += directions[dir][1] * TILE_SIZE
        #print(snake)
        if len(snake) >= snake_length:
            snake.pop(0)
        if snake[-1][0] == apple[0] and snake[-1][1] == apple[1]:
            posX, posY = rd.randint(0, 29), rd.randint(0, 29)
            apple = [posX * TILE_SIZE + 10, posY * TILE_SIZE + 10]
            snake_length += 1
            DELAY *= 0.99
            DELAY = max(0.05, DELAY)
            print(DELAY)
        if snake_head in snake or not snake_head[0] in AREA or not snake_head[1] in AREA:
            gameRunning = False
        snake.append(snake_head[:])
tm.sleep(1); main()
# mainloop isnt neccessary?
# root.mainloop()

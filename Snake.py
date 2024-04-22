#!usr/bin/env Python
# zFa3
# Python3 - Snake in Tkinter

# TODO
# add collision detection
# add boundary detection
# add variants
# make snake go in diagonals?
# make game over screen

import tkinter as tk, random as rd, time as tm

#important consts
SIDE_LEN = 600 # in pixels
TILE_SIZE = 20 # in pixels
LINE_WID = 1
DELAY = 0.05 # in seconds
PRNT_GRID = True

# important variables
snake = []
posX = posY = 18
snake_head = [(SIDE_LEN)//2 + 10, (SIDE_LEN)//2 + 10]
apple = [posX * TILE_SIZE + 10, posY * TILE_SIZE + 10]
snake_length = 4
gameRunning = True
# all directions snake can go in
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# index in directions list
dir = 2 

# Tkinter things
root = tk.Tk()
root.geometry(f"{SIDE_LEN}x{SIDE_LEN}")
game_canvas = tk.Canvas(root)

def draw():
    global game_canvas
    game_canvas.config(width=SIDE_LEN, height=SIDE_LEN)
    game_canvas.delete("all")
    if PRNT_GRID:
        for line in range(SIDE_LEN//TILE_SIZE):
            # iterates creating the vertical lines
            game_canvas.create_line(line * TILE_SIZE, 0, line*TILE_SIZE, SIDE_LEN, width = LINE_WID)
        for line in range(SIDE_LEN//TILE_SIZE):
            # create the horizontal lines
            game_canvas.create_line(0, line * TILE_SIZE, SIDE_LEN, line*TILE_SIZE, width = LINE_WID)
    for index in snake:
        ind_row, ind_col = index[0], index[1]
        game_canvas.create_rectangle(ind_row - 10, ind_col - 10, (ind_row + TILE_SIZE//2), (ind_col + TILE_SIZE//2), fill="green")
    game_canvas.create_rectangle(apple[0] - 10, apple[1] - 10, (apple[0] + TILE_SIZE//2), (apple[1] + TILE_SIZE//2), fill="red")
    game_canvas.update()
    game_canvas.pack()

def keypress(event):
    global dir
    keycodes = {
        68:0,
        87:3,
        65:1,
        83:2
    }
    try:
        dir = keycodes[event.keycode]
    except: pass
def main():
    root.bind("w", keypress)
    root.bind("a", keypress)
    root.bind("s", keypress)
    root.bind("d", keypress)
    global snake_head, apple, snake_length
    tm.sleep(DELAY*2)
    while gameRunning:
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
main()
root.mainloop()
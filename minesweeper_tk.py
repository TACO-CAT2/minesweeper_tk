"""
A TACO-CAT2 project. check LICENSE.md
This is a version of minesweeper using the python tkinter
module. It has a 8 by 8 grid that can be edited by changing
the value of SIZE and 10 mines which can be edited by changing
the value of NUMINE
"""


import tkinter as tk
from pprint import pprint
from random import randint as ri
from random import choice as c
from tkinter import PhotoImage as poe




win = tk.Tk()
SIZE = 8
NUMINE = 10
win.geometry("500x600")
win.title("minesweeper tk")
win.rows = SIZE
win.cols = SIZE

red_mine_pic = poe(file="./images/red_mine50.png")
mine_pic = poe(file="./images/mine50.png")
one_pic = poe(file="./images/one50.png")
two_pic = poe(file="./images/two50.png")
three_pic = poe(file="./images/three50.png")
four_pic = poe(file="./images/four50.png")
eight_pic = poe(file="./images/eight50.png")
five_pic = poe(file="./images/five50.png")
six_pic = poe(file="./images/six50.png")
seven_pic = poe(file="./images/seven50.png")
flag_pic = poe(file="./images/flag50.png")
space_pic = poe(file="./images/space50.png")
face_pic = poe(file="./images/face50.png")
cool_pic = poe(file="./images/cool50.png")
sad_pic = poe(file="./images/sad50.png")

numpic_list = (one_pic, two_pic,
            three_pic, four_pic, five_pic,
            six_pic, seven_pic, eight_pic)

top_frame = tk.Frame(win, borderwidth=2)
top_frame.pack()

def reset():
    mine_frame.destroy()
    make_grid()
    result_button["image"] = face_pic


result_button = tk.Button(top_frame,
                          image=face_pic,
                          command=reset)
result_button.pack()





def win_event():
    widgets = mine_frame.grid_slaves()
    count = 0
    for w in widgets:
        if type(w) == tk.Button:
            count += 1
    if count == NUMINE:
        for w in widgets:
            if type(w) == tk.Button:
                w["image"] = flag_pic
                w["width"] = 0
                w["height"] = 0
        result_button["image"] = cool_pic
                     

def clickidy(event):
    info = event.widget.grid_info()
    row, col = info["row"], info["column"]
    disp[row][col].grid_remove()
    num_label = tk.Label(mine_frame)
    num_label.grid(row=row, column=col)
    if grid[row][col] == "M":
        num_label["image"] = red_mine_pic
        result_button["image"] = sad_pic
        for r in range(SIZE):
            for c in range(SIZE):                
                if grid[r][c] == "M":
                    button = mine_frame.grid_slaves(
                        row=r, column=c)[0]
                    button.event_generate("<1>")
                    
                     
    elif int(grid[row][col]) > 0:
        index = int(grid[row][col]) -1
        num_pic = numpic_list[index]
        num_label["image"] = num_pic
    
    elif int(grid[row][col]) == 0:
        num_label["image"] = space_pic
        for r in range(max(0, row-1), min(SIZE, (row+1)+1)):
            for c in range(max(0, col-1), min(SIZE, (col+1)+1)):
                button = mine_frame.grid_slaves(row=r,
                                                column=c)[0]
                button.event_generate("<1>")
    win_event()

def flaggidy(event):
    if not event.widget.is_flagged:
        event.widget["image"] = flag_pic
        event.widget["width"] = 0
        event.widget["height"] = 0
        event.widget.is_flagged = True
    
    else:
        event.widget["image"] = ""
        event.widget["width"] = 6
        event.widget["height"] = 3
        event.widget.is_flagged = False
    

def make_grid():
    global mine_frame, grid, disp
    grid = []
    disp = []
    mine_frame = tk.Frame(win, borderwidth=2)
    mine_frame.pack()
    for row in range(win.rows):
        new_row = []
        new_row2 = []
        for col in range(win.cols):
            new_row.append("X")
            newb = tk.Button(mine_frame,
                             width=6,
                             height=3)
            newb.is_flagged = False
            new_row2.append(newb)
            newb.grid(row=row, column=col)
            newb.row = row
            newb.col = col
            newb.bind("<1>", clickidy)
            newb.bind("<3>", flaggidy)
        grid.append(new_row)
        disp.append(new_row2)

    for _ in range(NUMINE):
        ran_x = ri(0, SIZE-1)
        ran_y = ri(0, SIZE-1)
        while grid[ran_x][ran_y] != "X":
            ran_x = ri(0, SIZE-1)
            ran_y = ri(0, SIZE-1)
        grid[ran_x][ran_y] = "M"


    def mine_check(srow, scol, grid=grid):
        if grid[srow][scol] == "M":
            return True
      
      
    def get_num(trow, tcol, grid=grid):
        count = 0
        for r in range(max(0, trow-1), min(SIZE, (trow+1)+1)):
            for c in range(max(0, tcol-1), min(SIZE, (tcol+1)+1)):
                if trow == r and tcol == c:
                    continue
                if mine_check(r, c):
                    count += 1
        return count 

    for tr in range(SIZE):
        for tc in range(SIZE):
            if grid[tr][tc] == "M":
                continue
            grid[tr][tc] = str(get_num(tr, tc, grid=grid))
    
    
make_grid()


win.mainloop()

from tkinter import *

tapped = None

num = [1, 2, 3, 4,
       5, 6, 7, 8,
       9, 10, 11, 12,
       13, 14, 15, 16]

def card(i):
    global bttns, num
    bttns[i][0]['text'] = str(num[i])

def xy(i):
    if i//4 == 0:
        row = 1
    elif i//4 == 1:
        row = 2
    elif i//4 == 2:
        row = 3
    else:
        row = 4
    if i%4 == 0:
        col = 1
    elif i%4 == 1:
        col = 2
    elif i%4 == 2:
        col = 3
    else:
        col = 4
    return row, col
    

bttns = []
for i in range(16):
    tag = i
    bt = Button(text = '    ', font = 'Arial 20')
    bttn = [bt, tag]
    bt['command'] = lambda: card(bttn[1])
    bttns.append(bttn)
    x, y = xy(i)
    bt.grid(row = x, column = y)
bttn = []
mainloop()

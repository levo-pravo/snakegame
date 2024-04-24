from tkinter import *

tapped = None

num = [1, 2, 3, 4,
       5, 6, 7, 8,
       9, 10, 11, 12,
       13, 14, 15, 16]

def card(i):
    global bttns, num
    bttns[i].config(text = num[i])

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

'''cmnds = []
for i in range(16):
    def cmnd():
        tapped = i
        card(i)
    cmnds.append(cmnd)'''

bttns = []
for i in range(16):
    bttn = Button(text = '    ', font = 'Arial 20', command = lambda i: card(i))
    bttns.append(bttn)
    x, y = xy(i)
    bttn.grid(row = x, column = y)

mainloop()

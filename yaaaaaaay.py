from tkinter import *
from time import sleep

tapped = None

num = [1, 1, 3, 4,
       5, 6, 7, 8,
       9, 10, 11, 12,
       13, 14, 15, 16]

def card(i):
    global bttns, num, tapped
    if bttns[i-1] in bttns:
        bttns[i-1]['text'] = str(num[i-1])
        if tapped != None:
            sleep(0.5)
            if tapped['text'] == bttns[i-1]['text']:
                bttns.remove(tapped)
                bttns.remove(bttns[i-1])
            tapped['text'] = '    '
            bttns[i-1]['text'] = '    '
            tapped = None
        else:
            tapped = bttns[i-1]

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
    
coms = []
def bt1():
    card(1)
coms.append(bt1)
def bt2():
    card(2)
coms.append(bt2)
def bt3():
    card(3)
coms.append(bt3)
def bt4():
    card(4)
coms.append(bt4)
def bt5():
    card(5)
coms.append(bt5)
def bt6():
    card(6)
coms.append(bt6)
def bt7():
    card(7)
coms.append(bt7)
def bt8():
    card(8)
coms.append(bt8)
def bt9():
    card(9)
coms.append(bt9)
def bt10():
    card(10)
coms.append(bt10)
def bt11():
    card(11)
coms.append(bt11)
def bt12():
    card(12)
coms.append(bt12)
def bt13():
    card(13)
coms.append(bt13)
def bt14():
    card(14)
coms.append(bt14)
def bt15():
    card(15)
coms.append(bt15)
def bt16():
    card(16)
coms.append(bt16)

bttns = []
for i in range(16):
    bttn = Button(text = '    ', font = 'Arial 20')
    bttn['command'] = coms[i]
    bttns.append(bttn)
    x, y = xy(i)
    bttn.grid(row = x, column = y)
mainloop()

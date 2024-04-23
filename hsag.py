from tkinter import *

root = Tk()
root.geometry("300x300")

num = [0, 0, 1, 1,
       2, 2, 3, 3,
       4, 4, 5, 5,
       6, 6, 7, 7]

clear = [0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0]

waiter = 0

def c1():
    global b1, waiter
    if clear[0] == 0:
        b1.config(text = num[0])
        waiter+=1
    
b1 = Button(text='    ', font="Arial 20", command=c1)
b1.grid(row=2, column=1)

def c2():
    global b2, waiter
    if clear[1] == 0:
        b2.config(text = num[1])
        waiter+=1
    
b2 = Button(text='    ', font="Arial 20", command=c2)
b2.grid(row=2, column=2)

def c3():
    global b3, waiter
    if clear[2] == 0:
        b3.config(text = num[2])
        waiter+=1
    
b3 = Button(text='    ', font="Arial 20", command=c3)
b3.grid(row=2, column=3)

def c4():
    global b4, waiter
    if clear[3] == 0:
        b4.config(text = num[3])
        waiter+=1
    
b4 = Button(text='    ', font="Arial 20", command=c4)
b4.grid(row=2, column=4)

def c5():
    global b5, waiter
    if clear[4] == 0:
        b5.config(text = num[4])
        waiter+=1
    
b5 = Button(text='    ', font="Arial 20", command=c5)
b5.grid(row=3, column=1)

def c6():
    global b6, waiter
    if clear[5] == 0:
        b6.config(text = num[5])
        waiter+=1
    
b6 = Button(text='    ', font="Arial 20", command=c6)
b6.grid(row=3, column=2)

def c7():
    global b7, waiter
    if clear[6] == 0:
        b7.config(text = num[6])
        waiter+=1
    
b7 = Button(text='    ', font="Arial 20", command=c7)
b7.grid(row=3, column=3)

def c8():
    global b8, waiter
    if clear[7] == 0:
        b8.config(text = num[7])
        waiter+=1
    
b8 = Button(text='    ', font="Arial 20", command=c8)
b8.grid(row=3, column=4)

def c9():
    global b9, waiter
    if clear[8] == 0:
        b9.config(text = num[8])
        waiter+=1
    
b9 = Button(text='    ', font="Arial 20", command=c9)
b9.grid(row=4, column=1)

def c10():
    global b10, waiter
    if clear[9] == 0:
        b10.config(text = num[9])
        waiter+=1
    
b10 = Button(text='    ', font="Arial 20", command=c10)
b10.grid(row=4, column=2)

def c11():
    global b11, waiter
    if clear[10] == 0:
        b11.config(text = num[10])
        waiter+=1
    
b11 = Button(text='    ', font="Arial 20", command=c11)
b11.grid(row=4, column=3)

def c12():
    global b12, waiter
    if clear[11] == 0:
        b12.config(text = num[11])
        waiter+=1
    
b12 = Button(text='    ', font="Arial 20", command=c12)
b12.grid(row=4, column=4)

def c13():
    global b13, waiter
    if clear[12] == 0:
        b13.config(text = num[12])
        waiter+=1
    
b13 = Button(text='    ', font="Arial 20", command=c13)
b13.grid(row=5, column=1)

def c14():
    global b14, waiter
    if clear[13] == 0:
        b14.config(text = num[13])
        waiter+=1
    
b14 = Button(text='    ', font="Arial 20", command=c14)
b14.grid(row=5, column=2)

def c15():
    global b15, waiter
    if clear[14] == 0:
        b15.config(text = num[14])
        waiter+=1
    
b15 = Button(text='    ', font="Arial 20", command=c15)
b15.grid(row=5, column=3)

def c16():
    global b16, waiter
    if clear[15] == 0:
        b16.config(text = num[15])
        waiter+=1
    
b16 = Button(text='    ', font="Arial 20", command=c16)
b16.grid(row=5, column=4)

def cclear():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b21, b13, b14, b15, b16
    b1.config(text='    ')
    b2.config(text='    ')
    b3.config(text='    ')
    b4.config(text='    ')
    b5.config(text='    ')
    b6.config(text='    ')
    b7.config(text='    ')
    b8.config(text='    ')
    b9.config(text='    ')
    b10.config(text='    ')
    b11.config(text='    ')
    b12.config(text='    ')
    b13.config(text='    ')
    b14.config(text='    ')
    b15.config(text='    ')
    b16.config(text='    ')

    
mainloop()

while True:
    if waiter == 2:
        sleep(1)
        cclear()
        waiter = 0


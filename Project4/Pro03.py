from tkinter import *

def checkrect():
    global shape, fill
    shape = False
    draw(shape, fill)
def checkoval():
    global shape, fill
    shape = True
    draw(shape,fill)
def draw(shape, fill):
    rect = canvas.create_rectangle(0, 0, 400, 130, fill="White")
    if shape:
        if fill:
            rect = canvas.create_oval(40, 20, 360, 100, fill="black", width=1)
        else:
            rect = canvas.create_oval(40, 20, 360, 100, width=1)
    else:
        if fill:
            rect = canvas.create_rectangle(40, 20, 360, 100, fill="black", width=1)
        else:
            rect = canvas.create_rectangle(40, 20, 360, 100, width=1)
def checkfill():
    global shape, fill
    if fill:
        fill = False
    else:
        fill = True
    draw(shape, fill)


window = Tk()
window.geometry("400x150+400+400")
window.resizable(False, False)

fill = False
shape = False
radVar = IntVar()
canvas = Canvas(window, width = 400, height = 120, relief = "solid", bd = 2, background = 'white')
canvas.pack()

radio1 = Radiobutton(window, text = "직사각형", command = checkrect, variable = radVar, value = 1)
radio1.pack(side = LEFT)
radio2 = Radiobutton(window, text = "타원", command = checkoval, variable = radVar, value = 2)
radio2.pack(side = LEFT)
check = Checkbutton(window, text = "채우기", command = checkfill)
check.pack(side = LEFT)

window.mainloop()
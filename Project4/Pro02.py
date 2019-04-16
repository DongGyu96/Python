from tkinter import *

def process():
    money = float(Input1.get())
    day = float(Input2.get())
    rate = float(Input3.get())
    result = (money * (1 + rate)**(day*12)) // 1
    label5 = Label(window, text = result)
    label5.grid(row = 3, column = 1)

window = Tk()
window.title("투자금 계산기")
window.geometry("200x110+400+400")
window.resizable(False, False)


label1 = Label(window, text = "투자금")
label2 = Label(window, text = "기간")
label3 = Label(window, text = "월이율")
label4 = Label(window, text = "미래가치")

Input1 = Entry(window)
Input2 = Entry(window)
Input3 = Entry(window)
button = Button(window, text = "계산하기", command = process)

label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)
label3.grid(row = 2, column = 0)
label4.grid(row = 3, column = 0)
Input1.grid(row = 0, column = 1)
Input2.grid(row = 1, column = 1)
Input3.grid(row = 2, column = 1)
button.grid(row = 4)

window.mainloop()
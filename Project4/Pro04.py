from tkinter import *
import random

def MakeStr():
    str = []
    word = []
    for i in range(1000):
        str.append(chr(random.randrange(97, 123)))
    for i in range(26):
        word.append(str.count(chr(97 + i)))
    draw(word)

def draw(word):
    global canvas
    canvas.create_rectangle(0, 0, 530, 250, fill = "White")
    for i in range(26):
        canvas.create_rectangle((i * 20) + 4, 240, ((i + 1) * 20) + 4, 240 - (word[i] * 3), width = 1)
        canvas.create_text((i * 20) + 14, 230 - (word[i] * 3), text = word[i])

window = Tk()
window.title("문자의 개수 세기")
window.geometry("530x300+400+400")
window.resizable(False, False)

canvas = Canvas(window, width = 530, height = 240, relief = "solid", bd = 1, background = 'white')
canvas.pack()

for i in range(26):
    label = Label(window, text = chr(97 + i))
    label.place(x = 10 + (i * 20), y = 244)

button = Button(window, text = "히스토그램 출력", command = MakeStr)
button.pack(side = BOTTOM)

window.mainloop()
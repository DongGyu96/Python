from tkinter import *
import random

def MakeNum():
    global key, count, search
    key = -1
    count = -1
    num = []
    for i in range(20):
        num.append(random.randrange(5, 40))
    draw(num)
    return num
def ReNum():
    global key, count, search
    key = -1
    count = -1
    for i in range(20):
        num[i] = random.randrange(5, 40)
    draw(num)
def draw(num):
    global canvas, count
    canvas.create_rectangle(0, 0, 530, 250, fill = "White")
    for i in range(20):
        if i == count:
            if num[i] == key:
                canvas.create_rectangle((i * 25) + 10, 240, ((i + 1) * 25) + 10, 240 - (num[i] * 3), fill="orange",
                                        width=1)
                canvas.create_text((i * 25) + 22, 230 - (num[i] * 3), text=num[i])
            else:
                canvas.create_rectangle((i * 25) + 10, 240, ((i + 1) * 25) + 10, 240 - (num[i] * 3), fill="black",
                                        width=1)
                canvas.create_text((i * 25) + 22, 230 - (num[i] * 3), text=num[i])
        else:
            canvas.create_rectangle((i * 25) + 10, 240, ((i + 1) * 25) + 10, 240 - (num[i] * 3), width=1)
            canvas.create_text((i * 25) + 22, 230 - (num[i] * 3), text=num[i])
def Search():
    global key, count, num, state
    try:
        key = float(input.get())
    except:
        key = -1
    if not key == -1:
        if count < 20:
            count += 1
        draw(num)

window = Tk()
window.title("선형 검색 애니메이션")
window.geometry("530x300+400+400")
window.resizable(False, False)
key = -1
count = -1
canvas = Canvas(window, width = 530, height = 240, relief = "solid", bd = 1, background = 'white')
canvas.pack()
num = MakeNum()

label = Label(window, text = "키를 입력하세요 : ");
input = Entry(window)
button = Button(window, text = "다음단계", command = Search)
button2 = Button(window, text = "재설정", command = ReNum)
label.pack(side = LEFT)
input.pack(side = LEFT)
button.pack(side = LEFT)
button2.pack(side = LEFT)

window.mainloop()
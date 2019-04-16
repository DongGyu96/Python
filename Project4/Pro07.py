from tkinter import *
import random

def MakeNum():
    global count
    count = -1
    num = []
    for i in range(20):
        num.append(random.randrange(5, 70))
    draw(num, -1)
    return num
def ReNum():
    global count
    count = -1
    for i in range(20):
        num[i] = random.randrange(5, 40)
    draw(num, -1)
def draw(num, key):
    global canvas, count
    canvas.create_rectangle(0, 0, 530, 250, fill = "White")
    for i in range(20):
        if i == key:
            canvas.create_rectangle((i * 25) + 10, 240, ((i + 1) * 25) + 10, 240 - (num[i] * 3), fill="black",
                                    width=1)
            canvas.create_text((i * 25) + 22, 230 - (num[i] * 3), text=num[i])
        else:
            canvas.create_rectangle((i * 25) + 10, 240, ((i + 1) * 25) + 10, 240 - (num[i] * 3), width=1)
            canvas.create_text((i * 25) + 22, 230 - (num[i] * 3), text=num[i])
def Search():
    global count, num, state
    key = 0
    search = False
    for i in range(0, count - 1):
        least = i;
        for j in range(i + 1, count):
            if num[j] < num[least]:
                least = j
        if not i == least:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
            key = j
            search = True

    if count < 20:
        count += 1
    if search:
        draw(num, key)
    else:
        draw(num, count)

window = Tk()
window.title("선택 정렬 애니메이션")
window.geometry("530x300+400+400")
window.resizable(False, False)

count = -1
canvas = Canvas(window, width = 530, height = 240, relief = "solid", bd = 1, background = 'white')
canvas.pack()
num = MakeNum()

button = Button(window, text = "다음단계", command = Search)
button2 = Button(window, text = "재설정", command = ReNum)

button.pack(side = LEFT)
button2.pack(side = LEFT)

window.mainloop()
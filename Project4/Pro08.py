from tkinter import *
import tkinter.messagebox
import random

def Shuffle(arr):
    for i in range(500):
        x = random.randrange(0, 52)
        y = random.randrange(0, 52)
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
    return arr

def Draw():
    global image, label, key
    key = Shuffle(key)
    image = []
    label = []
    for i in range(4):
        image.append(PhotoImage(file="image/" + str(key[i]) + ".gif"))
        label.append(Label(window, image=image[i]))
    for i in range(4):
        label[i].place(x=i * 75, y=25)

def ToInt(list):
    size = len(list)
    num = 0
    for i in range(len(list)):
        num += int(list[i]) * (10 ** (size - i - 1))
    return num

def Result():
    global key
    arr = answer.get()
    str = []
    for i in range(len(arr)):
        if not arr[i] == " ":
            str.append(arr[i])
    list = []
    operate = []
    x = 0
    while 1:
        temp = []
        for i in range(x, len(str)):
            if str[i] == "!":
                continue
            elif str[i] == "+":
                operate.append(str[i])
                x = i + 1
                break
            elif str[i] == "-":
                operate.append(str[i])
                x = i + 1
                break
            elif str[i] == "*":
                operate.append(str[i])
                x = i + 1
                break
            elif str[i] == "/":
                operate.append(str[i])
                x = i + 1
                break
            elif str[i] == "(":
                x = i + 1
                break
            elif str[i] == ")":
                x = i + 1
                break
            else:
                temp.append(str[i])
                str[i] = "!"
        if not temp == []:
            list.append(ToInt(temp))
        if(len(list) == 4):
            break
    print(list)
    result = list[0]
    for i in range(3):
        if operate[i] == "+":
            result += list[i + 1]
        elif operate[i] == "-":
            result -= list[i + 1]
        elif operate[i] == "*":
            result *= list[i + 1]
        elif operate[i] == "/":
            result /= list[i + 1]
    if result == 24:
        for i in range(4):
            number = key[i] % 13
            if number == 0:
                number = 13
            if not number in list:
                tkinter.messagebox.showerror("틀림", "보여지는 카드를 사용해야 합니다")
                return
        tkinter.messagebox.showinfo("정답", "맞았습니다")
    elif not result == 24:
        for i in range(4):
            number = key[i] % 13
            if number == 0:
                number = 13
            if not number in list:
                tkinter.messagebox.showerror("틀림", "보여지는 카드를 사용해야 합니다")
                return
        tkinter.messagebox.showerror("틀림", arr + "은/는 24가 아닙니다.")




key = []
for i in range(52):
    key.append(i + 1)

key = Shuffle(key)
window = Tk()
window.title("24점 게임")
window.geometry("300x150+400+400")
window.resizable(False, False)


refresh = Button(window, text = "새로고침", command = Draw)
refresh.pack(side = TOP)

image = []
label = []
for i in range(4):
    image.append(PhotoImage(file = "image/" + str(key[i]) + ".gif"))
    label.append(Label(window, image = image[i]))
for i in range(4):
    label[i].place(x = i * 75, y = 25)

info = Label(window, text = "수식을 입력하세요:")
info.place(x = 0, y = 125)
answer = Entry(window, width = 21)
answer.place(x = 110, y = 125)
action = Button(window, text = "확인", command = Result)
action.place(x = 262, y = 123)
window.mainloop()

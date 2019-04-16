import urllib.request
from tkinter import *

def Func():
    url = urllib.request.urlopen(input.get())
    data = url.read().decode("utf-8")
    histogram = []
    for i in range(26):
        histogram.append(0)

    new = data.lower()
    for c in new:
        if ord(c) >= 97 and ord(c) <= 122:
            histogram[ord(c) - ord('a')] += 1
    maxCount = max(histogram)
    barW = (500 - 20) / 26

    for i in range(26):
        canvas.create_rectangle(10 + (i * barW), 300 - (290 - 10) * histogram[i] / maxCount - 15, 10 + ((i + 1) * barW),
                                300 - 15)
        canvas.create_text(10 + i * barW + 8, 300 - 10 + 5, text=chr(i + ord('a')))


window = Tk()
window.title("URL에 포함된 문자의 출현 빈도수 히스토그램")
window.geometry("500x350+400+400")
window.resizable(False, False)

canvas = Canvas(window, width = 600, height = 300, background = "white")
canvas.pack()

label = Label(window, text = "URL을 입력하세요 : ")
label.pack(side=LEFT)
input = Entry(window, width = 40)
input.pack(side = LEFT)
button = Button(window, text = "결과 보기", command = Func)
button.pack(side = LEFT)

window.mainloop()
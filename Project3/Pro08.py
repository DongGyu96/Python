from tkinter import *
from tkinter import filedialog
from tkinter import font

def Open():
    global window, RenderFileName
    RenderFileName.config(state="normal")
    window.dirName = filedialog.askopenfilename(initialdir='C:/', title='select file',
                                                filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    RenderFileName.insert(INSERT, window.dirName)
    RenderFileName.config(state="disabled")

def Render():
    global window, RenderText
    RenderText.config(state='normal')
    f = open(window.dirName, 'r')
    lines = f.readlines()
    word = []
    for i in range(26):
        word.append(0)

    for line in lines:
        for i in range(26):
            word[i] += line.count(chr(65 + i))
            word[i] += line.count(chr(97 + i))

    for i in range(26):
        RenderText.insert(INSERT, chr(97 + i))
        RenderText.insert(INSERT, " - ")
        RenderText.insert(INSERT, word[i])
        RenderText.insert(INSERT, "번 나타납니다")
        RenderText.insert(INSERT, '\n')
    f.close()

window = Tk()
window.geometry("500x260")

frame1 = Frame(window)
frame2 = Frame(window)
RenderTextScrollbar = Scrollbar(frame1)

TempFont = font.Font(frame1, size = 12, family = 'Consolas')

RenderText = Text(frame1, font = TempFont, width = 48, height = 11, borderwidth = 4,
                  relief = 'ridge', yscrollcommand = RenderTextScrollbar.set)

TempFont = font.Font(frame2, size = 10, family = 'Consolas')
label = Label(frame2, font = TempFont, text = "파일명을 입력하세요:")
TempFont = font.Font(frame2, size = 12, family = 'Consolas')
RenderFileName = Text(frame2, font = TempFont, width = 25, height = 1, borderwidth = 3)

button1 = Button(frame2, text = "열기", borderwidth = 2, command = Open)
button2 = Button(frame2, text = "결과보기", command = Render)

RenderText.pack()
RenderText.place(x=0, y=0)
RenderText.config(state = 'disabled')
RenderTextScrollbar.place(x = 450, y = 100)
RenderTextScrollbar.pack(side = RIGHT, fill = BOTH)
RenderTextScrollbar.config(command = RenderText.yview)
frame1.pack(ipadx = 220, ipady = 85, padx = 0, pady = 0, side = TOP)

label.pack(side = LEFT)
label.place(x=5, y=6)
RenderFileName.pack(side = TOP)
RenderFileName.place(x=145,y=5)
button1.pack()
button1.place(x = 380, y = 5)
button2.pack()
button2.place(x = 415, y = 5)
frame2.pack(ipady = 35, fill = BOTH)

window.mainloop()

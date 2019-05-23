from tkinter import *
import tkinter.messagebox
from ReadData import *

class RankingGraph:
    def __init__(self, window, type, Data):
        #self.menubar = Menu(window)
        #self.menu1 = Menu(self.menubar, tearoff=0)
        #self.menu1.add_command(label='하위메뉴 1-1')
        #self.menu1.add_separator()
        #self.menu1.add_command(label='1-2')
        #self.menubar.add_cascade(label='상위메뉴 1', menu=self.menu1)

        #self.GraphFrame = Toplevel(window, menu=self.menubar)
        self.GraphFrame = Toplevel(window)
        self.GraphFrame.geometry("800x400+800+400")
        self.GraphFrame.resizable(False, False)
        self.GraphFrame.title(Data.find("showrange").string + " 박스오피스 랭킹 그래프")

        self.Canvas = Canvas(self.GraphFrame, width=800, height=350, background='light blue')
        self.Canvas.create_line(0, 350, 30, 320, width=1)
        self.Canvas.create_line(30, 320, 30, 0, width=1)
        self.Canvas.create_line(30, 320, 830, 320, width=1)
        #self.Canvas.create_line(770, 320, 800, 350, width=1)
        #self.Canvas.create_line(770, 320, 770, 0, width=1)
        self.Canvas.create_line(0, 350, 800, 350, width=5)

        if type == DAILY:
            typename = "dailyboxoffice"
        else:
            typename = "weeklyboxoffice"
        self.labels = []
        self.value = []
        self.count = 0
        for data in Data.find_all(typename):
            if self.count == 0:
                self.labels.append(Label(self.GraphFrame, font=("HYHeadLine", 11, "bold"), text=str(self.count + 1) + "위", fg = "gold2"))
                MaxValue = Value(data.audicnt.string, data.audiinten.string, data.audiacc.string)
            elif self.count < 2:
                self.labels.append(Label(self.GraphFrame, font=("HYHeadLine", 11, "bold"), text=str(self.count + 1) + "위", fg = "SlateGray3"))
            elif self.count < 3:
                self.labels.append(Label(self.GraphFrame, font=("HYHeadLine", 11, "bold"), text=str(self.count + 1) + "위", fg = "tan1"))
            else:
                self.labels.append(Label(self.GraphFrame, font=("HYHeadLine", 11, "bold"), text=str(self.count + 1) + "위",fg="black"))
            self.labels[self.count].bind("<Button-1>", lambda event = "마우스값", Data = data : ShowMovieName(event, Data))
            self.value.append(Value(data.audicnt.string, data.audiinten.string, data.audiacc.string))
            self.count += 1

        for data in self.value:
            if data.today > MaxValue.today:
                MaxValue.today = data.today
            if data.totalday > MaxValue.totalday:
                MaxValue.totalday = data.totalday
            if data.prevday > MaxValue.prevday:
                MaxValue.prevday = data.prevday

        for i in range(self.count):
            color = 'gray'
            height = (self.value[i].totalday - self.value[i].today) / MaxValue.totalday * 320
            self.Canvas.create_rectangle(30 + (i * 75), 340, 45 + (i * 75), 340 - height, fill=color)
            self.Canvas.create_polygon(30 + (i * 75), 340 - height, 40 + (i * 75), 340 - height - 10,
                                       55 + (i * 75), 340 - height - 10, 45 + (i * 75), 340 - height, fill=color,
                                       outline="black")
            self.Canvas.create_polygon(55 + (i * 75), 340 - height - 10, 55 + (i * 75), 330,
                                       45 + (i * 75), 340, 45 + (i * 75), 340 - height, fill=color,
                                       outline="black")

            color = "SteelBlue3"
            startheight = height
            height = self.value[i].today / MaxValue.totalday * 320
            self.Canvas.create_rectangle(30 + (i * 75), 340 - startheight, 45 + (i * 75), 340 - height - startheight, fill=color)
            self.Canvas.create_polygon(30 + (i * 75), 340 - height - startheight, 40 + (i * 75), 340 - height - 10 - startheight,
                                       55 + (i * 75), 340 - height - 10 - startheight, 45 + (i * 75), 340 - height - startheight, fill=color,
                                       outline="black")
            self.Canvas.create_polygon(55 + (i * 75), 340 - height - 10 - startheight, 55 + (i * 75), 330 - startheight,
                                       45 + (i * 75), 340 - startheight, 45 + (i * 75), 340 - height - startheight, fill=color,
                                       outline="black")

            color = "SteelBlue1"
            height = self.value[i].today / MaxValue.today * 150
            self.Canvas.create_rectangle(45 + (i * 75), 340, 60 + (i * 75), 340 - height, fill=color)
            self.Canvas.create_polygon(45 + (i * 75), 340 - height, 55 + (i * 75), 340 - height - 10,
                                       70 + (i * 75), 340 - height - 10, 60 + (i * 75), 340 - height, fill=color,
                                       outline="black")
            self.Canvas.create_polygon(70 + (i * 75), 340 - height - 10, 70 + (i * 75), 330,
                                       60 + (i * 75), 340, 60 + (i * 75), 340 - height, fill=color,
                                       outline="black")

            if self.value[i].increment == self.value[i].today:
                height = 1
            else:
                height = self.value[i].increment / MaxValue.today * 150
            if height < 0:
                height = height * -1
                color = "orange"
            else:
                color = "cyan"
            self.Canvas.create_rectangle(60 + (i * 75), 340, 75 + (i * 75), 340 - height, fill=color)
            self.Canvas.create_polygon(60 + (i * 75), 340 - height, 70 + (i * 75), 340 - height - 10,
                                       85 + (i * 75), 340 - height - 10, 75 + (i * 75), 340 - height, fill=color,
                                       outline="black")
            self.Canvas.create_polygon(85 + (i * 75), 340 - height - 10, 85 + (i * 75), 330,
                                       75 + (i * 75), 340, 75 + (i * 75), 340 - height, fill=color,
                                       outline="black")

        self.Canvas.create_rectangle(685, 0, 800, 105, fill="white", outline = "black", width = 1)

        self.Canvas.create_rectangle(700, 5, 710, 25, fill = "gray")
        self.Canvas.create_rectangle(700, 30, 710, 50, fill="steel blue3")
        self.Canvas.create_rectangle(700, 55, 710, 75, fill="steel blue1")
        self.Canvas.create_rectangle(700, 80, 710, 100, fill="cyan")
        self.Canvas.create_rectangle(688, 80, 698, 100, fill="orange")

        self.Canvas.create_text(750, 12, font = ("Impact", 8), text = "총 관객수")
        self.Canvas.create_text(750, 38, font = ("Impact", 8), text="전체 대비 당일")
        self.Canvas.create_text(750, 65, font = ("Impact", 8), text="당일 관객수")
        self.Canvas.create_text(750, 90, font = ("Impact", 8), text="당일 대비 전날")

        self.Canvas.create_line(0, 2, 800, 2, width=5)

        self.RenderGraph()

    def RenderGraph(self):
        self.Canvas.pack()
        i = 0
        for data in self.labels:
            data.place(x = 40 + (i * 75), y = 355)
            i += 1

def ShowMovieName(event, Data):
    data = Data.rank.string + "위" + "\n"
    data = data + "영화 제목 :\t" + Data.movienm.string + "\n"
    data = data + "개봉일 :\t\t" + Data.opendt.string + "\n"
    data = data + "당일 관람객 :\t" + Data.audicnt.string + "\n"
    data = data + "전 일/주 대비 :\t" + Data.audiinten.string + "\n"
    data = data + "총관람객 :\t" + Data.audiacc.string + "\n"
    tkinter.messagebox.showinfo("영화 정보", data)

class Value:
    def __init__(self, today, prevday, totalday):
        self.today = eval(today)
        self.prevday = eval(today) - eval(prevday)
        self.totalday = eval(totalday)
        self.increment = eval(prevday)

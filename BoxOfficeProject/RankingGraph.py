from tkinter import *
from ReadData import *

class RankingGraph:
    def __init__(self, window, type, Data):
        self.menubar = Menu(window)
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label='하위메뉴 1-1')
        self.menu1.add_separator()
        self.menu1.add_command(label='1-2')
        self.menubar.add_cascade(label='상위메뉴 1', menu=self.menu1)

        self.GraphFrame = Toplevel(window, menu=self.menubar)
        self.GraphFrame.geometry("800x400+800+400")
        self.GraphFrame.resizable(False, False)
        self.GraphFrame.title("Ranking Graph")

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
                color = "red"
            else:
                color = "cyan"
            self.Canvas.create_rectangle(60 + (i * 75), 340, 75 + (i * 75), 340 - height, fill=color)
            self.Canvas.create_polygon(60 + (i * 75), 340 - height, 70 + (i * 75), 340 - height - 10,
                                       85 + (i * 75), 340 - height - 10, 75 + (i * 75), 340 - height, fill=color,
                                       outline="black")
            self.Canvas.create_polygon(85 + (i * 75), 340 - height - 10, 85 + (i * 75), 330,
                                       75 + (i * 75), 340, 75 + (i * 75), 340 - height, fill=color,
                                       outline="black")

        self.Canvas.create_line(0, 2, 800, 2, width=5)
        self.RenderGraph()

    def RenderGraph(self):
        self.Canvas.pack()
        i = 0
        for data in self.labels:
            data.place(x = 40 + (i * 75), y = 355)
            i += 1

class Value:
    def __init__(self, today, prevday, totalday):
        self.today = eval(today)
        self.prevday = eval(today) - eval(prevday)
        self.totalday = eval(totalday)
        self.increment = eval(prevday)
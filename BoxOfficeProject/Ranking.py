from tkinter import *
from tkinter.font import *
from ReadData import *

class Ranking():
    def __init__(self, window, width, height):
        self.boxofficeimage = PhotoImage(file="image/Ranking2.png")
        self.BoxofficeData = None
        self.boxofficetype = None

        self.startrank = 1
        self.date = 0
        self.RankingFrame = Frame(window, bd=2, relief="solid")
        self.rankframe = []
        self.rankcanvas = []
        for i in range(3):
            self.rankframe.append(Frame(self.RankingFrame, width=266, height=316,
                                        bd=4, relief="ridge"))
            self.rankcanvas.append(Canvas(self.RankingFrame, width=250, height=300, bd=2, relief="solid"))
            self.rankcanvas[i].create_rectangle(0, 0, 255, 305, fill="light yellow")
        self.frametitle = Frame(self.RankingFrame, width=400, height=80)
        self.boxofficelabel = Label(self.frametitle, image=self.boxofficeimage)

        self.frameranking1 = Frame(self.RankingFrame, width=480, height=110)

        self.font = Font(family="맑은 고딕", size=13, weight="bold")
        self.ranktypebox = Listbox(self.frameranking1, font=self.font, width=5, height=2,
                                   borderwidth=3, relief="ridge")

        self.ranktypebox.insert(0, "일간")
        self.ranktypebox.insert(1, "주간")
        self.ranktypebox.activate(0)

        self.font = Font(family="맑은 고딕", size=12, weight="bold")
        self.yearbox = Spinbox(self.frameranking1, font=self.font, width=5, borderwidth=3, relief="ridge",
                               to=2019, from_=2004)
        self.monthbox = Spinbox(self.frameranking1, font=self.font, width=5, borderwidth=3, relief="ridge",
                                from_=1, to=12)
        self.daybox = Spinbox(self.frameranking1, font=self.font, width=5, borderwidth=3, relief="ridge",
                              from_=1, to=31)
        self.font = Font(family="맑은 고딕", size=15, weight="bold")
        self.ranktypelabel = Label(self.frameranking1, font=self.font, text="분류")
        self.yearlabel = Label(self.frameranking1, font=self.font, text="연도")
        self.monthlabel = Label(self.frameranking1, font=self.font, text="달")
        self.daylabel = Label(self.frameranking1, font=self.font, text="일")

        self.setrankbutton = Button(self.frameranking1, font=self.font, text="갱신",
                                    command=lambda set=True: self.SetRanking(set))
        # command = lambda index = i: func(index)
        self.datelabel = Label(self.frameranking1, font=self.font, text=" ")
        self.nextrankingbutton = Button(self.frameranking1, font=("consolas", 10, "bold"), text="다음 페이지",
                                        command=self.NextRanking)
        self.prevrankingbutton = Button(self.frameranking1, font=("consolas", 10, "bold"), text="이전 페이지",
                                        command=self.PrevRanking)
        # self.BoxofficeData = LoadXMLFromBoxofficeData(self.boxofficetype, self.date);

    def SetRanking(self, set):
        self.boxofficetype = self.ranktypebox.curselection()
        if int(self.monthbox.get()) < 10:
            month = "0" + self.monthbox.get()
        else:
            month = self.monthbox.get()
        if int(self.daybox.get()) < 10:
            day = "0" + self.daybox.get()
        else:
            day = self.daybox.get()
        self.date = self.yearbox.get() + month + day
        if set:
            self.startrank = 1
            self.BoxofficeData = LoadXMLFromFileBoxOffice(self.boxofficetype, self.date)

        self.datelabel = Label(self.RankingFrame, font = ("Bernard MT", 22, "bold"), text = self.BoxofficeData.showrange.string)
        self.RenderRanking()
        self.Render()

    def RenderRanking(self):
        if self.boxofficetype == DAILY:
            typename = "dailyboxoffice"
        else:
            typename = "weeklyboxoffice"
        max = 0
        for data in self.BoxofficeData.find_all(typename):
            if max < int(data.rank.string):
                max = int(data.rank.string)
        for i in range(3):
            for data in self.BoxofficeData.find_all(typename):
                if i + self.startrank > max:
                    self.startrank -= max
                if i + self.startrank == int(data.rank.string):
                    self.rankcanvas[i].create_rectangle(0, 0, 255, 305, fill="light yellow")
                    font = Font(size=42, family="Impact", weight="bold", slant="italic", underline=True)
                    rank = data.rank.string + "."
                    if data.rank.string == "1":
                        self.rankcanvas[i].create_text(30, 35, font=font, text=rank, fill="goldenrod1")
                    else:
                        self.rankcanvas[i].create_text(30, 35, font=font, text=rank, fill="gray1")
                    titlecolor = "black"
                    if len(data.movienm.string) < 6:
                        self.rankcanvas[i].create_text(150, 40, font=("Impact", 28, "bold"), text=data.movienm.string, fill = titlecolor)
                    elif len(data.movienm.string) < 8:
                        self.rankcanvas[i].create_text(155, 45, font=("Impact", 22, "bold"), text=data.movienm.string, fill = titlecolor)
                    elif len(data.movienm.string) < 11:
                        self.rankcanvas[i].create_text(155, 50, font=("Impact", 18, "bold"), text=data.movienm.string, fill = titlecolor)
                    elif len(data.movienm.string) < 13:
                        self.rankcanvas[i].create_text(155, 50, font=("Impact", 15, "bold"), text=data.movienm.string, fill = titlecolor)
                    elif len(data.movienm.string) < 18:
                        self.rankcanvas[i].create_text(150, 22, font=("Impact", 20, "bold"), text=data.movienm.string[:7], fill = titlecolor)
                        self.rankcanvas[i].create_text(150, 50, font=("Impact", 20, "bold"), text=data.movienm.string[7:], fill = titlecolor)
                    else:
                        self.rankcanvas[i].create_text(150, 25, font=("Impact", 14, "bold"), text=data.movienm.string[:10], fill = titlecolor)
                        self.rankcanvas[i].create_text(150, 50, font=("Impact", 14, "bold"), text=data.movienm.string[10:], fill = titlecolor)
                    # ===제목===========================================================================
                    if int(data.rankinten.string) < 0:
                        self.rankcanvas[i].create_text(30, 75, font=("Impact", 12), text=data.rankinten.string, fill = "red")
                    elif int(data.rankinten.string) > 0:
                        self.rankcanvas[i].create_text(30, 75, font=("Impact", 12), text="+" + data.rankinten.string, fill="blue")
                    # ===순위등락========================================================================
                    self.rankcanvas[i].create_text(200, 80, font = ("Impact", 14), text = data.opendt.string)
                    self.rankcanvas[i].create_line(10, 100, 245, 100)
                    # ===개봉일==========================================================================
                    self.rankcanvas[i].create_text(30, 210, font=("HYHeadLine", 14, "bold"), text="당일")
                    self.rankcanvas[i].create_text(200, 210, font=("Impact", 14), text="+" + data.audicnt.string, fill="steel blue")
                    self.rankcanvas[i].create_text(50, 235, font=("HYHeadLine", 14, "bold"), text="전일 대비")
                    if int(data.audiinten.string) < 0:
                        self.rankcanvas[i].create_text(200, 235, font=("Impact", 14), text=data.audiinten.string, fill="red")
                    else:
                        self.rankcanvas[i].create_text(200, 235, font=("Impact", 14), text="+" + data.audiinten.string, fill="light blue4")
                    self.rankcanvas[i].create_text(70, 260, font=("HYHeadLine", 16, "bold"), text="누적 관객수 -")
                    self.rankcanvas[i].create_text(200, 260, font = ("Impact", 16), text = data.audiacc.string)
                    self.rankcanvas[i].create_line(10, 280, 245, 280)
                    # ===관객수===========================================================================
                    self.rankcanvas[i].create_text(30, 120, font=("HYHeadLine", 14, "bold"), text="당일")
                    self.rankcanvas[i].create_text(190, 120, font=("Impact", 14), text="+" + data.salesamt.string,fill="steel blue")
                    self.rankcanvas[i].create_text(50, 145, font=("HYHeadLine", 14, "bold"), text="전일 대비")
                    if int(data.salesinten.string) < 0:
                        self.rankcanvas[i].create_text(190, 145, font=("Impact", 14), text=data.salesinten.string, fill="red")
                    else:
                        self.rankcanvas[i].create_text(190, 145, font=("Impact", 14), text="+" + data.salesinten.string, fill="light blue4")
                    self.rankcanvas[i].create_text(65, 170, font=("HYHeadLine", 16, "bold"), text="누적 매출액")
                    self.rankcanvas[i].create_text(190, 170, font=("Impact", 16), text=data.salesacc.string)
                    self.rankcanvas[i].create_line(10, 190, 245, 190)

    def Render(self):
        for i in range(3):
            self.rankframe[i].place(x = (i * 300) + 15, y = 145)
            self.rankcanvas[i].place(x= (i * 300) + 20, y = 150)
        self.frametitle.place(x = 10, y = 10)
        self.frameranking1.place(x = 420, y = 0)
        self.ranktypebox.place(x = 0, y = 35)
        self.yearbox.place(x = 70, y = 35)
        self.monthbox.place(x = 150, y = 35)
        self.daybox.place(x = 230, y = 35)
        self.ranktypelabel.place(x = 5, y = 0)
        self.yearlabel.place(x = 80, y = 0)
        self.monthlabel.place(x = 180, y = 0)
        self.daylabel.place(x = 260, y = 0)
        self.setrankbutton.place(x = 310, y = 35)
        self.boxofficelabel.pack()
        self.datelabel.place(x = 20, y = 100)
        self.nextrankingbutton.place(x = 200, y = 70)
        self.prevrankingbutton.place(x=100, y=70)

    def NextRanking(self):
        if not self.BoxofficeData == None:
            self.startrank += 1
            self.SetRanking(False)
    def PrevRanking(self):
        if not self.BoxofficeData == None:
            if self.startrank > 1:
                self.startrank -= 1
            self.SetRanking(False)

    def GetFrame(self):
        return self.RankingFrame
from tkinter import *
from tkinter.font import *
from ReadData import *
from RankingGraph import *

class Ranking():
    def __init__(self, window, width, height):
        self.boxofficeimage = PhotoImage(file="image/Ranking3.png")
        self.nextbuttonImage = PhotoImage(file='image/Button/NextPageIcon1.png')
        self.prevbuttonImage = PhotoImage(file='image/Button/PrevPageIcon1.png')
        self.searchImage = PhotoImage(file = 'image/SearchIcon.png')
        self.rankImage = PhotoImage(file = 'image/RankingIcon.png')
        self.BoxofficeData = None
        self.boxofficetype = None
        self.Graph = None
        self.startrank = 1
        self.date = 0
        framecolor = "azure"
        self.RankingFrame = Frame(window, bd=2, relief="solid", background = framecolor)
        self.rankframe = []
        self.rankcanvas = []
        for i in range(3):
            self.rankframe.append(Frame(self.RankingFrame, width=266, height=316,
                                        bd=4, relief="ridge", background = framecolor))
            self.rankcanvas.append(Canvas(self.RankingFrame, width=250, height=300, bd=2, relief="solid"))
            self.rankcanvas[i].create_rectangle(0, 0, 255, 305, fill="light blue")
        self.frametitle = Frame(self.RankingFrame, width=400, height=100, background = framecolor)
        self.boxofficelabel = Label(self.frametitle, image=self.boxofficeimage, bg = "light blue3")

        self.frameranking1 = Frame(self.RankingFrame, width=480, height=110, background = framecolor)

        self.font = Font(family="맑은 고딕", size=13, weight="bold")
        self.ranktypebox = Listbox(self.frameranking1, font=self.font, width=5, height=2,
                                   borderwidth=3, relief="ridge")

        self.ranktypebox.insert(0, "일간")
        self.ranktypebox.insert(1, "주간")
        self.ranktypebox.activate(0)

        self.font = Font(family="맑은 고딕", size=12, weight="bold")
        self.yearbox = Spinbox(self.frameranking1, font=self.font, width=5, borderwidth=3, relief="ridge",
                               to=2019, from_=2005)
        self.monthbox = Spinbox(self.frameranking1, font=self.font, width=5, borderwidth=3, relief="ridge",
                                from_=1, to=12)
        self.daybox = Spinbox(self.frameranking1, font=self.font, width=5, borderwidth=3, relief="ridge",
                              from_=1, to=31)
        self.font = Font(family="맑은 고딕", size=14, weight="bold")
        self.ranktypelabel = Label(self.frameranking1, font=self.font, text="분류", bg = framecolor)
        self.yearlabel = Label(self.frameranking1, font=self.font, text="연도", bg = framecolor)
        self.monthlabel = Label(self.frameranking1, font=self.font, text="달", bg = framecolor)
        self.daylabel = Label(self.frameranking1, font=self.font, text="일", bg = framecolor)

        self.setrankbutton = Button(self.frameranking1, image = self.searchImage, bg = "DodgerBlue4",
                                    command=lambda set=True: self.SetRanking(set))
        # command = lambda index = i: func(index)
        self.datelabel = Label(self.frameranking1, font=self.font, text=" ", bg = framecolor)
        self.nextrankingbutton = Button(self.frameranking1, image = self.nextbuttonImage, bg = "DodgerBlue4",
                                        command=self.NextRanking)
        self.prevrankingbutton = Button(self.frameranking1, image = self.prevbuttonImage, bg = "DodgerBlue4",
                                        command=self.PrevRanking)
        self.creategraphbutton = Button(self.frameranking1, image = self.rankImage, bg = "DodgerBlue4", command = self.CreateGraph)
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

        if self.boxofficetype == DAILY:
            date = self.BoxofficeData.showrange.string[:4] + "년" + self.BoxofficeData.showrange.string[4:6] + "월" +\
                   self.BoxofficeData.showrange.string[6:8] + "일                                          "
        else:
            date = self.BoxofficeData.showrange.string[:4] + "년" + self.BoxofficeData.showrange.string[4:6] + "월" + \
                   self.BoxofficeData.showrange.string[6:8] + "일 "
            date = date + self.BoxofficeData.showrange.string[8:9] + " " + self.BoxofficeData.showrange.string[9:13] + "년" + \
                   self.BoxofficeData.showrange.string[13:15] + "월" + self.BoxofficeData.showrange.string[15:] + "일"

        self.datelabel = Label(self.RankingFrame, font = ("Bernard MT", 22, "bold"), text = date, bg = "azure")
        self.RenderRanking()
        self.Render()

    def RenderRanking(self):
        if self.boxofficetype == DAILY:
            typename = "dailyboxoffice"
        else:
            typename = "weeklyboxoffice"
        for i in range(3):
            for data in self.BoxofficeData.find_all(typename):
                if i + self.startrank == int(data.rank.string):
                    self.rankcanvas[i].create_rectangle(0, 0, 255, 305, fill="light blue")
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
                        self.rankcanvas[i].create_text(150, 50, font=("Impact", 14, "bold"), text=data.movienm.string[10:22], fill = titlecolor)
                    # ===제목===========================================================================
                    if int(data.rankinten.string) < 0:
                        self.rankcanvas[i].create_text(30, 75, font=("Impact", 12), text=data.rankinten.string, fill = "red")
                    elif int(data.rankinten.string) > 0:
                        self.rankcanvas[i].create_text(30, 75, font=("Impact", 12), text="+" + data.rankinten.string, fill="blue")
                    # ===순위등락========================================================================
                    self.rankcanvas[i].create_text(200, 80, font = ("Impact", 14), text = data.opendt.string)
                    # ===개봉일==========================================================================
                    #self.rankcanvas[i].create_line(10, 100, 245, 100)
                    self.rankcanvas[i].create_line(0, 100, 300, 100, width=3)
                    self.rankcanvas[i].create_text(30, 210, font=("HYHeadLine", 14, "bold"), text="당일")
                    self.rankcanvas[i].create_text(200, 210, font=("Impact", 14), text="+" + data.audicnt.string,
                                                   fill="steel blue")
                    self.rankcanvas[i].create_text(50, 235, font=("HYHeadLine", 14, "bold"), text="전일 대비")
                    if int(data.audiinten.string) < 0:
                        self.rankcanvas[i].create_text(200, 235, font=("Impact", 14), text=data.audiinten.string,
                                                       fill="red")
                    else:
                        self.rankcanvas[i].create_text(200, 235, font=("Impact", 14),
                                                       text="+" + data.audiinten.string, fill="light blue4")
                    self.rankcanvas[i].create_text(70, 260, font=("HYHeadLine", 16, "bold"), text="누적 관객수 -")
                    self.rankcanvas[i].create_text(200, 260, font=("Impact", 16), text=data.audiacc.string)
                    self.rankcanvas[i].create_line(10, 280, 245, 280)
                    # ===관객수===========================================================================
                    self.rankcanvas[i].create_text(30, 120, font=("HYHeadLine", 14, "bold"), text="당일")
                    self.rankcanvas[i].create_text(190, 120, font=("Impact", 14), text="+" + data.salesamt.string,
                                                   fill="steel blue")
                    self.rankcanvas[i].create_text(50, 145, font=("HYHeadLine", 14, "bold"), text="전일 대비")
                    if int(data.salesinten.string) < 0:
                        self.rankcanvas[i].create_text(190, 145, font=("Impact", 14), text=data.salesinten.string,
                                                       fill="red")
                    else:
                        self.rankcanvas[i].create_text(190, 145, font=("Impact", 14),
                                                       text="+" + data.salesinten.string, fill="light blue4")
                    self.rankcanvas[i].create_text(65, 170, font=("HYHeadLine", 16, "bold"), text="누적 매출액")
                    self.rankcanvas[i].create_text(190, 170, font=("Impact", 16), text=data.salesacc.string)
                    self.rankcanvas[i].create_line(10, 190, 245, 190)


    def Render(self):
        for i in range(3):
            self.rankframe[i].place(x = (i * 300) + 15, y = 145)
            self.rankcanvas[i].place(x= (i * 300) + 20, y = 150)
        self.frametitle.place(x = 10, y = 5)
        self.frameranking1.place(x = 420, y = 0)
        self.ranktypebox.place(x = 0, y = 30)
        self.yearbox.place(x = 70, y = 27)
        self.monthbox.place(x = 150, y = 27)
        self.daybox.place(x = 230, y = 27)
        self.ranktypelabel.place(x = 5, y = -3)
        self.yearlabel.place(x = 80, y = -3)
        self.monthlabel.place(x = 180, y = -3)
        self.daylabel.place(x = 260, y = -3)
        self.setrankbutton.place(x = 320, y = 10)
        self.boxofficelabel.place(x= 0, y = 0)
        self.datelabel.place(x = 20, y = 100)
        self.nextrankingbutton.place(x = 260, y = 60)
        self.prevrankingbutton.place(x=70, y=60)
        self.creategraphbutton.place(x=395, y = 10)

    def NextRanking(self):
        if not self.BoxofficeData == None:
            if self.startrank < 8:
                self.startrank += 1
                self.SetRanking(False)
    def PrevRanking(self):
        if not self.BoxofficeData == None:
            if self.startrank > 1:
                self.startrank -= 1
                self.SetRanking(False)

    def CreateGraph(self):
        if self.BoxofficeData != None:
            self.Graph = RankingGraph(self.RankingFrame, self.boxofficetype, self.BoxofficeData)

    def GetFrame(self):
        return self.RankingFrame

    def GetRanking(self, list):
        if list[0] == "일간":
            daytype = DAILY
            typename = "dailyboxoffice"
        else:
            daytype = WEEKLY
            typename = "weeklyboxoffice"

        if len(list[1]) != 8:
            return None
        date = list[1]

        telegramData = LoadXMLFromFileBoxOffice(daytype, date)
        boxoffice = []
        boxoffice.append("조회 날짜 : " + telegramData.find("showrange").string)
        for data in telegramData.find_all(typename):
            text = data.rank.string + "위 \n"
            text = text + "영화 제목 : " + data.movienm.string + "\n"
            text = text + "개봉일 : " + data.opendt.string + "\n"
            text = text + "해당 기간 관객수 : " + data.audicnt.string + "\n"
            text = text + "전 일/주 증감분 : " + data.audiinten.string + " (" + data.audichange.string + "%) \n"
            text = text + "누적 관객수 : " + data.audiacc.string + "\n"
            text = text + "누적 매출액 : " + data.salesacc.string + "원 \n"
            text = text + "해당 기간 상영 횟수 : " + data.showcnt.string + "회"
            boxoffice.append(text)
        return boxoffice
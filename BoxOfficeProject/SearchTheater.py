from tkinter import *
from ReadData import *
from TheaterInfo import *

class SearchTheater():
    def __init__(self, window, width, height):
        self.TheaterFrame = Frame(window, width = width, height = height, bd=2, relief="solid", bg = "light blue")
        self.Image = LoadGoogleAPIMapToURL(37.3406, 126.732)
        self.labelImage = PhotoImage(file = 'image/SearchTheaterLabel.png')
        self.TheaterList = []
        Data = LoadXLSFromFileTheater()
        for data in Data.rows:
            if data[THEATERstate].value != "01":
                continue
            else:
                find = False
                for theater in self.TheaterList:
                    if theater.code == data[THEATERx].value:
                        find = True
                        break
                if find == False:
                    if data[THEATERaddress].value == "":
                        address = data[THEATERprevaddress].value
                    else:
                        address = data[THEATERaddress].value
                    self.TheaterList.append(Theater(data[THEATERname].value,
                                                    data[THEATERstartdate].value,
                                                    data[THEATERprevaddress].value,
                                                    data[THEATERcall].value,
                                                    data[THEATERtype].value,
                                                    data[THEATERx].value))
                    # 영화관 593개
        self.SearchFrame1 = Frame(self.TheaterFrame, width = 150, height = height, bd = 2, bg = "RoyalBlue4")
        self.SearchFrame2 = Frame(self.TheaterFrame, width=170, height=height, bd=2, bg="light slate gray")
        self.SearchFrame3 = Frame(self.TheaterFrame, width=200, height=height, bd=2, bg="light slate gray")
        self.MapFrame = Frame(self.TheaterFrame, width = 400, height = height, bg = "light blue", bd = 2)

        #self.searchScrollbar1 = Scrollbar(self.SearchFrame1)
        self.searchState = Listbox(self.SearchFrame1, width = 15, height = height, font = ("HYHeadLine", 16, "bold"),
                                   bg = "light slate gray", fg = "white", exportselection = True, relief = "flat")
        self.searchState.bind("<Double-Button-1>", self.SelectState)

        self.prevSelectState = -1
        #yscrollcommand = self.searchScrollbar1.set
        #self.searchScrollbar1["command"] = self.searchState.yview

        self.searchScrollbar2 = Scrollbar(self.SearchFrame2)
        self.searchCity = Listbox(self.SearchFrame2, width = 12, height=height, yscrollcommand=self.searchScrollbar2.set,
                                  bg = "light slate gray", font = ("HYHeadLine", 16, "bold"), fg = "white", relief = "flat")
        self.searchScrollbar2["command"] = self.searchCity.yview
        self.CityNum = 0
        self.TheaterNum = 0
        self.state = ""
        self.searchCity.bind("<Double-Button-1>", self.SelectCity)
        #<<ListboxSelect>>

        self.searchScrollbar3 = Scrollbar(self.SearchFrame3)
        self.searchTheater = Listbox(self.SearchFrame3, width = 20, height=height, yscrollcommand=self.searchScrollbar3.set,
                                     bg = "light slate gray", font = ("HYHeadLine", 16, "bold"), fg = "white", relief = "flat")
        self.searchScrollbar3["command"] = self.searchTheater.yview
        self.searchTheater.bind("<Double-Button-1>", self.SelectTheater)

        self.SetState()

        self.Map = Label(self.MapFrame, image = self.Image, bg = "black", bd = 2)
        self.TheaterNameLabel = Label(self.MapFrame, text = "한국산업기술대학교", font = ("HYHeadLine", 16, "bold"),
                                      bg = "light blue")
        self.TheaterAddressLabel = Label(self.MapFrame, text="경기도 시흥시 산기대학로 237", font=("HYHeadLine", 12, "bold"),
                                      bg="light blue")
        self.TheaterLinkLabel = Label(self.MapFrame, text = "", font = ("HYHeadLine", 16, "bold"), bg = "light blue",
                                      fg='lime green')
        self.TheaterLinkLabel.bind("<Button-1>", self.Link)
        self.TitleLabel = Label(self.MapFrame, image = self.labelImage, bg = "light blue")

        self.linktype = None
    def SetState(self):
        i = -1
        self.searchState.insert(++i, "제주특별자치도")
        self.searchState.insert(++i, "울산광역시")
        self.searchState.insert(++i, "부산광역시")
        self.searchState.insert(++i, "경상남도")
        self.searchState.insert(++i, "대구광역시")
        self.searchState.insert(++i, "경상북도")
        self.searchState.insert(++i, "대전광역시")
        self.searchState.insert(++i, "전라남도")
        self.searchState.insert(++i, "광주광역시")
        self.searchState.insert(++i, "전라북도")
        self.searchState.insert(++i, "충청남도")
        self.searchState.insert(++i, "충청북도")
        self.searchState.insert(++i, "강원도")
        self.searchState.insert(++i, "세종특별자치시")
        self.searchState.insert(++i, "경기도")
        self.searchState.insert(++i, "인천광역시")
        self.searchState.insert(++i, "서울특별시")

    def SelectState(self, event):
        try:
            #self.searchState.activate(self.searchState.curselection()[0])
            self.searchCity.delete(0, self.CityNum)
            self.CityNum = 0
            self.searchTheater.delete(0, self.TheaterNum)
            self.TheaterNum = 0
            citylist = []
            for data in self.TheaterList:
                state = self.searchState.get(self.searchState.curselection(), self.searchState.curselection())
                self.state = state[0]
                if data.addresslist[STATE] == state[0]:
                    if not data.addresslist[CITY] in citylist:
                        self.searchCity.insert(self.CityNum, data.addresslist[CITY])
                        citylist.append(data.addresslist[CITY])
                        self.CityNum += 1
        except:
            return

    def SelectCity(self, event):
        try:
            self.searchTheater.delete(0, self.TheaterNum)
            self.TheaterNum = 0
            for data in self.TheaterList:
                state = self.searchCity.get(self.searchCity.curselection(), self.searchCity.curselection())
                if self.state + " " + state[0] in data.address:
                    self.searchTheater.insert(self.TheaterNum, data.name)
                    self.TheaterNum += 1
        except:
            return

    def SelectTheater(self, event):
        name = self.searchTheater.get(self.searchTheater.curselection(), self.searchTheater.curselection())
        name = name[0]
        MyTheater = Theater(None, None, None, None, None, None)
        for theater in self.TheaterList:
            if theater.name == name:
                MyTheater = Theater(theater.name, theater.date, theater.address, theater.tel, theater.type, theater.code)
                break
        self.TheaterNameLabel.configure(text=MyTheater.name)
        self.TheaterAddressLabel.configure(text = MyTheater.address)

        address = LoadGoogleAPIGeocoding(MyTheater.address)

        self.Image = LoadGoogleAPIMapToURL(address[0], address[1])
        self.Map.configure(image = self.Image)
        self.linktype = MyTheater.name
        self.TheaterLinkLabel.configure(text="[네이버로 보기]")

    def Link(self, event):
        if self.linktype != None:
            OpenNaverWebBrowser(self.linktype)

    def Render(self):
        self.SearchFrame1.pack(side = LEFT)
        self.SearchFrame2.pack(side = LEFT)
        self.SearchFrame3.pack(side = LEFT)
        self.MapFrame.pack(side = LEFT)

        #self.searchScrollbar1.pack(side = RIGHT, fill = "y")
        self.searchState.pack()
        self.searchScrollbar2.pack(side=RIGHT, fill="y")
        self.searchCity.pack()
        self.searchScrollbar3.pack(side=RIGHT, fill="y")
        self.searchTheater.pack()
        self.Map.place(x=-5, y=60)
        self.TheaterNameLabel.place(x = 0, y = 370)
        self.TheaterAddressLabel.place(x = 0, y = 400)
        self.TheaterLinkLabel.place(x = 0, y = 430)
        self.TitleLabel.place(x=10, y = -10)

    def GetFrame(self):
        return self.TheaterFrame


























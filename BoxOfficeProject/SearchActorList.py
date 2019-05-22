# 리스트 박스에서 배우를 클릭하면
# 오른쪽에 프로필사진이나 이미지를 띄우고 관련된 뉴스 기사를 띄우기


from tkinter import *
from ReadData import *
import ActorInfo

class ActorList():
    def __init__(self, window, width, height):
        self.ActorName = None
        self.width = width
        self.height = height

        self.Background = Frame(window, bd=2, relief="solid", background="light blue")

        self.SearchFrame = Frame(self.Background, width = self.width / 2, height = 100, bg = "light blue")
        self.SearchFrameLabel = Label(self.SearchFrame, font=("나눔 고딕", 25, "bold"), text="배우 상세 정보", bg = "light blue")
        self.SearchEntry = Entry(self.SearchFrame, width = 31, font=("HYHeadLine", 15, "bold"), bd = 6, relief = "ridge")
        self.SearchBnt = Button(self.SearchFrame, text = "검색",   font=("나눔 고딕", 14, "bold"), width = 6, bd = 3, command = self.Search)

        self.ListFrame = Frame(self.Background, width=self.width / 2, height = 370, bg = "light blue")
        self.ActorListBox = Listbox(self.ListFrame, width = 46, height = 22, bd = 6, relief="ridge")
        self.ActorListScrollbar = Scrollbar(self.ListFrame)
        self.ActorListScrollbar["command"] = self.ActorListBox.yview
        self.NextBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="다음 페이지", bd=3, width=9, command=self.Next)
        self.PrevBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="이전 페이지", bd=3, width=9, command=self.Prev)
        self.InfoBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="정보 보기", bd=3, width=9, command=self.Info)

        # 리스트 박스에 들어있는 배우정보
        self.ActorData = ActorInfo.ActorManager()

        self.ListPage = 1
        self.InsertActorList()

        self.InfoFrame = Frame(self.Background, width = self.width / 2, height = self.height, bg = "light blue", bd = 6, relief = "ridge")
        #self.InfoCanvas = Canvas(self.InfoFrame, width=self.width / 2 - 10, height=500, bd=4, relief="ridge", bg="light blue")

    def InsertActorList(self, page = 1, name = None):
        self.ActorListData = LoadXMLFromFileActorList(self.ListPage, name, None)  # page = 1, name 이랑 movie를 none으로 인자를 넣으면 전체목록을 부름
        i = 0  # 리스트박스는 배열처럼 쓰기 때문에 일종의 인덱스 표현을 위해서
        for data in self.ActorListData.find_all("people"):
            if data.reprolenm.string == "배우":
                #print(data.peoplecd.string)
                self.ActorListBox.insert(i, data.peoplenm.string)
                actor = ActorInfo.Actor(data.peoplecd.string, data.peoplenm.string, data.reprolenm.string)
                self.ActorData.SetActor(actor)
                i += 1

        #print(self.ActorData.index)
        #print(i)
        # 리스트박스에 몇개를 집어넣었는지 알고 있어야 함

    def ClearActorList(self):
        self.ActorListBox.delete(0, self.ActorListBox.size() - 1)
        self.ActorData.Clear()

    def Search(self):
        ActorName = self.SearchEntry.get()
        self.ClearActorList()
        self.InsertActorList(self.ListPage, ActorName)

    def Next(self):
        self.ListPage += 1
        self.ClearActorList()
        self.InsertActorList(self.ListPage)

    def Prev(self):
        if self.ListPage == 1:
            return
        self.ListPage -= 1
        self.ClearActorList()
        self.InsertActorList(self.ListPage)

    def Info(self):
        index = self.ActorListBox.curselection()
        ActorName = self.ActorListBox.get(index)
        self.ActorData.FindCodeFromIndex(index[0])


    def Render(self):
        self.InfoFrame.pack(side = RIGHT, expand=True)
        self.SearchFrame.pack(anchor = "nw", expand=True)
        self.ListFrame.pack(anchor = "w",expand=True,fill="both")

        self.SearchFrameLabel.place(x = 10, y = 10)
        self.SearchEntry.place(x=0, y=62)
        self.SearchBnt.place(x = 355, y = 60)

        self.ActorListBox.pack(side = LEFT)
        self.ActorListScrollbar.pack(side=LEFT, fill="y")
        self.NextBnt.place(x = 355, y = 10)
        self.PrevBnt.place(x = 355, y = 40)             # 버튼 간격 30씩
        self.InfoBnt.place(x = 355, y = 70)
        #self.InfoCanvas.place(x = 0, y = 0)

    def GetFrame(self):
        return self.Background
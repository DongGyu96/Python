# 리스트 박스에서 배우를 클릭하면
# 오른쪽에 프로필사진이나 이미지를 띄우고 관련된 뉴스 기사를 띄우기


from tkinter import *
from ReadData import *
import ActorInfo
import requests
import urllib.parse
from bs4 import BeautifulSoup

class ActorList():
    def __init__(self, window, width, height):
        self.ActorName = None
        self.width = width
        self.height = height

        self.Background = Frame(window, bd=2, relief="solid", background="light blue")

        self.SearchFrame = Frame(self.Background, width = self.width, height = 70, bg = "light blue")
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
        self.BookmarkBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="북마크 보기", bd=3, width=9, command=self.Bookmark)
        self.AddBookmarkBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="북마크 저장", bd=3, width=9, command=self.AddBookmark)
        self.SubBookmarkBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="북마크 해제", bd=3, width=9, command=self.SubBookmark)

        # 즐겨 찾기 버튼을 눌러 저장한 배우 목록들
        self.BookmarkList = []
        # 북마크 창이 켜져있는지 체크
        self.BookmarkOn = False
        # 리스트 박스에 들어있는 배우정보
        self.ActorData = ActorInfo.ActorManager()

        self.ListPage = 1
        self.InfoFrame = Frame(self.Background, width = self.width / 2, height = 470, bg = "light blue", bd = 6, relief = "ridge")


        self.ActorLabel = Label(self.InfoFrame, bg = "light blue")
        self.NameLabel = Label(self.InfoFrame, font=("나눔 고딕", 25, "bold"), bg = "light blue")

        #self.InfoCanvas = Canvas(self.InfoFrame, width=self.width / 2 - 10, height=500, bd=4, relief="ridge", bg="light blue")

    def InsertActorList(self, page = 1, name = None):
        self.ActorListData = LoadXMLFromFileActorList(self.ListPage, name, None)  # page = 1, name 이랑 movie를 none으로 인자를 넣으면 전체목록을 부름
        i = 0  # 리스트박스는 배열처럼 쓰기 때문에 일종의 인덱스 표현을 위해서
        for data in self.ActorListData.find_all("people"):
            if data.reprolenm.string == "배우":
                self.ActorListBox.insert(i, data.peoplenm.string)
                actor = ActorInfo.Actor(data.peoplecd.string, data.peoplenm.string, data.reprolenm.string)
                self.ActorData.SetActor(actor)
                i += 1

    def ClearActorList(self):
        self.ActorListBox.delete(0, self.ActorListBox.size() - 1)
        self.ActorData.Clear()

    def Search(self):
        ActorName = self.SearchEntry.get()
        if ActorName == "":
            return
        self.ClearActorList()
        self.InsertActorList(self.ListPage, ActorName)
        self.BookmarkOn = False

        self.Actorimg = LoadNaverAPIToImage(ActorName)
        self.Actorimage = LoadImageFromURL(self.Actorimg['items'][0]['link'], 270, 380)
        #self.Actorimage = LoadImageFromURL("https://search.pstatic.net/common?type=a&size=120x150&quality=95&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2F76%2F201706081735556361.jpg", 270, 380)
        # people_info_z > div.cont_noline > div > div > a:nth-child(1) > img

        self.ActorLabel.configure(image = self.Actorimage)
        self.NameLabel.configure(text = ActorName)

    def Next(self):
        if self.BookmarkOn:
            return
        self.ListPage += 1
        self.ClearActorList()
        self.InsertActorList(self.ListPage)

    def Prev(self):
        if self.BookmarkOn:
            return
        if self.ListPage == 1:
            return
        self.ListPage -= 1
        self.ClearActorList()
        self.InsertActorList(self.ListPage)

    def Info(self):
        index = self.ActorListBox.curselection()
        if index == ():
            return
        name = self.ActorListBox.get(index[0])
        self.NameLabel.configure(text = name)

    def Bookmark(self):
        self.BookmarkOn = True
        self.ClearActorList()
        for i in range(len(self.BookmarkList)):
            self.ActorListBox.insert(i,self.BookmarkList[i][0])

    def AddBookmark(self):
        if self.BookmarkOn:
            return
        index = self.ActorListBox.curselection()
        if index == ():
            return
        code = self.ActorData.FindCodeFromIndex(index[0])
        name = self.ActorData.FindNameFromIndex(index[0])
        self.BookmarkList.insert(len(self.BookmarkList), [name, code])

    def SubBookmark(self):
        if not self.BookmarkOn:
            return
        index = self.ActorListBox.curselection()
        if index == ():
            return
        self.BookmarkList.pop(index[0])
        self.Bookmark()

    def Render(self):
        self.SearchFrame.pack(anchor = "nw", expand=True)
        self.InfoFrame.pack(fill="both")
        #self.ListFrame.pack(anchor = "w",expand=True,fill="both")

        self.SearchFrameLabel.place(x = 10, y = 10)
        self.SearchEntry.place(x = 300, y = 20)
        self.SearchBnt.place(x = 670, y = 20)

        self.ActorLabel.place(x = 0, y = 0)
        self.NameLabel.place(x=280, y=0)

        #self.ActorListBox.pack(side = LEFT)
        #self.ActorListBox.place(x = 0, y = 0)
        #self.ActorListScrollbar.pack(side=LEFT, fill="y")
        #self.ActorListScrollbar.place(x = 340, y = 0)
        #self.NextBnt.place(x = 355, y = 10)
        #self.PrevBnt.place(x = 355, y = 40)             # 버튼 간격 30씩
        #self.InfoBnt.place(x = 355, y = 70)
        #self.BookmarkBnt.place(x = 355, y = 100)
        #self.AddBookmarkBnt.place(x = 355, y = 130)
        #self.SubBookmarkBnt.place(x = 355, y = 160)

        #self.NameLabel.place(x = 0, y = 0)
        #self.InfoCanvas.place(x = 0, y = 0)

    def GetFrame(self):
        return self.Background



if __name__ == '__main__': # ReadData.py를 실행시킬때만 실행되는 내용
    actor = urllib.parse.quote("공유")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + actor
    req = requests.get(url)
    if req.ok:
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        imgselect = soup.select('people_info_z > div.cont_noline > div > div > a:nth-child(1) > img')
        print(imgselect)
    #img = LoadNaverAPIToImage("공유")
    #profile = i#mg['items']
    #print(profile)
    #print(profile[0]['link'])
    #window = Tk()
    #image = []
    #for data in profile:
    #    image.append(LoadImageFromURL(profile[0]['link'], 500, 200))
    #label = Label(window, image = image[0])
    #label.pack()
    #window.mainloop()



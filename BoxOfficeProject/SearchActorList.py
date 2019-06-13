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
        self.SearchBtn = Button(self.SearchFrame, text ="검색", font=("나눔 고딕", 14, "bold"), width = 6, bd = 3, command = self.Search)

        #self.BookmarkBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="북마크 보기", bd=3, width=9, command=self.Bookmark)
        #self.AddBookmarkBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="북마크 저장", bd=3, width=9, command=self.AddBookmark)
        #self.SubBookmarkBnt = Button(self.ListFrame, font=("HYHeadLine", 10, "bold"), text="북마크 해제", bd=3, width=9, command=self.SubBookmark)

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
        self.NewsLabel = Label(self.InfoFrame, font=("나눔 고딕", 25, "bold"), bg = "light blue")

        self.NewsTitleBtn= []


    def Search(self):
        ActorName = self.SearchEntry.get()
        if ActorName == "":
            return

        self.BookmarkOn = False

        url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + ActorName
        req = requests.get(url)
        if not req.ok:
            return

        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        imgselect = soup.find_all('img')
        #print(imgselect[1].get('src'))

        self.Actorimage = LoadImageFromURL(imgselect[1].get('src'), 120, 150)
        self.ActorLabel.configure(image = self.Actorimage)
        self.NameLabel.configure(text = ActorName)
        self.NewsLabel.configure(text = "관련 뉴스 기사")
        #ActorNews = LoadNaverAPIToNews(ActorName)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + ActorName
        req = requests.get(url)
        print(url)
        if not req.ok:
            return

        for btn in self.NewsTitleBtn:
            btn.destroy()
        self.NewsTitleBtn.clear()
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        News = soup.select('ul.type01 > li > dl > dt > a')
        for n in News:
            text = n['title']
            self.NewsTitleBtn.append(Button(self.InfoFrame, font=("나눔 고딕", 11, "bold"), text=text[:30] + "...", bg = "light blue", bd = 0, command = lambda url = n['href'] : self.NewsLink(url)))
            #print(n['title'], n['href'])

        for i in range(len(self.NewsTitleBtn)):
            self.NewsTitleBtn[i].place(x = self.width / 2 , y = 33 * i + 45)

    def NewsLink(self, link):
        OpenWebBrowser(link)

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

        self.SearchFrameLabel.place(x = 10, y = 10)
        self.SearchEntry.place(x = 300, y = 20)
        self.SearchBtn.place(x = 670, y = 20)

        self.ActorLabel.place(x = 0, y = 0)
        self.NameLabel.place(x=150, y=0)
        self.NewsLabel.place(x = self.width/ 2 , y = 0)

        #self.BookmarkBnt.place(x = 355, y = 100)
        #self.AddBookmarkBnt.place(x = 355, y = 130)
        #self.SubBookmarkBnt.place(x = 355, y = 160)


    def GetFrame(self):
        return self.Background



if __name__ == '__main__': # ReadData.py를 실행시킬때만 실행되는 내용
    actor = urllib.parse.quote("정유미")
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + actor
    req = requests.get(url)
    if req.ok:
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        imgselect = soup.find_all('img')
        print(imgselect[1].get('src'))




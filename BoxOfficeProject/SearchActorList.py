# 리스트 박스에서 배우를 클릭하면
# 오른쪽에 프로필사진이나 이미지를 띄우고 관련된 뉴스 기사를 띄우기


from tkinter import *
from ReadData import *
import ActorInfo
import requests
import urllib.parse
import copy
from bs4 import BeautifulSoup

class ActorList():
    def __init__(self, window, width, height):
        self.ActorName = None
        self.width = width
        self.height = height

        self.Background = Frame(window, bd=2, relief="solid", background="light blue")

        self.SearchFrame = Frame(self.Background, width = self.width, height = 70, bg = "light blue")
        self.SearchFrameLabel = Label(self.SearchFrame, font=("나눔 고딕", 25, "bold"), text="배우 상세 정보", bg = "light blue")
        self.SearchEntry = Entry(self.SearchFrame, width = 31, font=("HYHeadLine", 15, "bold"), bd = 1 , relief = "solid", bg = "light blue")
        self.searchImage = PhotoImage(file='image/Button/SearchHereIcon3.png')
        self.SearchBtn = Button(self.SearchFrame, image = self.searchImage, command=self.Search,bg= "light blue", bd = 0)
        #self.SearchBtn = Button(self.SearchFrame, text ="검색", font=("나눔 고딕", 14, "bold"), width = 6, bd = 3, command = self.Search)

        self.bookmarkImage = PhotoImage(file='image/Button/BookmarkIcon.png')

        self.Actor = []             # 이름, 프로필정보, 출연작품
        self.BookmarkBtn = Button(self.SearchFrame, image = self.bookmarkImage, command = lambda  x = self.Actor : self.Bookmark(self.Actor), bg= "light blue", bd = 2)

        # 즐겨 찾기 버튼을 눌러 저장한 배우 목록들
        self.BookmarkList = []
        # 북마크 창이 켜져있는지 체크
        self.ListPage = 1


        self.InfoFrame = Frame(self.Background, width = self.width / 2, height = 470, bg = "light blue", bd = 6, relief = "ridge")
        self.ActorLabel = Label(self.InfoFrame, bg = "light blue")
        self.NameLabel = Label(self.InfoFrame, font=("나눔 고딕", 25, "bold"), bg = "light blue")
        self.ActorInfo = []
        self.ActorMovie = []
        self.ActorMovieImg = []
        self.ActorMovieImgLabel = []
        self.LastInfoY = 0
        self.ActorMovieLabel = Label(self.InfoFrame, font=("나눔 고딕", 11, "bold"), bg="light blue" )

        self.noImage = PhotoImage(file = 'image/NoImage56x80.png')
        self.webImage = PhotoImage(file = 'image/WebIcon.png')

        self.NaverBtn = Button(self.InfoFrame, font=("나눔 고딕", 14, "bold"), bg="light blue", bd=0)
        self.NewsLabel = Label(self.InfoFrame, font=("나눔 고딕", 25, "bold"), bg = "light blue")
        self.NewsTitleBtn= []


    def Search(self):
        ActorName = self.SearchEntry.get()
        if ActorName == "":
            return

        self.Actor.clear()
        self.Actor.append(ActorName)
        self.NameLabel.configure(text = ActorName)

        #url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + ActorName
        #req = requests.get(url)
        #if not req.ok:
        #    return

        # 프로필 정보
       # html = req.text
        #soup = BeautifulSoup(html, 'html.parser')
        #info = soup.select('#people_info_z > div.cont_noline > div > dl')

        #if len(info) == 0:
        #    ActorName = "영화배우" + ActorName
         #   url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + ActorName
         #   req = requests.get(url)
       #    if not req.ok:
         #       return
          #  html = req.text
         #   soup = BeautifulSoup(html, 'html.parser')

        detail = self.GetProfile(ActorName)
        soup = detail[1]

        # 네이버에서 보기
        self.NaverBtn.configure(command =lambda url =detail[0] : self.NewsLink(url), image = self.webImage )

        for i in self.ActorInfo:
            i.destroy()
        self.ActorInfo.clear()

        for i in range(2, len(detail)):
            self.ActorInfo.append(Label(self.InfoFrame, font=("나눔 고딕", 11, "bold"), text=detail[i] , bg="light blue" ))

        dtcnt = len(self.ActorInfo)
        for i in range(dtcnt):
            self.ActorInfo[i].place(x = 125 , y = 30 * i + 45)

        detailInfo = self.GetProfileDetail(soup,  dtcnt)
        for d in detailInfo:
            text = d
            if len(text) > 20:
                text = text[:20] + "..."
            self.ActorInfo.append(Label(self.InfoFrame, font=("나눔 고딕", 11, "bold"), text=text, bg="light blue" ))

        self.LastInfoY = 0
        for i in range(dtcnt, len(self.ActorInfo)):
            self.ActorInfo[i].place(x = 175 , y = 30 * (i - dtcnt) + 45)
            self.LastInfoY = 30 * (i - dtcnt) + 45

        for i in range(2, len(detail)):
            info = detail[i] + " " + detailInfo[i - 2]
            self.Actor.append(info)

        # 출연한 영화정보
        for txt in self.ActorMovie:
            txt[1].destroy()
        self.ActorMovie.clear()
        self.ActorMovieImg.clear()
        for img in self.ActorMovieImgLabel:
            img.destroy()
        self.ActorMovieImgLabel.clear()

        actorMovie = self.GetMoive(soup)
        for m in actorMovie:
            self.ActorMovie.append((m[0], Label(self.InfoFrame, font=("나눔 고딕", 8, "bold"), text=m[0], bg="light blue")))
            if m[1] == "https://ssl.pstatic.net/sstatic/search/images11/blank.gif":
                self.ActorMovieImg.append(self.noImage)
            else:
                self.ActorMovieImg.append(LoadImageFromURL(m[1], 56, 80))

        for img in self.ActorMovieImg:
            self.ActorMovieImgLabel.append(Label(self.InfoFrame, image=img, bg="light blue"))

        if len(self.ActorMovie) != 0:
            self.ActorMovieLabel.configure(text="출연 작품")
            self.ActorMovieLabel.place(x=110, y=self.LastInfoY + 70)

            for i in range(3):
                self.ActorMovieImgLabel[i].place(x = 180 + (100 * i), y = self.LastInfoY + 50)
                self.ActorMovie[i][1].place(x = 180 + (100 * i), y = self.LastInfoY + 135)
                self.Actor.append(self.ActorMovie[i][0])
        else:
            self.ActorMovieLabel.configure(text="")


        # 프로필사진
        imgselect = soup.find_all('img')
        #print(imgselect[1].get('src'))

        self.Actorimage = LoadImageFromURL(imgselect[1].get('src'), 120, 150)
        self.ActorLabel.configure(image = self.Actorimage)

        #  뉴스
        self.NewsLabel.configure(text = "관련 뉴스 기사")
        for btn in self.NewsTitleBtn:
            btn.destroy()
        self.NewsTitleBtn.clear()

        news = self.GetNews(ActorName)
        for text in news:
            t = text[0]
            if len(t) > 29:
                t = t[:30] + "..."
            self.NewsTitleBtn.append(Button(self.InfoFrame, font=("나눔 고딕", 11, "bold"), text=t, bg = "light blue", bd = 0, command = lambda url = text[1] : self.NewsLink(url)))
            self.Actor.append(text)

        for i in range(len(self.NewsTitleBtn)):
            self.NewsTitleBtn[i].place(x = self.width / 2 , y = 33 * i + 45)

    def GetProfile(self, name):
        ActorName = name
        result = []
        url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + ActorName
        req = requests.get(url)
        if not req.ok:
           return None

        # 프로필 정보
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.select('#people_info_z > div.cont_noline > div > dl')

        if len(info) == 0:
            ActorName = "영화배우" + ActorName
            url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + ActorName
            req = requests.get(url)
            if not req.ok:
               return None
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

        result.append(url)
        result.append(soup)

        info = soup.select('#people_info_z > div.cont_noline > div > dl')

        if len(info) == 0:
            return None

        for i in info:
            dt = i.find_all('dt')
            for d in dt:
                if not d.text=="사이트":
                    result.append(d.text)

        return result

    def GetProfileDetail(self, soup, size):
        result = []
        for i in range(1, size + 1):
            info = soup.select('#people_info_z > div.cont_noline > div > dl> dd:nth-child(' + str(1 + i * 2) + ')')
            for i in info:
                result.append(i.text)
        return result

    def GetMoive(self, soup):
        result = []
        movie = soup.select('#tx_ca_people_movie_content > ul')

        for i in movie:
            dt = i.find_all('li')
            for d in dt:
                name = d.dd.text
                img = d.img['src']
                result.append([name, img])

        return result

    def GetNews(self, name):
        result = []
        ActorName = name

        ActorName += "배우"
        url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + ActorName
        req = requests.get(url)
        if not req.ok:
            return
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        News = soup.select('ul.type01 > li > dl > dt > a')
        for n in News:
            result.append((n['title'], n['href']))
        return result

    def NewsLink(self, link):
        OpenWebBrowser(link)

    def Bookmark(self, actor):
        if len(actor) == 0:
            return
        index = self.FindIndexToBookmarkList(actor[0])  # -1이면  없는거임
        if not index == -1:
            self.BookmarkList.pop(index)
        else:
            self.BookmarkList.append(copy.deepcopy(actor))

        #print(self.BookmarkList)
        #print(len(self.BookmarkList))


    def FindIndexToBookmarkList(self, name):
        cnt = 0
        for i in self.BookmarkList:
            if i[0] == name:
                return cnt
            cnt+= 1
        return -1

    def Render(self):
        self.SearchFrame.pack(anchor = "nw", expand=True)
        self.InfoFrame.pack(fill="both")

        self.SearchFrameLabel.place(x = 10, y = 10)
        self.SearchEntry.place(x = 300, y = 20)
        self.SearchBtn.place(x = 643, y = 18)
        self.BookmarkBtn.place(x = 800, y = 17)

        self.ActorLabel.place(x = 0, y = 0)
        self.NaverBtn.place(x = 28, y = 160)
        self.NameLabel.place(x=125, y=0)
        self.NewsLabel.place(x = self.width/ 2 , y = 0)

    def GetFrame(self):
        return self.Background

    def GetActorBookmark(self):
        return self.BookmarkList

    def GetActorInfo(self, list):
        name = list[1]

        ActorInfo = []
        ActorInfo.append("==========배우 정보==========")
        # 이름
        text = "배우 이름 : " + name
        ActorInfo.append(copy.deepcopy(text))

        # 프로필정보
        profiletext = self.GetProfile(name)
        soup = profiletext[1]
        size = len(profiletext) - 2
        profiledetail = self.GetProfileDetail(soup, size)

        info = []
        for i in range(size):
            text = profiletext[i + 2] + " : " + profiledetail[i]
            ActorInfo.append(copy.deepcopy(text))

        #ActorInfo.append(info)

        # 최근 작품
        movie = self.GetMoive(soup)

        text = ""
        for i in range(len(movie)):
            text = text + "[" + str(i + 1)+ "]" + movie[i][0] + "  "

        ActorInfo.append("==========최근 작품==========")
        ActorInfo.append(copy.deepcopy(text))

        # 뉴스
        news = self.GetNews(name)
        ActorInfo.append("==========관련 뉴스==========")
        for n in news:
            ActorInfo.append("[ "  + n[0] + " ] link : " + n[1])

        return ActorInfo




if __name__ == '__main__': # ReadData.py를 실행시킬때만 실행되는 내용
    pass
        #actor = urllib.parse.quote("영화배우정유미")
    #url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + actor
    #req = requests.get(url)
   # if req.ok:
    #    html = req.text
    #    soup = BeautifulSoup(html, 'html.parser')
     #   info = soup.select('#tx_ca_people_movie_content > ul')
    #    detail = []
    #    for i in info:
    #        dt = i.find_all('li')
   #         for d in dt:
    #            print(d.dd.text)
     #           print(d.img['src'])
            #print(i.find_all('dd'))#people_info_z > div.cont_noline > div > dl > dd:nth-child(3)

      #  for i in range(1, len(detail) + 1):
     #       info = soup.select('#people_info_z > div.cont_noline > div > dl> dd:nth-child(' + str(1 + i * 2) + ')')
     #       for i in info:
      #          print(i.text)
            #print(info)


        #print(info)
       # imgselect = soup.find_all('img')
        #print(imgselect[1].get('src'))







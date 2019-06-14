from tkinter import *
from tkinter.font import *
from ReadData import *

class MovieList():
    def __init__(self, window, width, height):
        self.moviename = None
        self.movielistpage = 1  # 1부터 페이지를 넘길거기 때문
        self.width = width
        self.height = height
        self.labelimage = PhotoImage(file = 'image/SearchMovieLabel.png')
        self.noImage = PhotoImage(file = 'image/NoImage.png')
        self.clearimage = PhotoImage(file = 'image/Button/ClearPageIcon2.png')
        self.nextimage = PhotoImage(file='image/Button/NextPageIcon2.png')
        self.previmage = PhotoImage(file='image/Button/PrevPageIcon2.png')
        self.infoimage = PhotoImage(file='image/Button/MoreInfoIcon2.png')
        self.searchimage = PhotoImage(file='image/Button/SearchHereIcon2.png')
        temp = 'light blue'
        #bd = 두깨 크기
        #relief = 외곽선 설정
        #background = 배경색
        #font = (글꼴 크기 스타일(볼드 기울임 등))
        #글씨 색바꾸는건 canvas_create.text에서만 가능한듯
        #이미지 혹은 캔버스만드려서 텍스트띄우는방법
        self.SearchFrame = Frame(window, bd=2, relief="solid", background=temp)
        self.framesearch1 = Frame(self.SearchFrame, width=self.width / 2, height=100, bd=0, relief="solid",
                                  background= temp)
        self.framesearch2 = Frame(self.SearchFrame, width=self.width / 2, height=self.height, bd=0, relief="solid",
                                  background= temp)
        self.framemovielist = Frame(self.SearchFrame, width=330, height=350, background="white")
        self.movielistscrollbar = Scrollbar(self.framemovielist, width = 14)
        self.movielistbox = Listbox(self.framemovielist, width=27, height=22, bd=6, relief="sunken",
                                    font = ("휴면엑스포", 15, "bold"),
                                    yscrollcommand=self.movielistscrollbar.set, bg = "azure",
                                    selectbackground = "orange", selectforeground = "black", selectborderwidth = 2,
                                    borderwidth = 4, fg = "black", highlightbackground = "gray",highlightthickness = 2)
        self.movielistscrollbar["command"] = self.movielistbox.yview
        self.movieinfocanvas = Canvas(self.framesearch2, width=self.width / 2 - 10, height=500, bd=4, relief="ridge",
                                      background="light blue")
        self.movieinfocanvas.bind("<Button-1>", self.Click)
        self.find = False

        self.SearchFrameLabel = Label(self.framesearch1, image = self.labelimage, bg = temp)

        self.searchmovie = Entry(self.framesearch1, font=("휴면엑스포", 16, "bold"), width=26, bd=6, relief="sunken", bg = "azure")
        self.searchmoviebutton = Button(self.SearchFrame, image = self.searchimage, bg = "SteelBlue4",
                                        bd=3, command = self.Search)
        self.nextmoviebutton = Button(self.SearchFrame, image = self.nextimage, bd=3, command=self.NextMovie, bg = "SteelBlue4")
        self.prevmoviebutton = Button(self.SearchFrame, image = self.previmage, bd=3, command=self.PrevMovie, bg = "SteelBlue4")
        self.infobutton = Button(self.SearchFrame, image = self.infoimage, bd = 3, command = self.Info, bg = "SteelBlue4")

        self.resetbutton = Button(self.SearchFrame, image = self.clearimage, bd = 3, command = self.Reset, bg = "SteelBlue4")
        self.setpage = Entry(self.SearchFrame, font=("HYHeadLine", 15, "bold"), width=7, bg = temp)
        self.setpage.insert(0, str(self.movielistpage))
        self.pagelabel = Label(self.SearchFrame, font =("HYHeadLine", 15, "bold"), text = "[Page]", bg = temp)
        #영화 목록 호출
        self.MovieListData = LoadXMLFromFileMovieList(self.movielistpage, self.moviename)

        self.movielistsize = 0
        self.movieInfoData = None # 영화 상세 정보를 저장할 변수
        self.url = None # 네이버 영화페이지 주소

        i = 0 # 리스트박스는 배열처럼 쓰기 때문에 일종의 인덱스 표현을 위해서
        find = False
        for data in self.MovieListData.find_all("movie"):
            for word in Filter: # 만약 필터링 배열의 단어들을 포문을 돌림
                if word in data.movienm.string: # 단어가 이름안에 포함된다면
                    find = True
                    break
            if find == False:
                self.movielistbox.insert(i, data.movienm.string)
                i+= 1
            find = False
        self.movielistsize = i # 새로 검색이나 다음페이지나 이전페이지로 갈경우 리스트박스를 지우고 다시 추가해야되기 때문에
        # 리스트박스에 몇개를 집어넣었는지 알고 있어야 함

    def Search(self):
        self.moviename = self.searchmovie.get() # 찾으려는 이름을 Entry에서 얻어옴
        self.movielistpage = 1
        if self.moviename != "":
            self.setpage.delete(0, len(self.setpage.get()))
            self.setpage.insert(0, str(self.movielistpage))
        self.ResetMovieList() # 리스트 박스 리셋

    def Info(self):
        # try가 성공하면 그냥 넘어가고 에러코드를 발생할 경우 에러메시지를 띄우거나 터트리지 않고
        # except문으로 넘김
        try:
            # 어떤 영화에 대한 상세정보를 띄울것인지 리스트박스에서 뭘 선택했는지 가져와야함
            # get(start, end) 면 스타트부터 앤드까지의 항목들을 튜플로 받아옴
            # get(1, 1) 이면 리스트박스 2번째의 영화이름이 들어간 (영화이름,) 이 반환되서
            # self.searchname[0] 으로 뽑아내서 쓰면 됨
            self.searchname = self.movielistbox.get(self.movielistbox.curselection(),self.movielistbox.curselection())
            for data in self.MovieListData.find_all("movie"):
                if data.movienm.string == self.searchname[0]:
                    self.movieInfoData = LoadXMLFromFileMovieInfo(data.moviecd.string)
                    break
        except:
            self.searchname = None
        self.RenderMovieInfo()

    def RenderMovieInfo(self):
        if self.movieInfoData != None:
            self.movieinfocanvas.create_rectangle(0, 0, self.width / 2, 500, fill = "light blue")
            naverAPI = LoadNaverAPIToMovie(self.movieInfoData.find("movienm").string)
            image = None
            rating = None
            try:
                for data in naverAPI['items']:
                    name = data['title']
                    name = name.replace(' ', '')
                    name = name.replace('<', '')
                    name = name.replace('>', '')
                    name = name.replace('/', '')
                    name = name.replace('b', '')
                    if self.movieInfoData.find("movienm").string.replace(' ', '') == name:
                        image = data['image']
                        rating = data['userRating'] + "/10.0"
                        url = data['link']
            except:
                image = None
                url = None

            self.movieinfocanvas.create_rectangle(15, 15, 185, 255, fill = 'black')

            try:
                if image != None:
                    self.movieImage = LoadImageFromURL(image, 165, 235)
                    self.movieinfocanvas.create_image(100, 135, image=self.movieImage)
                    self.find = True
                    self.url = url
                else:
                    self.movieinfocanvas.create_image(100, 135, image=self.noImage)
                    self.find = False
                    self.url = None
            except:
                self.movieinfocanvas.create_image(100, 135, image=self.noImage)
                self.find = False
                self.url = None

            #print(self.movieInfoData.find("moviecd").string)
            #print(self.movieInfoData.find("movienm").string)
            titlecolor = 'black'
            for data in self.movieInfoData.find_all("movieinfo"):
                # =====================================================================================================
                # 제목
                if len(data.movienm.string) < 6:
                    self.movieinfocanvas.create_text(325, 50, font=("Impact", 35, "bold"), text=data.movienm.string,fill=titlecolor)
                elif len(data.movienm.string) < 8:
                    self.movieinfocanvas.create_text(325, 55, font=("Impact", 31, "bold"), text=data.movienm.string, fill=titlecolor)
                elif len(data.movienm.string) < 11:
                    self.movieinfocanvas.create_text(320, 60, font=("Impact", 24, "bold"), text=data.movienm.string,fill=titlecolor)
                elif len(data.movienm.string) < 12:
                    self.movieinfocanvas.create_text(330, 65, font=("Impact", 20, "bold"), text=data.movienm.string, fill=titlecolor)
                elif len(data.movienm.string) < 18:
                    self.movieinfocanvas.create_text(320, 30, font=("Impact", 23, "bold"),text=data.movienm.string[:7], fill=titlecolor)
                    self.movieinfocanvas.create_text(320, 70, font=("Impact", 23, "bold"), text=data.movienm.string[7:], fill=titlecolor)
                else:
                    self.movieinfocanvas.create_text(320, 30, font=("Impact", 18, "bold"),text=data.movienm.string[:10], fill=titlecolor)
                    self.movieinfocanvas.create_text(320, 70, font=("Impact", 18, "bold"),text=data.movienm.string[10:25], fill=titlecolor)
                # ====================================================================================================
                self.movieinfocanvas.create_line(200, 100, 450, 100, width = 5) # 구분선
                # ====================================================================================================
                # 개봉일
                try:
                    day = data.opendt.string[:4] + "년" + data.opendt.string[4:6] + "월" + data.opendt.string[6:] + "일"
                except:
                    day = None
                self.movieinfocanvas.create_text(230, 125, font=("Impact", 16, "bold"), text="개봉일",  fill='black')
                self.movieinfocanvas.create_text(373, 125, font=("Impact", 16, "bold"), text=day, fill='black')
                # ====================================================================================================
                # 상영시간
                self.movieinfocanvas.create_text(240, 155, font=("Impact", 16, "bold"), text="상영시간", fill='black')
                try:
                    self.movieinfocanvas.create_text(426, 155, font=("Impact", 16, "bold"),
                                                     text=data.showtm.string + "분", fill='black')
                except:
                    pass
                # ====================================================================================================
                self.movieinfocanvas.create_line(200, 172, 450, 172, width=1)  # 구분선
                # 장르
                self.movieinfocanvas.create_text(220, 185, font=("Impact", 16, "bold"), text="장르", fill='black')
                line = 0
                for genre in data.find_all("genre"):
                    self.movieinfocanvas.create_text(400, 185 + (line * 30), font=("Impact", 16, "bold"), text=genre.genrenm.string, fill='black')
                    line += 1
                    if line == 3:
                        break
                # ====================================================================================================
                self.movieinfocanvas.create_line(20, 262, 450, 262, width=5)  # 구분선
                # ====================================================================================================
                # 감독
                self.movieinfocanvas.create_text(220, 280, font=("Impact", 16, "bold"), text="감독", fill='black')
                line = 0
                for director in data.find_all('director'):
                    words = len(director.peoplenm.string)
                    self.movieinfocanvas.create_text(450 - (words * 10), 280 + (line * 30), font=("Impact", 16, "bold"), text=director.peoplenm.string, fill='black')
                    line += 1
                    if line == 2:
                        break
                # ====================================================================================================
                # 평점
                self.movieinfocanvas.create_text(40, 280, font=("Impact", 16, "bold"), text="평점", fill='black')
                self.movieinfocanvas.create_text(130, 280, font=("Impact", 16, "bold"), text=rating, fill='black')
                self.movieinfocanvas.create_line(200, 330, 450, 330, width=2)  # 구분선
                # ====================================================================================================
                # 배우
                self.movieinfocanvas.create_text(220, 350, font=("Impact", 16, "bold"), text="배우", fill='black')
                line = 0
                for actor in data.find_all('actor'):
                    words = len(actor.peoplenm.string)
                    spaces = actor.peoplenm.string.count(' ')
                    self.movieinfocanvas.create_text(450 - (words * 10) + (spaces * 5), 350 + (line * 30), font=("Impact", 16, "bold"),
                                                     text=actor.peoplenm.string, fill='black')
                    line += 1
                    if line == 4:
                        break
                self.movieinfocanvas.create_line(195, 458, 450, 458, width=2)  # 구분선
                self.movieinfocanvas.create_line(245, 262, 245, 458, width=2)  # 구분선
                # ====================================================================================================
                # 심의 등급
                for grade in data.find_all('audit'):
                    self.movieinfocanvas.create_text(100, 310, font=("Impact", 16, "bold"), text=grade.watchgradenm.string, fill='black')
                # ====================================================================================================
                if image != None: # 하이퍼링크 텍스트
                    self.movieinfocanvas.create_text(100, 400, font=("Impact", 16, "bold"), text="[네이버로 보기]", fill='royalblue1')
                # ====================================================================================================

        #http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml?key=e4ef9cc26c8da2fbd710c5899e835cd7&movieCd=20191590

    def NextMovie(self):
        # 페이지를 증가시키고 리스트 박스 리셋
        self.movielistpage += 1
        self.setpage.delete(0, len(self.setpage.get()))
        self.setpage.insert(0, str(self.movielistpage))
        self.ResetMovieList()
    def PrevMovie(self):
        if self.movielistpage > 1:
            self.movielistpage -= 1
            self.setpage.delete(0, len(self.setpage.get()))
            self.setpage.insert(0, str(self.movielistpage))
        self.ResetMovieList()

    def Click(self, event):
        if self.find == False:
            return

        if event.x > 35 and event.x < 175: # 네이버로 보기 라벨 클릭
            if event.y > 390 and event.y < 410:
                if self.url != None:
                    OpenWebBrowser(self.url)

    def ResetMovieList(self):
        self.movielistpage = eval(self.setpage.get())
        self.MovieListData = LoadXMLFromFileMovieList(self.movielistpage, self.moviename)
        # 검색하려는 페이지와 이름을 넣어서 반환받음

        self.movielistbox.delete(0, self.movielistsize)
        # 리스트박스 원소갯수만큼 지움
        i = 0
        find = False
        for data in self.MovieListData.find_all("movie"):
            if data.repgenrenm.string != None:
                if not "성인물" in data.repgenrenm.string:
                    for word in Filter:
                        if word in data.movienm.string:
                            find = True
                            break
                    if find == False:
                        self.movielistbox.insert(i, data.movienm.string)
                        i += 1
                    find = False
        self.movielistsize = i

    def Render(self):
        self.framesearch2.pack(side=RIGHT, anchor="ne", fill="y", expand=True)
        self.framesearch1.pack(anchor="nw", fill="both", expand=True)
        self.framemovielist.pack(anchor="sw")
        self.movielistscrollbar.pack(side=RIGHT, fill="y")
        self.movielistbox.pack(anchor="s")
        self.movieinfocanvas.pack(side=RIGHT)
        self.SearchFrameLabel.place(x=5, y=-5)
        self.searchmovie.place(x=0, y=62)
        self.searchmoviebutton.place(x=330, y=60)
        self.nextmoviebutton.place(x=330, y=110)
        self.prevmoviebutton.place(x=330, y=150)
        self.infobutton.place(x=330, y= 190)
        self.resetbutton.place(x=330, y = 230)
        self.setpage.place(x=330, y= 430)
        self.pagelabel.place(x=330, y = 400)

    def Reset(self):
        self.movielistpage = 1
        self.moviename = None
        self.searchmovie.delete(0, len(self.searchmovie.get()))
        self.ResetMovieList()

    def GetFrame(self):
        return self.SearchFrame
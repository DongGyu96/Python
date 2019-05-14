from tkinter import *
from tkinter.font import *
from ReadData import *

class MovieList():
    def __init__(self, window, width, height):
        self.moviename = None
        self.movielistpage = 1  # 1부터 페이지를 넘길거기 때문
        self.width = width
        self.height = height

        #bd = 두깨 크기
        #relief = 외곽선 설정
        #background = 배경색
        #font = (글꼴 크기 스타일(볼드 기울임 등))
        #글씨 색바꾸는건 canvas_create.text에서만 가능한듯
        #이미지 혹은 캔버스만드려서 텍스트띄우는방법
        self.SearchFrame = Frame(window, bd=2, relief="solid", background="light blue")
        self.framesearch1 = Frame(self.SearchFrame, width=self.width / 2, height=100, bd=0, relief="solid",
                                  background="light blue")
        self.framesearch2 = Frame(self.SearchFrame, width=self.width / 2, height=self.height, bd=0, relief="solid",
                                  background="light blue")
        self.framemovielist = Frame(self.SearchFrame, width=330, height=350, background="white")
        self.movielistscrollbar = Scrollbar(self.framemovielist)
        self.movielistbox = Listbox(self.framemovielist, width=46, height=22, bd=6, relief="ridge",
                                    yscrollcommand=self.movielistscrollbar.set)
        self.movielistscrollbar["command"] = self.movielistbox.yview
        self.movieinfocanvas = Canvas(self.framesearch2, width=self.width / 2 - 10, height=500, bd=4, relief="ridge",
                                      background="light blue")

        self.SearchFrameLabel = Label(self.framesearch1, font=("Impact", 25, "bold"), text="영화 상세 정보")

        self.searchmovie = Entry(self.framesearch1, font=("HYHeadLine", 15, "bold"), width=31, bd=6, relief="ridge")
        self.searchmoviebutton = Button(self.SearchFrame, font=("HYHeadLine", 14, "bold"), text="검색", width=6,
                                        bd=3, command = self.Search)
        self.nextmoviebutton = Button(self.SearchFrame, font=("HYHeadLine", 10, "bold"), text="다음 페이지", bd=3,
                                      width=9, command=self.NextMovie)
        self.prevmoviebutton = Button(self.SearchFrame, font=("HYHeadLine", 10, "bold"), text="이전 페이지", bd=3,
                                      width=9, command=self.PrevMovie)
        self.infobutton = Button(self.SearchFrame, font = ("HYHeadLine", 10, "bold"), text = "상세 정보", bd = 3,
                                 width = 9, command = self.Info)

        self.MovieListData = LoadXMLFromFileMovieList(self.movielistpage, self.moviename)

        self.movielistsize = 0

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
        except:
            self.searchname = None

    def NextMovie(self):
        # 페이지를 증가시키고 리스트 박스 리셋
        self.movielistpage += 1
        self.ResetMovieList()
    def PrevMovie(self):
        if self.movielistpage > 1:
            self.movielistpage -= 1
        self.ResetMovieList()

    def ResetMovieList(self):
        self.MovieListData = LoadXMLFromFileMovieList(self.movielistpage, self.moviename)
        # 검색하려는 페이지와 이름을 넣어서 반환받음

        self.movielistbox.delete(0, self.movielistsize)
        # 리스트박스 원소갯수만큼 지움
        i = 0
        find = False
        for data in self.MovieListData.find_all("movie"):
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
        self.SearchFrameLabel.place(x=10, y=10)
        self.searchmovie.place(x=0, y=62)
        self.searchmoviebutton.place(x=355, y=60)
        self.nextmoviebutton.place(x=355, y=110)
        self.prevmoviebutton.place(x=355, y=140)
        self.infobutton.place(x=355, y= 170)

    def GetFrame(self):
        return self.SearchFrame
from tkinter import *
from tkinter.font import *
from ReadData import *

class MovieList():
    def __init__(self, window, width, height):
        self.movielistpage = 1
        self.width = width
        self.height = height
        self.SearchFrame = Frame(window, bd=2, relief="solid", background="light yellow")
        self.framesearch1 = Frame(self.SearchFrame, width=self.width / 2, height=100, bd=0, relief="solid",
                                  background="light yellow")
        self.framesearch2 = Frame(self.SearchFrame, width=self.width / 2, height=self.height, bd=0, relief="solid",
                                  background="light yellow")
        self.framemovielist = Frame(self.SearchFrame, width=330, height=350, background="white")
        self.movielistscrollbar = Scrollbar(self.framemovielist)
        self.movielistbox = Listbox(self.framemovielist, width=46, height=22, bd=6, relief="ridge",
                                    yscrollcommand=self.movielistscrollbar.set)
        self.movielistscrollbar["command"] = self.movielistbox.yview
        self.movieinfocanvas = Canvas(self.framesearch2, width=self.width / 2, height=500, bd=4, relief="ridge",
                                      background="light yellow")

        self.SearchFrameLabel = Label(self.framesearch1, font=("Impact", 25, "bold"), text="영화 상세 정보")

        self.searchmovie = Entry(self.framesearch1, font=("HYHeadLine", 15, "bold"), width=31, bd=6, relief="ridge")
        self.searchmoviebutton = Button(self.SearchFrame, font=("HYHeadLine", 14, "bold"), text="검색", width=6, bd=3)
        self.nextmoviebutton = Button(self.SearchFrame, font=("HYHeadLine", 10, "bold"), text="다음 페이지", bd=3,
                                      command=self.NextMovie)
        self.prevmoviebutton = Button(self.SearchFrame, font=("HYHeadLine", 10, "bold"), text="이전 페이지", bd=3,
                                      command=self.PrevMovie)
        self.MovieListData = LoadXMLFromFileMovieList(self.movielistpage)
        i = 0
        for data in self.MovieListData.find_all("movie"):
            self.movielistbox.insert(i, data.movienm.string)
            i += 1

    def NextMovie(self):
        self.movielistpage += 1
        self.ResetMovieList()
    def PrevMovie(self):
        if self.movielistpage > 1:
            self.movielistpage -= 1
        self.ResetMovieList()

    def ResetMovieList(self):
        self.MovieListData = LoadXMLFromFileMovieList(self.movielistpage)

        self.movielistbox.delete(0, 49)
        i = 0
        for data in self.MovieListData.find_all("movie"):
            self.movielistbox.insert(i, data.movienm.string)
            i += 1

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

    def GetFrame(self):
        return self.SearchFrame
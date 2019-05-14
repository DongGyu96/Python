from tkinter import *
from Ranking import *
from SearchMovieList import *
from SearchActorList import *
from tkinter.font import *
import tkinter.ttk

class Interface:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        self.SetPhotoImage()

        self.notebook = tkinter.ttk.Notebook(window, width = self.width - 20, height = self.height - 130)
        
        self.titlelabel = Label(window, height = 100, image = self.titleimage)

        self.Ranking = Ranking(window, width, height)
        self.notebook.add(self.Ranking.GetFrame(), image=self.RankingIcon)

        self.MovieList = MovieList(window, width, height)
        self.notebook.add(self.MovieList.GetFrame(), image=self.SearchIcon)

        self.ActorList = ActorList(window, width, height)
        self.notebook.add(self.ActorList.GetFrame(), image = self.ActorSearchIcon)


        self.MapFrame = Frame(window, bd = 2, relief = "solid")
        self.notebook.add(self.MapFrame, image = self.MapIcon)
        self.SettingFrame = Frame(window, bd = 2, relief = "solid")
        self.notebook.add(self.SettingFrame, image = self.SettingIcon)


    def SetPhotoImage(self):
        # label, button에도 사용 가능
        self.RankingIcon = PhotoImage(file="image/RankingIcon4.png")
        self.MapIcon = PhotoImage(file = "image/MapIcon3.png")
        self.SearchIcon = PhotoImage(file = "image/SearchIcon2.png")
        self.SettingIcon = PhotoImage(file = "image/SettingIcon2.png")
        self.ActorSearchIcon = PhotoImage(file = "image/ActorSearchIcon2.png")
        self.titleimage = PhotoImage(file = "image/TitleImage.png")


    def Draw(self):
        self.titlelabel.place(x = self.width - 370, y = 5)
        self.notebook.place(x = 10, y = 40)
        self.MovieList.Render()
        self.Ranking.Render()
        self.ActorList.Render()
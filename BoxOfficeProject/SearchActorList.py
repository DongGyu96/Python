from tkinter import *
from ReadData import *

class ActorList():
    def __init__(self, window, width, height):
        self.ActorName = None
        self.width = width
        self.height = height

        self.Background = Frame(window, bd=2, relief="solid", background="light blue")

        self.SearchFrame = Frame(self.Background, width = self.width / 2, bg = "light blue", bd = 2, relief = "solid")
        self.SearchFrameLabel = Label(self.SearchFrame, font=("Impact", 25, "bold"), text="배우 상세 정보", bg = "light blue")
        self.SearchEntry = Entry(self.SearchFrame, width = 31, font=("HYHeadLine", 15, "bold"), bd = 6, relief = "ridge")
        self.SearchBnt = Button(self.SearchFrame, text = "검색",   font=("HYHeadLine", 14, "bold"), width = 6, bd = 3, command = self.Search)

        self.ListFrame = Frame(self.Background, width = 330, height = 370, bg = "light blue", bd = 2, relief = "solid")
        self.ActorListBox = Listbox(self.ListFrame, width =  46, bd = 6, relief="ridge")
        self.ActorListScrollbar = Scrollbar(self.ListFrame)
        self.ActorListScrollbar["command"] = self.ActorListBox.yview

        self.InfoFrame = Frame(self.Background,width = self.width / 2, bg = "light blue", bd = 2, relief = "solid")
        self.InfoCanvas = Canvas(self.InfoFrame, width=self.width / 2 - 10, height=500, bd=4, relief="ridge", bg="light blue")



    def Search(self):
        pass

    def Render(self):
        self.SearchFrame.pack(anchor="nw", fill="both", expand=True)
        self.SearchFrameLabel.place(x = 10, y = 10)
        self.SearchEntry.place(x=0, y=62)
        self.SearchBnt.place(x = 355, y = 59)
        self.ListFrame.pack(anchor="sw", fill="both", expand=True)
        self.ActorListScrollbar.pack(side=RIGHT, fill="y")
        self.ActorListBox.place(x = 0, y = 0)
        self.InfoFrame.pack(side=RIGHT, anchor="ne", fill="y", expand=True)
        self.InfoCanvas.place(x = 0, y = 0)

    def GetFrame(self):
        return self.Background
from tkinter import *
from ReadData import *

class SearchTheater():
    def __init__(self, window, width, height):
        self.TheaterFrame = Frame(window, width = width, height = height, bd=2, relief="solid", bg = "light blue")
        self.testimage = LoadGoogleAPIMapToURL(35.100697, 129.019798)
        self.MapFrame = Frame(self.TheaterFrame, width = 600, height = 300, bg = "black", bd = 2)
        self.Map = Label(self.MapFrame, image = self.testimage)
    def Render(self):
        self.MapFrame.pack(anchor = "ne")
        self.Map.pack()
    def GetFrame(self):
        return self.TheaterFrame
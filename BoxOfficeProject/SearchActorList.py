from tkinter import *
from tkinter.font import *
from ReadData import *

class ActorList():
    def __init__(self, window, width, height):
        self.ActorName = None

        self.Background = Frame(window, bd=2, relief="solid", background="light blue")

    def Search(self):
        pass

    def Render(self):
        pass

    def GetFrame(self):
        return self.Background
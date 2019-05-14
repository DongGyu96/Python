from tkinter import *
from ReadData import *

class ActorList():
    def __init__(self, window, width, height):
        self.ActorName = None

        self.Background = Frame(window, bd=2, relief="solid", background="light blue")

        self.SearchFrame = Frame(self.Background, bd = 2, relief = "solid", bg = "white")
        self.SearchFrameLabel = Label(self.SearchFrame, font=("Impact", 25, "bold"), text="배우 상세 정보", bg = "light blue")
        self.SearchEntry = Entry(self.SearchFrame, width = 50)



    def Search(self):
        pass

    def Render(self):
        self.SearchFrame.pack(anchor="nw", fill="both", expand=True)
        # ex)  anchor : 특정위치로 이동, fill : 크기 맞춤, expand : 미사용 공간 확보
        # 그리고 나는 frame안에 entry넣으니까 외곽선이 검정색으로만 보이는데 이거 너꺼처럼 흰색 + 회색으로 하는법
        # 아니 프레임 추가해서 pack하니까 하늘색 사라짐 ㅡㅡ ㅅㅂ

        self.SearchFrameLabel.place(x = 10, y = 10)
        self.SearchEntry.place(x=10, y=100)

    def GetFrame(self):
        return self.Background
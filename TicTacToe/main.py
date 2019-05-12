from tkinter import *
import random

class TicTacToe:
    def __init__(self):
        window = Tk()
        window.geometry("200x200+400+400")
        frame1 = Frame(window)
        frame2 = Frame(window)
        self.imageList = []
        self.imageList.append(PhotoImage(file = 'image/o.gif'))
        self.imageList.append(PhotoImage(file = 'image/x.gif'))
        self.imageList.append(PhotoImage(file = 'image/empty.gif'))
        frame1.pack()
        frame2.pack()

        self.turn = True # True = O Turn    False = X Turn
        self.buttonList = []
        self.cellList = [[0 for y in range(3)] for x in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttonList.append(Button(frame1, image = self.imageList[2], command = lambda Row = r, Col = c : self.Pressed(Row, Col)))
                self.buttonList[(r*3) + c].grid(row = r, column = c)
        self.explain = Label(frame2, text = "O 차례")
        self.explain.pack()

        Button(frame2, text='다시생성', command=self.Again).pack()
        window.mainloop()

    def Again(self):
        for r in range(3):
            for c in range(3):
                self.buttonList[(r*3) + c].configure(image = self.imageList[2], state = "active")
                self.cellList[r][c] = 0
                #self.labelList[(r*3) + c]["image"] = self.imageList[random.randint(0, 1)]
        self.turn = True
        self.explain.configure(text = "O 차례")

    def Pressed(self, r, c):
        if self.turn:
            self.buttonList[(r*3)+c].configure(image = self.imageList[0], state = "disable")
            self.turn = False
            self.explain.configure(text = "X 차례")
            self.cellList[r][c] = 1
        else:
            self.buttonList[(r * 3) + c].configure(image=self.imageList[1], state = "disable")
            self.turn = True
            self.explain.configure(text = "O 차례")
            self.cellList[r][c] = -1
        self.Check()

    def Check(self):
        result = 0
        for r in range(3):
            for c in range(3):
                result += self.cellList[r][c]
                if result == 3:
                    self.End(True)
                    return
                elif result == -3:
                    self.End(False)
                    return
            result = 0

        for c in range(3):
            for r in range(3):
                result += self.cellList[r][c]
                if result == 3:
                    self.End(True)
                    return
                elif result == -3:
                    self.End(False)
                    return
            result = 0

        for i in range(3):
            result += self.cellList[i][i]
            if result == 3:
                self.End(True)
                return
            elif result == -3:
                self.End(False)
                return
        result = 0

        for i in range(3):
            result += self.cellList[i][(i-2) * -1]
            if result == 3:
                self.End(True)
                return
            elif result == -3:
                self.End(False)
                return

        for r in range(3):
            for c in range(3):
                if self.cellList[r][c] == 0:
                    return
        self.explain.configure(text="무승부")

    def End(self, winner):
        if winner:
            for r in range(3):
                for c in range(3):
                    self.buttonList[(r * 3) + c].configure(state="disable")
            self.explain.configure(text = "O 승리!")
        else:
            for r in range(3):
                for c in range(3):
                    self.buttonList[(r * 3) + c].configure(state="disable")
            self.explain.configure(text = "X 승리!")


TicTacToe()
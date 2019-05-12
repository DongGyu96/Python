from tkinter import *
import random

class TicTacToe:
    def __init__(self):
        window = Tk()
        window.geometry("400x400+400+400")
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
        self.cellList = [[0 for y in range(7)] for x in range(6)]
        for r in range(6):
            for c in range(7):
                self.buttonList.append(Button(frame1, image = self.imageList[2], text = ' ', command = lambda Row = r, Col = c : self.Pressed(Row, Col)))
                self.buttonList[(r*7) + c].grid(row = r, column = c)
        self.explain = Label(frame2, text = "O 차례")
        self.explain.pack()

        Button(frame2, text='다시생성', command=self.Again).pack()
        window.mainloop()

    def Again(self):
        for r in range(6):
            for c in range(7):
                self.buttonList[(r*7) + c].configure(image = self.imageList[2], text = ' ', state = "active")
                self.cellList[r][c] = 0
                #self.labelList[(r*3) + c]["image"] = self.imageList[random.randint(0, 1)]
        self.turn = True
        self.explain.configure(text = "O 차례")

    def Pressed(self, r, c):
        for i in range(5, -1, -1):
            if self.buttonList[i*7 + c]['text'] == ' ':
                if self.turn:
                    self.buttonList[(i*7)+c].configure(image = self.imageList[0], state = "disable", text = "O")
                    self.turn = False
                    self.explain.configure(text = "X 차례")
                    self.cellList[i][c] = 1
                    if self.Check(i, c, 1):
                        self.explain.configure(text = "O 승리!")
                        for r in range(6):
                            for c in range(7):
                                self.buttonList[(r * 7) + c].configure(state="disabled")
                    return
                else:
                    self.buttonList[(i * 7) + c].configure(image=self.imageList[1], state = "disable", text = "X")
                    self.turn = True
                    self.explain.configure(text = "O 차례")
                    self.cellList[i][c] = -1
                    if self.Check(i, c, -1):
                        self.explain.configure(text = "X 승리!")
                        for r in range(6):
                            for c in range(7):
                                self.buttonList[(r * 7) + c].configure(state="disabled")
                    return

    def Check(self, row, col, turn):
        count = 0
        for c in range(col, -1, -1): # <-- 왼쪽
            if not turn == self.cellList[row][c]:
                break
            else:
                count += 1
                if count == 4:
                    return True

        count = 0
        for c in range(col, 7): # --> 오른쪽
            if not turn == self.cellList[row][c]:
                break
            else:
                count += 1
                if count == 4:
                    return True

        count = 0
        for r in range(row, -1, -1): # 아래
            if not turn == self.cellList[r][col]:
                break
            else:
                count += 1
                if count == 4:
                    return True

        count = 0
        for r in range(row, 6): # 위
            if not turn == self.cellList[r][col]:
                break
            else:
                count += 1
                if count == 4:
                    return True

        count = 0
        r = row
        c = col
        while(1): # \ 대각선 아래
            if r >= 6 or c >= 7:
                break
            if not turn == self.cellList[r][c]:
                break
            else:
                count += 1
                if count == 4:
                    return True
                r += 1
                c += 1

        count = 0
        r = row
        c = col
        while (1):  # \ 대각선 위
            if r < 0 or c < 0:
                break
            if not turn == self.cellList[r][c]:
                break
            else:
                count += 1
                if count == 4:
                    return True
                r -= 1
                c -= 1

        count = 0
        r = row
        c = col
        while (1):  # / 대각선 아래
            if r >= 6 or c < 0:
                break
            if not turn == self.cellList[r][c]:
                break
            else:
                count += 1
                if count == 4:
                    return True
                r += 1
                c -= 1

        count = 0
        r = row
        c = col
        while (1):  # / 대각선 위
            if r < 0 or c >= 7:
                break
            if not turn == self.cellList[r][c]:
                break
            else:
                count += 1
                if count == 4:
                    return True
                r -= 1
                c += 1


TicTacToe()
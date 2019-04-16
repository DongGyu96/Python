from tkinter import *

class Ball:
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.x = 250
        self.y = 175
        self.speed = 10
        self.id = canvas.create_oval(self.x - 10, self.y - 10,
                                     self.x + 10, self.y + 10, fill = color, width = 1)
        self.dir = 0
    def draw(self, dir):
        if dir == self.TOP:
            self.canvas.move(self.id, 0, -self.speed)
        elif dir == self.BOTTOM:
            self.canvas.move(self.id, 0, self.speed)
        elif dir == self.LEFT:
            self.canvas.move(self.id, -self.speed, 0)
        elif dir == self.RIGHT:
            self.canvas.move(self.id, self.speed, 0)
        pos = self.canvas.coords(self.id)
    def MoveTop(self):
        if self.y - self.speed > 0:
            self.y -= self.speed
            self.draw(self.TOP)
    def MoveBottom(self):
        if self.y + self.speed < 350:
            self.y += self.speed
            self.draw(self.BOTTOM)
    def MoveRight(self):
        if self.x + self.speed < 500:
            self.x += self.speed
            self.draw(self.RIGHT)
    def MoveLeft(self):
        if self.x - self.speed > 0:
            self.x -= self.speed
            self.draw(self.LEFT)

window = Tk()
window.title("공 옮기기")
window.geometry("500x400+100+100")
window.resizable(False, False)

canvas = Canvas(window, width = 500, height = 350, relief = "solid", bd = 1, background = 'white')
canvas.pack()

ball = Ball(canvas, 'blue')
topbutton = Button(window, text = "상", width = 2, command = ball.MoveTop)
bottombutton = Button(window, text = "하", width = 2, command = ball.MoveBottom)
leftbutton = Button(window, text = "좌", width = 2, command = ball.MoveLeft)
rightbutton = Button(window, text = "우", width = 2, command = ball.MoveRight)


topbutton.pack(side = LEFT)
bottombutton.pack(side = LEFT)
leftbutton.pack(side = LEFT)
rightbutton.pack(side = LEFT)
window.mainloop()
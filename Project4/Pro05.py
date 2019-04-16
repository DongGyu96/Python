from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, x, y, color, speedx, speedy):
        self.x = x
        self.y = y
        self.color = color
        self.speedx = speedx
        self.speedy = speedy
        self.size = 10
        self.canvas = canvas
        self.id = canvas.create_oval(self.x - self.size, self.y - self.size,
                                     self.x + self.size, self.y + self.size, fill=color, width=1)
    def Draw(self):
        self.Check()
        self.canvas.move(self.id, self.speedx, self.speedy)
        pos = self.canvas.coords(self.id)
    def Check(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x + self.speedx > 600:
            self.speedx *= -1
        elif self.x + self.speedx < 0:
            self.speedx *= -1
        if self.y + self.speedy > 300:
            self.speedy *= -1
        elif self.y + self.speedy < 0:
            self.speedy *= -1

def Update():
    global active, ball, window
    while active:
        for i in range(20):
            ball[i].Draw()
        window.update()
        time.sleep(0.05)
def Stop():
    global active
    active = False
def Start():
    global active
    if not active:
        active = True
        Update()
def Create():
    pass
def Delete():
    pass
def Fast():
    pass
def Slow():
    pass

colors = ["blue", "red", "yellow", "brown", "black", "purple"]

window = Tk()
window.title("공 튕기기")
window.geometry("600x350+400+400")
window.resizable(False, False)

active = True

canvas = Canvas(window, width = 600, height = 300, relief = "solid", bd = 1, background = 'white')
canvas.pack()
ball = []
for i in range(20):
    color = colors[random.randrange(0, 6)]
    dir = random.randrange(0, 4)
    if dir == 0:
        ball.append(Ball(canvas, random.randrange(50, 550), random.randrange(50, 250), color, 5, 5))
    elif dir == 1:
        ball.append(Ball(canvas, random.randrange(50, 550), random.randrange(50, 250), color, -5, 5))
    elif dir == 2:
        ball.append(Ball(canvas, random.randrange(50, 550), random.randrange(50, 250), color, 5, -5))
    elif dir == 3:
        ball.append(Ball(canvas, random.randrange(50, 550), random.randrange(50, 250), color, -5, -5))
stop = Button(window, text = "정지", command = Stop)
start = Button(window, text = "재시작", command = Start)
create = Button(window, text = "+", command = Create)
delete = Button(window, text = "-", command = Delete)
fast = Button(window, text = "빠르게", command = Fast)
slow = Button(window, text = "느리게", command = Slow)

stop.pack(side = LEFT)
start.pack(side = LEFT)
create.pack(side = LEFT)
delete.pack(side = LEFT)
fast.pack(side = LEFT)
slow.pack(side = LEFT)

Update()


window.mainloop()
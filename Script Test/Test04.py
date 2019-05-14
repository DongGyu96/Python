from tkinter import *
import time

class Ball:
    def __init__(self):
        self.id = 0
        self.x = 12
        self.y = 12
        self.size = 2
        self.speedx = 10
        self.speedy = 10
    def Update(self):
        self.x += self.speedx
        self.y += self.speedy
        if self.x + self.speedx > 500:
            self.speedx *= -1
        elif self.x + self.speedx < 0:
            self.speedx *= -1
        if self.y + self.speedy > 300:
            self.speedy *= -1
        elif self.y + self.speedy < 0:
            self.speedy *= -1


class BallAnimate:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x340+400+400")
        self.window.resizable(False, False)
        self.window.title("공 튀기기")
        self.ballList = []
        self.active = True
        self.canvas = Canvas(self.window, width=500, height=300, background="White")
        self.canvas.pack()
        self.speed = 100
        self.ballList.append(Ball())
        self.ballList[0].id = self.canvas.create_oval(self.ballList[0].x - self.ballList[0].size, self.ballList[0].y - self.ballList[0].size,
                                                 self.ballList[0].x + self.ballList[0].size, self.ballList[0].y + self.ballList[0].size, fill="Red")

        Button(self.window, text="정지", command = self.Stop).pack(side=LEFT)
        Button(self.window, text="재시작", command=self.Start).pack(side=LEFT)
        Button(self.window, text="+", command=self.Add).pack(side=LEFT)
        Button(self.window, text="-", command=self.Del).pack(side=LEFT)
        Button(self.window, text="빠르게", command=self.Fast).pack(side=LEFT)
        Button(self.window, text="느리게", command=self.Slow).pack(side=LEFT)
        self.Update()
        self.window.mainloop()


    def Update(self):
        while(self.active):
            for i in range(len(self.ballList)):
                self.canvas.move(self.ballList[i].id, self.ballList[i].speedx, self.ballList[i].speedy)
                self.ballList[i].Update()
            self.window.update()
            time.sleep(self.speed / 1000)
        return

    def Stop(self):
        self.active = False
    def Start(self):
        if self.active == False:
            self.active = True
            self.Update()

    def Add(self):
        self.ballList.append(Ball())
        self.ballList[len(self.ballList) - 1].id = self.canvas.create_oval(self.ballList[len(self.ballList) - 1].x - self.ballList[len(self.ballList) - 1].size,
                                                                        self.ballList[len(self.ballList) - 1].y - self.ballList[len(self.ballList) - 1].size,
                                                                        self.ballList[len(self.ballList) - 1].x + self.ballList[len(self.ballList) - 1].size,
                                                                        self.ballList[len(self.ballList) - 1].y + self.ballList[len(self.ballList) - 1].size, fill="Red")
    def Del(self):
        if len(self.ballList) > 1:
            self.canvas.create_rectangle(0, 0, 600, 300, fill = "White", width = 0)
            self.ballList.pop()
            for i in range(len(self.ballList)):
                self.ballList[i].id = self.canvas.create_oval(self.ballList[i].x - self.ballList[i].size,
                                                              self.ballList[i].y - self.ballList[i].size,
                                                              self.ballList[i].x + self.ballList[i].size,
                                                              self.ballList[i].y + self.ballList[i].size, fill="Red")
    def Fast(self):
        if self.speed - 50 > 0:
            self.speed -= 50
    def Slow(self):
        self.speed += 50


BallAnimate()
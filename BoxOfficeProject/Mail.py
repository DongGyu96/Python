# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import SearchActorList
import SearchMovieList
from tkinter import *

class Gmail:
    def __init__(self, window, width, height, interface):
        self.window = window
        self.width = width
        self.height = height
        self.interface = interface

        self.Background = Frame(window, bd=2, relief="solid", background="light blue")

        self.BookMarkFrame = Frame(self.Background, width = self.width / 2, height = self.height, bg = "light blue")
        self.BookMarkLabel = Label(self.BookMarkFrame, text = "북마크",font=("나눔 고딕", 25, "bold"), bg = "light blue" )
        self.BookMarkListFrame = Frame(self.BookMarkFrame,width = self.width / 2)
        self.BookMarkScroll = Scrollbar(self.BookMarkListFrame)
        self.BookMarkInfoList = []
        self.BookMarkList = Listbox(self.BookMarkListFrame, width=40, height=16,font = ("휴면엑스포", 12, "bold"), yscrollcommand=self.BookMarkScroll.set,  selectbackground = "orange", selectforeground = "black", selectborderwidth = 2,
                                    borderwidth = 4, fg = "black", highlightbackground = "gray",highlightthickness = 2, bg = "azure")
        self.AddMainText = Button(self.BookMarkFrame, text = "Mail\n추가", width = 6, bg = "light blue",font=("HYHeadLine", 10, "bold"), command = self.AddMainText)
        self.AddBookMark= Button(self.BookMarkFrame, text="북마크\n불러오기", width = 6, bg="light blue", font=("HYHeadLine", 10, "bold"),command=self.AddBookMarkList)
        #self.AddBookMarkList()

        self.MailFrame = Frame(self.Background, width = self.width / 2, height = 140, bg = "light blue")
        self.MailLabel = Label(self.MailFrame, text = "Gmail 보내기",font=("나눔 고딕", 25, "bold"), bg = "light blue" )
        self.RecvIDLabel = Label(self.MailFrame, text ="Mail 주소 : ", font=("HYHeadLine", 15, "bold"), bg ="light blue")
        self.RecvIDEntry = Entry(self.MailFrame, width = 28, font=("HYHeadLine", 15, "bold"), bg ="light blue")
        self.RecvIDEntry.insert(END, "hayoon9611@gmail.com")
        self.MainLabel = Label(self.MailFrame, text = "Mail 본문",font=("HYHeadLine", 15, "bold"), bg = "light blue" )

        self.MainTextFrame = Frame(self.Background, width = self.width / 2, height = 280,  bg ="light blue")
        self.MainText = Text(self.MainTextFrame, width = 40, height = 14, font=("HYHeadLine", 12, "bold"), bg ="light blue")

        self.MainTextScroll = Scrollbar(self.MainTextFrame)
        self.MainTextScroll.configure(command = self.MainText.yview)



        self.MailButtonFrame = Frame(self.Background, width = self.width / 2, height = 130, bg = "light blue")
        self.SendButton = Button(self.MailButtonFrame, text = "메일 보내기", bg = "light blue", font=("HYHeadLine", 15, "bold"), command = self.Send)

    def AddBookMarkList(self):
        self.BookMarkList.delete(0, len(self.BookMarkInfoList))
        self.BookMarkInfoList.clear()
        #MovieBookMark = self.interface.GetMovieBookMark()
        #for d in MovieBookMark:
        #    self.BookmarkList.append(d)
         #   self.BookMarkList.insert(END, "영화 - " + d[0])
        ActorBookMark = self.interface.ActorList.GetActorBookmark()
        for d in ActorBookMark:
            self.BookMarkInfoList.append(d)
            self.BookMarkList.insert(END, "인물 - " + d[0].replace("이름 ", ""))

        #print(MovieBookMark)
        #print(ActorBookMark)

    def AddMainText(self):
        select = self.BookMarkList.curselection()
        for d in self.BookMarkInfoList[select[0]]:
            self.MainText.insert(END, str(d) + "\n")


    def Send(self):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        sender = 'hayoon9611@gmail.com'
        smtp.login(sender, 'rla118848@')

        text =  self.MainText.get(1.0, END)
        recvid = self.RecvIDEntry.get()
        msg = MIMEText(text)
        msg['subject'] = 'BoxOffice'
        msg['to'] = recvid
        smtp.sendmail(sender, msg['to'], msg.as_string())


    def Render(self):
        self.BookMarkFrame.pack(side = LEFT, fill = Y)
        self.BookMarkLabel.place(x = 10, y = 10)
        self.BookMarkListFrame.place(x = 10, y = 60)
        self.BookMarkScroll.pack(side=RIGHT, fill = Y)
        self.BookMarkList.pack()
        self.AddBookMark.place(x = 405, y = 60)
        self.AddMainText.place(x = 405, y = 120)

        self.MailFrame.pack()
        self.MailLabel.place(x = 10, y = 10)
        self.RecvIDLabel.place(x = 10, y = 60)
        self.RecvIDEntry.place (x = 120, y = 60)
        self.MainLabel.place(x = 10, y = 100)

        self.MainTextFrame.pack(side = TOP)
        self.MainTextScroll.pack(side = RIGHT,  fill = Y)
        self.MainText.pack(anchor="s")

        self.MailButtonFrame.pack()
        self.SendButton.place(x = 310, y = 10)

    def GetFrame(self):
        return self.Background

if __name__ == '__main__':
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('hayoon9611@gmail.com', 'rla118848@')

    msg = MIMEText('본문테스트 메시지')
    msg['subject'] = '제목?'
    msg['to'] = 'hayoon9611@gmail.com'
    smtp.sendmail(msg['to'], msg['to'], msg.as_string())

    smtp.quit()
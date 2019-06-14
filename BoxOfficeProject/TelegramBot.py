#-*- coding: utf-8 -*-
import telepot
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import copy

# 텔레그램
# 835222947:AAE3d-gEnxi63uVa4pwKf9y5FLeJh3lZanA

# chat id
# 805144083

#http://developwoong.blogspot.com/2018/11/cgv.html
# + 구글 검색 api

class TeleBot:
    def __init__(self, interface):
        self.tokken = '835222947:AAE3d-gEnxi63uVa4pwKf9y5FLeJh3lZanA'
        self.chatID = '805144083'
        self.bot = telepot.Bot(self.tokken)

        self.SendMessage("영화 박스오피스 텔레그램 봇이 실행되었습니다.")
        self.Help()
        self.Program = copy.copy(interface)
    def __del__(self):
        self.SendMessage("영화 박스오피스 텔레그램 봇이 종료되었습니다.")

    def SendMessage(self, text):
        self.bot.sendMessage(self.chatID, str(text))

    def Message_Loop(self):
        self.bot.message_loop(self.handle)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.SendMessage('잘못된 명령어입니다.')
            self.Help()
            return

        text = msg['text']
        list = text.split(' ')
        if list[0] == "일간" or list[0] == "주간":
            Data = self.Program.GetRanking(list)
            if Data == None:
                self.SendMessage('잘못된 명령어입니다. 다시 확인해주세요')
                self.Help()
            else:
                for data in Data:
                    self.SendMessage(data)

    def Help(self):
        text = "======= 명령어 ======= \n"
        text = text + "일간      날짜(yyyymmdd) \n"
        text = text + "주간      날짜(yyyymmdd) \n"
        text = text + "영화      영화이름 \n"
        text = text + "배우      배우이름 \n"
        text = text + "영화관   주소 \n"
        text = text + "ex) 일간 20190601 \n"
        text = text + "ex) 영화관 정왕동"
        self.SendMessage(text)


if __name__ == '__main__':  # ReadData.py를 실행시킬때만 실행되는 내용
    bot = TeleBot()

    bot.Message_Loop()
    while 1:
        time.sleep(10)
else:
    pass
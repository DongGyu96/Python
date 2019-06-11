#-*- coding: utf-8 -*-
import telepot
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

# 텔레그램
# 835222947:AAE3d-gEnxi63uVa4pwKf9y5FLeJh3lZanA

# chat id
# 805144083

#http://developwoong.blogspot.com/2018/11/cgv.html
# + 구글 검색 api

class TeleBot:
    def __init__(self):
        self.tokken = '835222947:AAE3d-gEnxi63uVa4pwKf9y5FLeJh3lZanA'
        self.chatID = '805144083'
        self.bot = telepot.Bot(self.tokken)
        print(self.bot.getMe())

        url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/' \
              'getRTMSDataSvcAptTrade' \
              '?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D' \
              '&LAWD_CD=11110' \
              '&DEAL_YMD=201712'
        response = urlopen(url).read()
        Data = BeautifulSoup(response, "html.parser")
        #print(Data)
        self.Help()

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
        args = text.split(' ')
        print(text)
        print(args)
        print(args[0])
        print(args[1])

    def Help(self):
        text = "일간 날짜(yyyymmdd) \n"
        text = text + "주간 날짜(yyyymmdd) \n"
        text = text + "영화 영화이름 \n"
        text = text + "배우 배우이름"
        self.SendMessage(text)


if __name__ == '__main__':  # ReadData.py를 실행시킬때만 실행되는 내용
    bot = TeleBot()

    bot.Message_Loop()
    while 1:
        time.sleep(10)
else:
    pass

class Actor():
    def __init__(self, code, name, field):
        self.Code = code            # 코드
        self.Name = name            # 이름
        self.Field = field          # 분야

    def GetCode(self):
        return self.Code


    def GetName(self):
        return self.Name

    def SetName(self, cnt):
        self.Name = self.Name + str(cnt)

    def GetField(self):
        return self.Field


class ActorManager():
    def __init__(self):
        self.ActorList = []
        self.index = 0

    def SetActor(self, actor):#
        #for i in self.ActorList:
        #    if actor.GetName() == i.GetName():
        #        i = self.GetSameNameCnt(actor.GetName())
        #        actor.SetName(i)

        self.ActorList.insert(self.index, actor)
        self.index += 1


    def FindCodeFromName(self, name):
        #if name.isdigit:
        #    i = len(name)
        #    cut = name[i - 1]
        #    old = name
        #    print(old)
#
        #    name = old.replace(cut, "")
        #    print(name)

        for actor in self.ActorList:
            if name == actor.GetName():
                return actor.GetCode()

            else:
                return None

    def FindNameFromCode(self, code):
        for actor in self.ActorList:
            if code == actor.GetCode():
                return actor.GetName()

            else:
                return None


    def GetSameNameCnt(self, name):
        cnt = 0
        for actor in self.ActorList:
            if name == actor.GetName():
                cnt += 1

        return cnt

    def FindCodeFromIndex(self, index):
        code = self.ActorList[index].GetCode()
        return code

    def FindNameFromIndex(self, index):
        name = self.ActorList[index].GetName()
        return name


    def Clear(self):
        self.ActorList.clear()
        self.index = 0

#import urllib.request as req
#import urllib.parse
#import json
#import urllib.request

#encText = urllib.parse.quote("강호동배우")
#url ="https://people.search.naver.com/search.naver?sm=tab_hty&where=nexearch&query="+ encText + "&ie=utf8&x=0&y=0"
#request = urllib.request.Request(url)
#print(url)
#response = urllib.request.urlopen(request)
#rescode = response.getcode()
#if rescode == 200:
#    response_body = response.read()
#    print(response_body)

#import requests
#from bs4 import  BeautifulSoup
import urllib.parse
#encText = urllib.parse.quote("공유")
#url ="https://people.search.naver.com/search.naver?sm=tab_hty&where=nexearch&query="+ encText + "&ie=utf8&x=0&y=0"
#url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=" + "공유"
#print(url)
#response = requests.get(url)
#print(response)
#result = BeautifulSoup(response.text, 'html.parser')
#print(response.text)
#result.find_all('div', 'class':'result_profile'')
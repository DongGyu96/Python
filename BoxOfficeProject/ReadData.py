#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse
from openpyxl import load_workbook
from tkinter import *
import http.client
import geocoder
import json
import requests
import os
import sys
from io import BytesIO
import urllib
import urllib.request
from PIL import Image,ImageTk
import webbrowser

import socket

DAILY = (0,)
WEEKLY = (1,)

THEATERnum = 0
THEATERID = 4
THEATERname = 15
THEATERstartdate = 5
THEATERlastdate = 18
THEATERstate = 6
THEATERcall = 10
THEATERaddress = 13
THEATERprevaddress = 12
THEATERx = 19
THEATERy = 20
THEATERtype = 22


def LoadXMLFromFileBoxOffice(type, date):
    # type == 1 : 일간 박스오피스
    # else : 주간 박스오피스
    # date = yyyymmdd   ex)20190330
    if type == DAILY:
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"
    else:
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml"
    key = "70fb64767aa3cd31fb488fe55820bf17"
    url = url + "?key=" + key +"&targetDt=" + str(date)
    data = urllib.request.urlopen(url).read()
    Data = BeautifulSoup(data, "html.parser")
    return Data

def LoadXMLFromFileMovieInfo(code):
    # 영화 코드로 조회하는 영화 상세정보 movieCd값
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml"
    key = "e4ef9cc26c8da2fbd710c5899e835cd7"
    url = url + "?key=" + key +"&movieCd=" + code
    data = urllib.request.urlopen(url).read()

    Data = BeautifulSoup(data, "html.parser")
    return Data

Filter = ["엄마", "팬티", "불륜", "무삭제", "섹스", "은밀", "유부녀", "숙모", "형수", "섹드립", "스와핑", "탐하기", "초흥분", "흠뻑", "오르가즘", "출장", "음란",
          "여고생", "장모님", "친구 누나", "의붓", "여동생", "친척 누나", "여직원", "친척누나", "누나 친구", "정사", "친구아빠", "발정", "알몸", "여사장", "비밀수업", "나의 노예", "순결", "딸의 친구", "친구 아내", "업소녀",
          "하숙집", "꼴리는", "색정", "명기", "여비서", "육덕", "여닌자", "착한 이모", "남편", "처제"]
def LoadXMLFromFileMovieList(page, name):
    # 영화 목록
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml"
    key = "70fb64767aa3cd31fb488fe55820bf17"
    url = url + "?key=" + key + "&curPage=" + str(page) + "&itemPerPage=50"
    if name != None:
        name = urllib.parse.quote(name)
        url = url + "&movieNm=" + name
    data = urllib.request.urlopen(url).read()

    Data = BeautifulSoup(data, "html.parser")
    return Data


# 배우 목록 데이터
def LoadXMLFromFileActorList(page, name, movie):
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.xml"
    key = "70fb64767aa3cd31fb488fe55820bf17"
    url = url + "?key=" + key + "&curPage=" + str(page) + "&itemPerPage=50"
    if name != None: # 배우 이름
        name = urllib.parse.quote(name)
        url = url + "&peopleNm=" + name
        # url = url.encode('utf-8')
    if movie != None: # 필모리스트
        movie = urllib.parse.quote(movie)
        url = url + "&filmoNames=" + movie
    data = urllib.request.urlopen(url).read()
    Data = BeautifulSoup(data, "html.parser")
    return Data

#데이터를 뽑아낼 때
#Data = LoadXMLFromFileActorList(1, None, None) 만약 다른 검색 없이 전체 목록만 뽑아낸다면
#1, "김", None 이면 배우이름에 김이 들어가는 영화배우들
#1, None, "ㅁㄴㅇ" 이면 ㅁㄴㅇ라는 영화에 출연한 영화배우들
#page값으로 다음페이지로 넘어갈수있음

# 뽑고나서는 for data in Data.find_all("peoplelist"): 로 피플리스트에 있는 모든 목록을 돌림 소문자로만 써야함 반드시 대문자도 소문자로
# 그러면 포문에서는 data 한번 돌때마다 피플리스트 하위항목으로 돌아가기 때문에
# 그냥 data.peoplenm 은 <peopleNm>민병우</peopleNm> 로 뜰거임
# data.peoplecd.string 은 코드를 문자열로 나타냄
# data.peoplenm.string 은 이름을 문자열로 나타냄

#<peopleList>
#<people>
#<peopleCd>10027799</peopleCd> 코드값
#<peopleNm>민병우</peopleNm> 이름
#<peopleNmEn>MIN Byung-woo</peopleNmEn> 영어이름
#<repRoleNm>감독</repRoleNm> 직업
#<filmoNames> 몽마르트 드 파파|지구인의 연애론|그 강아지 그 고양이|너는 펫|도둑 고양이들|그녀의 헤어짐</filmoNames> 필모리스트
#</people>

#<people>
#<peopleCd>20325412</peopleCd>
#<peopleNm>신현호</peopleNm>
#<peopleNmEn>SHIN Hyun-ho</peopleNmEn>
#<repRoleNm>감독</repRoleNm>
#<filmoNames>럭스</filmoNames>
#</people>


def LoadXMLFromFileActorInfo(code):
    # 배우 코드로 조회하는 영화 상세정보 peopleCd값
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.xml"
    key = "e4ef9cc26c8da2fbd710c5899e835cd7"
    url = url + "?key=" + key +"&peopleCd=" + str(code)
    data = urllib.request.urlopen(url).read()
    Data = BeautifulSoup(data, "html.parser")
    return Data

def LoadXLSFromFileTheater():
    Data = load_workbook(filename = "Theater.xlsx")
    Data = Data.worksheets[0]
    return Data

def LoadNaverAPIToMovie(moviename):
    client_id = "CauJEcypbFDul3iDdw3V"
    client_secret = "1gsH15h8bj"
    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText  # json 결과
    #url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        return json.loads(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        return None

def LoadImageFromURL(url, width, height):
    raw_data = urllib.request.urlopen(url).read()
    im = Image.open(BytesIO(raw_data))
    im = im.resize((width, height))
    data = ImageTk.PhotoImage(im)
    return data

def LoadNaverAPIToImage(name):
    client_id = "CauJEcypbFDul3iDdw3V"
    client_secret = "1gsH15h8bj"
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/image.json?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        return json.loads(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        return None

def LoadNaverAPIToNews(name):
    client_id = "CauJEcypbFDul3iDdw3V"
    client_secret = "1gsH15h8bj"
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return json.loads(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        return None

def OpenWebBrowser(url):
    webbrowser.open_new(url)

def OpenNaverWebBrowser(name):
    name = urllib.parse.quote(name)
    webbrowser.open_new("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + name)

# tkinter 버튼 함수
# command로 인자받는법 : 람다함수 사용
# command = lambda index = i: func(index)


def LoadGoogleAPIMapToURL(lat, lon):
    url = "https://maps.googleapis.com/maps/api/" \
    "staticmap?" \
    "?zoom=5" \
    "&size=295x300" \
    "&maptype=roadmap" \
    "&markers=color:blue%7Clabel:G%7C" + str(lat) + "," + str(lon) + "" \
    "&key=AIzaSyCYpTRneF3xvsbc37jgxbFk5e1AfDAJ8jo"
    raw_data = urllib.request.urlopen(url).read()
    im = Image.open(BytesIO(raw_data))
    data = ImageTk.PhotoImage(im)
    return data
#"&markers=color:green%7Clabel:G%7C40.711614,-74.012318" \
#"&markers=color:red%7Clabel:C%7C40.718217,-73.998284" \

#AIzaSyCYpTRneF3xvsbc37jgxbFk5e1AfDAJ8jo

def LoadNaverAPIToTest(name):
    client_id = "CauJEcypbFDul3iDdw3V"
    client_secret = "1gsH15h8bj"
    encText = urllib.parse.quote(name)
    url = "https://openapi.naver.com/v1/search/webkr.json?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return json.loads(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        return None

def LoadGoogleAPIGeocoding(address):
    address = urllib.parse.quote(address)
    url = "https://maps.googleapis.com/maps/api/geocode/xml?" \
          "address=" + address + ""\
          "&key=AIzaSyCYpTRneF3xvsbc37jgxbFk5e1AfDAJ8jo"
    Data = urllib.request.urlopen(url).read()
    Data = BeautifulSoup(Data, "html.parser")
    address = []
    address.append(Data.find("lat").string)
    address.append(Data.find("lng").string)
    return address

if __name__ == '__main__': # ReadData.py를 실행시킬때만 실행되는 내용
    # ip = geocoder.ip('me').ip
    # url = 'http://ip-api.com/json/' + ip
    # recvd = requests.get(url)
    # loc = json.loads(recvd.text)
    # print(loc)
    # print(loc["lat"])
    # print(loc["lon"])

    # Data = LoadXMLFromFileBoxOffice(DAILY, "20190518")
    # print(Data)

    # Data = LoadNaverAPIToMovie("터치")
    # for data in Data['items']:
    #    print(data['director'].split("|")[0])
    # print(Data['items'])

    # Data = LoadNaverAPIToNews("박보영")
    # image = []
    # print(Data)
    # for data in Data['items']:
    #    print(data['link'])
    #    image.append(LoadImageFromURL1(data['link'], 165, 235))
    #    # link의 이미지가 너무 크면 thumbnail 로 썸네일 이미지로 가져올수도 있음
    url1 = "http://www.lottecinema.co.kr/LCHS/Contents/Cinema/Cinema-Detail.aspx?divisionCode=1&detailDivisionCode=1&cinemaID=1018"
    url2 = "http://www.cgv.co.kr/theaters/?theaterCode=0056"
    data = urllib.request.urlopen(url2).read()
    Data = BeautifulSoup(data, "html.parser")
    print(Data)

    print(LoadNaverAPIToTest("CGV 강남"))
else:
    pass
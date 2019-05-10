#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse
from openpyxl import load_workbook
import http.client
import geocoder
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
THEATERx = 19
THEATERy = 20
THEATERtype = 21


def LoadXMLFromFileBoxOffice(type, date):
    # type == 1 : 일간 박스오피스
    # else : 주간 박스오피스
    # date = yyyymmdd   ex)20190330
    Data = None
    savename = "BoxOffice.xml"
    if type == DAILY:
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"
    else:
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml"
    key = "70fb64767aa3cd31fb488fe55820bf17"
    url = url + "?key=" + key +"&targetDt=" + str(date)
    data = urllib.request.urlopen(url).read()
    text = data.decode('utf-8')

    req.urlretrieve(url, savename)

    xml = open(savename, "r", encoding="utf-8").read()
    Data = BeautifulSoup(xml, "html.parser")
    return Data

def LoadXMLFromFileMovieInfo(code):
    # 영화 코드로 조회하는 영화 상세정보 movieCd값
    Data = None
    savename = "MovieInfo.xml"
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml"
    key = "e4ef9cc26c8da2fbd710c5899e835cd7"
    url = url + "?key=" + key +"&movieCd=" + str(code)
    data = urllib.request.urlopen(url).read()
    text = data.decode('utf-8')
    req.urlretrieve(url, savename)

    xml = open(savename, "r", encoding="utf-8").read()
    Data = BeautifulSoup(xml, "html.parser")
    return Data

def LoadXMLFromFileMovieList(page, name):
    # 영화 목록
    Data = None
    savename = "MovieList.xml"
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml"
    key = "70fb64767aa3cd31fb488fe55820bf17"
    url = url + "?key=" + key + "&curPage=" + str(page) + "&itemPerPage=50"
    if name != None:
        name = urllib.parse.quote(name)
        url = url + "&movieNm=" + name
        #url = url.encode('utf-8')
    data = urllib.request.urlopen(url).read()
    req.urlretrieve(url, savename)

    xml = open(savename, "r", encoding="utf-8").read()
    Data = BeautifulSoup(xml, "html.parser")
    return Data


def LoadXLSFromFileTheater():
    Data = load_workbook(filename = "Theater.xlsx")
    Data = Data.worksheets[0]
    return Data

def NaverAPI():
    server = 'openapi.naver.com'
    client_id = 'CauJEcypbFDul3iDdw3V'
    client_secret = '1gsH15h8bj'
    conn = http.client.HTTPSConnection(server)
    conn.request('GET', '/v1/serch/book.xml?query=love&display=10&start=1',None,
                 {'X-Naver-Clinet-Id':client_id, 'X-Naver-Client-Secret':client_secret})
    req = conn.getresponse()
    cLen = req.getheader("Content-Length")
    req.read(int(cLen))

# tkinter 버튼 함수
# command로 인자받는법 : 람다함수 사용
# command = lambda index = i: func(index)

if __name__ == '__main__':
    myloc = geocoder.ip(socket.gethostbyname(socket.gethostname()))
    print(socket.gethostbyname(socket.gethostname()))
    print(myloc.latlng)
    print(myloc.city)
    print(myloc.ip)

    myloc = geocoder.ip('me')
    print(myloc.latlng)
    print(myloc.city)
    print(myloc.ip)
else:
    pass
class Stock:
    def __init__(self, symbol, name,
                 previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
    def getName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price
    def getCurrentPrice(self):
        return self.__currentPrice
    def setCurrentPrice(self, price):
        self.__currentPrice = price
    def getChangePercent(self):
        gap = self.__currentPrice - self.__previousClosingPrice
        return gap / self.__previousClosingPrice * 100

code = input("주식 코드 : ")
name = input("종목 명 : ")
prePrice = eval(input("전일종가 : "))
curPrice = eval(input("현재가 : "))
stock = Stock(code, name, prePrice, curPrice)
print("가격 변동률 :", stock.getChangePercent(), "%")
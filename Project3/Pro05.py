import math
class Triangle:
    def __init__(self):
        self.side1 = 1.0
        self.side2 = 1.0
        self.side3 = 1.0
        self.color = "White"
        self.fill = False
    def __init__(self, side1, side2, side3, color, fill):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color
        self.fill = fill
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def getColor(self):
        return self.color
    def getFill(self):
        if self.fill == True:
            return True
        else:
            return False
    def setSide1(self, side):
        self.side1 = side
    def setSide2(self, side):
        self.side2 = side
    def setSide3(self, side):
        self.side3 = side
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def __str__(self):
        return "Triangle : Side1 = " + str(self.side1) + " Side2 = " + \
               str(self.side2) + " Side3 = " + str(self.side3)

side1 = eval(input("첫번째 변의 길이를 입력하세요 : "))
side2 = eval(input("두번째 변의 길이를 입력하세요 : "))
side3 = eval(input("세번째 변의 길이를 입력하세요 : "))
color = input("삼각형의 색상을 입력하세요 : ")
fill = eval(input("삼각형 내부가 채워져있습니까? (0 : 비움, 1: 채움) : "))
triangle = Triangle(side1, side2, side3, color, fill)
print(triangle)
print("삼각형의 넓이 : ", triangle.getArea())
print("삼각형의 둘레 : ", triangle.getPerimeter())
print("삼각형의 색상 : ", triangle.getColor())
if triangle.getFill():
    print("삼각형 내부는 채워져있음")
else:
    print("삼각형 내부는 채워져있지 않음")
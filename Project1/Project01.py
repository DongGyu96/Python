import math

x1, y1, x2, y2, x3, y3 = eval(input("삼각형의 세 꼭지점을 입력하세요 : "))

side1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
side2 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
side3 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
print("삼각형의 넓이는 ", area, "입니다. ")
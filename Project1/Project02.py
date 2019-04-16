import math

x1, y1 = eval(input("첫 번쨰 점(위도와 경도)을 60분법 각으로 입력하세요 : "))
x2, y2 = eval(input("두 번쨰 점(위도와 경도)을 60분법 각으로 입력하세요 : "))

d = 6370.01 * math.acos((math.sin(math.radians(x1)) * math.sin(math.radians(x2))) +
                        (math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                         math.cos(math.radians(y1 - y2))))

print("두 점 사이의 거리는 ", d, "km입니다. ")
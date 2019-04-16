import math
seoulx = 37.565289
seouly = 126.8491259
busanx = 35.1645701
busany = 129.0015892
gwangjux = 35.1768201
gwangjuy = 126.7735892
gangwonx = 37.7637326
gangwony = 128.8824475
radius = 6370.01
def FindSide(x1, y1, x2, y2):
        return radius * math.acos((math.sin(math.radians(x1)) * math.sin(math.radians(x2))) +
                                  (math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                                   math.cos(math.radians(y1 - y2))))
def FindArea(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

seoultobusan = FindSide(seoulx, seouly, busanx, busany)
seoultogwangju = FindSide(seoulx, seouly, gwangjux, gwangjuy)
gwangjutobusan = FindSide(gwangjux, gwangjuy, busanx, busany)
area1 = FindArea(seoultobusan, seoultogwangju, gwangjutobusan)

seoultogangwon = FindSide(seoulx, seouly, gangwonx, gangwony)
gangwontobusan = FindSide(gangwonx, gangwony, busanx, busany)
area2 = FindArea(seoultogangwon, seoultobusan, gangwontobusan)

print("서울 강원 부산 광주간의 추정 넓이는 ", area1 + area2, "입니다.")



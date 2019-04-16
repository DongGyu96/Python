import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def FindDistance(self):
        return math.sqrt((self.x**2) + (self.y**2))

def getRightmostLowestPoint(points):
    max = 0
    mp = Point(0, 0)
    p = [Point(0, 0) for i in range(len(points)//2)]
    for i in range(0, len(points), 2):
        p[i // 2].x = points[i]
        p[i // 2].y = points[i+1]
        print(p[i//2].x, p[i//2].y)

    for i in range(len(points)//2):
        if max < p[i].FindDistance():
            if p[i].y < 0 and p[i].x > 0:
                max = p[i].FindDistance()
                mp = p[i]

    return mp

arr = []
arr = input("번에 대한 원소를 입력하세요 : ")
arr = [eval(x) for x in arr.split()]
arr = list(map(float, arr))

point = getRightmostLowestPoint(arr)
print("최우측하단의 점은 (", point.x, ",", point.y,  ")입니다")
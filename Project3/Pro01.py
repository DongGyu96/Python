class Rectangle:
    def __init__(self):
        self.width = 1
        self.height = 2
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return 2 * (self.width + self.height)

Rect1 = Rectangle(4, 10)
Rect2 = Rectangle(3.5, 35.7)

print("Rectangle1의 넓이 : ", Rect1.getArea())
print("Rectangle1의 넓이 : ", Rect1.getPerimeter())

print("Rectangle2의 넓이 : %0.2f" % Rect2.getArea())
print("Rectangle2의 넓이 : ", Rect2.getPerimeter())
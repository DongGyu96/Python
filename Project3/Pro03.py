class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self):
        self.__speed = self.SLOW
        self.__on = False
        self.__radius = 5
        self.__color = "Blue"
    def __init__(self, speed, on, radius, color):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    def getSpeed(self):
        return self.__speed
    def setSpeed(self, speed):
        self.__speed = speed
    def getPower(self):
        return self.__on
    def setPower(self, on):
        self.__on = on
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color

fan1 = Fan(3, True, 10, "Yellow")
fan2 = Fan(2, False, 5, "Blue")

print("Fan1의 속도 : ", fan1.getSpeed())
print("Fan1의 반지름 : ", fan1.getRadius())
print("Fan1의 색상 : ", fan1.getColor())
print("Fan1의 전원 : ", fan1.getPower())
print("================================")
print("Fan2의 속도 : ", fan2.getSpeed())
print("Fan2의 반지름 : ", fan2.getRadius())
print("Fan2의 색상 : ", fan2.getColor())
print("Fan2의 전원 : ", fan2.getPower())


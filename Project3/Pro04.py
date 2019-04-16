import time

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = 0
    def getStart(self):
        return self.__startTime
    def getEnd(self):
        return self.__endTime
    def Start(self):
        self.__startTime = time.time()
    def Stop(self):
        self.__endTime = time.time()
    def getElaspedTime(self):
        return (self.__endTime - self.__startTime) * 1000

stopwatch = StopWatch()
sum = 0
stopwatch.Start()
for i in range(1000000):
    sum += i
stopwatch.Stop()
print("소요된 시간 : %0.1f" % stopwatch.getElaspedTime(), "ms")
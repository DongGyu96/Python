import random

count = 0
for i in range(1000000):
    x = random.randrange(-100, 101)
    y = random.randrange(-100, 101)
    if x > 0 and y > 0 and x < 100 and y < 100:
        x1 = x - 100;
        if y/x1 > -1.0:
            count += 1
    if x > 0 and y < 0:
        count += 1
print("1번 삼각형과 3번 사각형 내부를 맞힌 다트의 수는",count)
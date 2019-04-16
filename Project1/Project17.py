import random

balls = eval(input("떨어뜨릴 공의 개수를 입력하세요 : "))
size = eval(input("콩 기계의 슬릇 개수를 입력하세요 : "))
ballsroute = [[0] * (size - 1) for i in range(balls)]
slots = [0] * size
max = 0

for i in range(balls):
    count = 0
    for j in range(size - 1):
        ballsroute[i][j] = random.randrange(0, 2)
        if ballsroute[i][j] == 1:
            count += 1
            print("R ", end='')
        else:
            print("L ", end='')
    slots[count] += 1
    if max < slots[count]:
        max = slots[count]
    print()

for i in range(balls):
    for j in range(size):
        if max == slots[j]:
            print("0 ", end='')
            slots[j] -= 1
        else:
            print("  ", end='')
    max -= 1
    if max == 0:
        break
    print()
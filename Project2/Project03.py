gradient = 100 / -200

x, y = eval(input("점 x와 y의 좌표값을 입력하세요 : "))

x -= 200

if gradient > y / x:
    print("점은 삼각형 내부에 있습니다,")
else:
    print("점은 삼각형 내부에 있지 않습니다,")
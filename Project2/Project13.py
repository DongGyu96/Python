count = 0
def main():
    global count
    n = eval(input("디스크의 개수를 입력하세요 : "))
    print("옮기는 순서는 다음과 같습니다")
    moveDisks(n, 'A', 'B', 'C')
    print("총 이동 횟수는 : ", count, "입니다")

def moveDisks(n, fromTower, toTower, auxTower):
    global count
    count += 1
    if n==1:
        print("디스크", n, "을/를", fromTower,"에서",toTower,"로 옮긴다")
    else:
        moveDisks(n-1,fromTower, auxTower, toTower)
        print("디스크", n, "을/를", fromTower, "에서", toTower, "로 옮긴다")
        moveDisks(n-1, auxTower, toTower, fromTower)

main()
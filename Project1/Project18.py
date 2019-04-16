def sumColumn(m, columnIndex):
    sum = 0
    for i in range(3):
        sum += m[i][columnIndex]
    return sum


arr = [[0] * 4 for i in range(3)]

for i in range(3):
    print("3X4 행렬의 행", i, end = ' ')
    arr[i] = input("번에 대한 원소를 입력하세요 : ")
    arr[i] = [eval(x) for x in arr[i].split()]
    arr[i] = list(map(float, arr[i]))

for i in range(4):
    print("열 ", i, "번 원소의 총 합은 ",sumColumn(arr, i), "입니다.")
def sortColums(m):
    sortList = [[0] * 3 for i in range(3)]
    List = [[0] * 3 for i in range(3)]

    for i in range(3):
        for j in range(3):
            sortList[i][j] = m[j][i]
        sortList[i].sort()
    for i in range(3):
        for j in range(3):
            List[i][j] = sortList[j][i]

    return List

arr = []
arr = [[0] * 3 for i in range(3)]

print("3x3행렬을 한 행씩 입력하세요")
for i in range(0, 3):
    arr[i] = input()
    arr[i] = [eval(x) for x in arr[i].split()]

sortList = sortColums(arr)
for i in range(0, 3):
    print(sortList[i])
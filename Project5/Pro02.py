def ToInt(list):
    size = len(list)
    num = 0
    if list[0] == "-":
        for i in range(1, len(list)):
            num += int(list[i]) * (10 ** (size - i - 1))
        num *= -1
    else:
        for i in range(len(list)):
            num += int(list[i]) * (10 ** (size - i - 1))
    return num

count = eval(input(""))

for num in range(count):
    day = eval(input(""))
    A = []
    B = []
    C = []
    result = 0
    for i in range(day):
        list = input("")
        cnt = 0
        temp = 0
        for j in range(len(list)):
            if list[j] == " ":
                cnt += 1
                if cnt == 2:
                    tempList = []
                    for x in range(0, temp):
                        tempList.append(list[x])
                    A.append(ToInt(tempList))
                    tempList = []
                    for y in range(temp + 1, j):
                        tempList.append(list[y])
                    B.append(ToInt(tempList))
                    tempList = []
                    for z in range(j + 1, len(list)):
                        tempList.append(list[z])
                    C.append(ToInt(tempList))
                else:
                    temp = j
        if A[i] > B[i]:
            if A[i]  > C[i]:
                if A[i] > 0:
                    result += A[i]
            else:
                if C[i] > 0:
                    result += C[i]
        else:
            if B[i] > C[i]:
                if B[i] > 0:
                    result += B[i]
            else:
                if C[i] > 0:
                    result += C[i]
    print(result)
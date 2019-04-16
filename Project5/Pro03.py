T = eval(input(""))
for x in range(T, 0, -1):
    N = eval(input(""))
    c1 = input("")
    c2 = input("")
    wbCnt = 0
    bwCnt = 0
    for i in range(N):
        if c1[i] == "W" and c2[i] == "B":
            wbCnt += 1
        elif c1[i] =="B"and c2[i]=="W":
            bwCnt += 1
    if wbCnt <= bwCnt:
        print(bwCnt)
    else:
        print(wbCnt)
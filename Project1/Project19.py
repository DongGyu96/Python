arr = []
arr = input("정수 리스트를 입력하세요 : ")
arr = [eval(x) for x in arr.split()]
countarr = {}
max = 0

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if arr[i] not in countarr:
        if max < count:
            max = count
        countarr.update({arr[i] : count})

for key, value in countarr.items():
    if max == value:
        print(key, " 원소 - ", value, "개.")
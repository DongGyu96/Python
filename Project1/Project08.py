inputarr = []

inputarr =input("1과 100 사이의 정수를 입력하세요 : ")
arr = inputarr.split(" ")
countarr = {}

count = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if arr[i] not in countarr:
        countarr.update({arr[i] : count})
    count = 0

for key, value in countarr.items():
    print(key, " - ", value, "번 나타납니다.")
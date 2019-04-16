inputarr = []

inputarr =input("정수 리스트를 입력하세요 : ")
arr = inputarr.split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
check = False
arr2 = []
for i in range(len(arr)):
    if arr[i] not in arr2:
        arr2.append(arr[i])

print("중복을 제거한 고유한 숫자 : ", arr2)
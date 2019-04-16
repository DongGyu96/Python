inputarr = []

inputarr =input("정수 리스트를 입력하세요 : ")
arr = inputarr.split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.reverse()
print(arr)

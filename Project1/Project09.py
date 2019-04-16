inputarr = []

inputarr =input("정수 리스트를 입력하세요 : ")
arr = inputarr.split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])
avg = 0
count = 0
downscoreArr = []
upscoreArr = []
for i in range(len(arr)):
    avg = avg + arr[i]
    count += 1
avg = avg / count
print("평균 정수는 : ", avg)

for i in range(len(arr)):
    if arr[i] >= avg:
        upscoreArr.append(arr[i])
    elif arr[i] < avg:
        downscoreArr.append(arr[i])
print("평균이상정수는 : ", upscoreArr)
print("평균이하정수는 : ", downscoreArr)
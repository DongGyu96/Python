def indexOfSmallestElement(lst):
    min = lst[0]
    index = 0
    for i in range(len(lst)):
        if min > lst[i]:
            min = lst[i]
            index = i
    return index

inputarr = []

inputarr =input("정수 리스트를 입력하세요 : ")
arr = inputarr.split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

index = indexOfSmallestElement(arr)
print("가장 작은 원소의 인덱스는 ", index, "입니다.")
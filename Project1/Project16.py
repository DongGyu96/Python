def isSorted(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True

inputarr = []
for a in range(0, 2):
    inputarr = input("정수 리스트를 입력하세요 : ")
    arr = inputarr.split(" ")
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    if isSorted(arr):
        print("리스트는 이미 정렬되어 있습니다.")
    else:
        print("리스트는 정렬되어 있지 않습니다.")
def displaySortedNumbers(num1, num2, num3):
    arr = [num1, num2, num3]
    for i in range(3):
        for j in range(i, 3):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    print("정렬된 숫자는 : ", arr, "입니다.")

n1, n2, n3 = eval(input("세 개의 수를 입력하세요 : "))
displaySortedNumbers(n1,n2,n3)
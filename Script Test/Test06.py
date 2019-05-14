list = input("영단어들 입력 : ")
list = list.replace(" ", "")
print(list)
countarr = {}

count = 0
for i in range(len(list)):
    for j in range(len(list)):
        if (list[i] == list[j]):
            count += 1
    if list[i] not in countarr:
        countarr.update({list[i] : count})
    count = 0
for key, value in countarr.items():
    print(key, "빈도수 : ", value)
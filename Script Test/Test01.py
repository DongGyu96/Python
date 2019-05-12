def Slump(*strs):
    result = []
    list = strs[0]
    list = list.replace('"', "")
    list = list.replace(' ', "")
    list = list.split(',')

    for i in range(len(list)):
        if list[i][0] == 'D' or list[i][0] == 'E':
            for j in range(1, len(list[i])):
                if (list[i][j] != "D" and list[i][j] != "E") and (list[i][j] != "F" and list[i][j] != "G"):
                    result.append("NO")
                    break
                elif list[i][j] == "D" or list[i][j] == "E" or list[i][j] == "G":
                    if list[i][j - 1] != "F":
                        result.append("NO")
                        break
                if j == len(list[i]) - 1:
                    if list[i][j] == "F":
                        result.append("NO")
                    else:
                        result.append("YES")
        else:
            result.append("NO")

    return result


list = input("Slump : ")

print(Slump(list))

filename = input("파일이름을 입력하세요 : ")
removestr = input("제거할 문자열을 입력하세요 : ")

f = open(filename, 'r')
lines = f.readlines()
f.close()

f=open(filename, 'w')
for line in lines:
    if removestr in line:
        f.write(line.replace(removestr, ""))
        print(removestr, "삭제완료")
    else:
        f.write(line)

f.close()
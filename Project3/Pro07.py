filename = input("파일이름을 입력하세요 : ")

f = open(filename, 'r')

lines = f.readlines()

count = 0
wordCount = 0
lineCount = 0

for line in lines:
    lineCount += 1
    count += len(line)
    count -= line.count(' ')
    count -= line.count('\n')
    wordCount += line.count(' ')
    wordCount += line.count('\n')
    if line[-1] != '\n':
        wordCount += 1

print("문자 :", count, "개")
print("단어 :", wordCount, "개")
print("행 :", lineCount, "개")

f.close()

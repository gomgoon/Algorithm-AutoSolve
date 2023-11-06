n = int(input())
result=0
for _ in range(n):
    countList = [0] * 26
    strArray = input()
    c = ''
    for i in range(0,len(strArray)):
        if countList[ord(strArray[i])-ord('a')] == 0:
            c = strArray[i]
            countList[ord(strArray[i])-ord('a')] = 1
        else:
            if c == strArray[i]:
                continue
            else:
                result -= 1
                break
    result += 1
print(result)
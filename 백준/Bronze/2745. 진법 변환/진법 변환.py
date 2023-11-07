stringVal, numVal = input().split()
stringVal = list(stringVal)
stringVal.reverse()
stringVal = ''.join(stringVal)
numVal=int(numVal)
result=0
for i in range(len(stringVal)):
    if stringVal[i] >= 'A' and stringVal[i] <= 'Z':
        num = 10 + ord(stringVal[i]) - ord('A')
    else:
        num = int(stringVal[i])
    num = num * (numVal**(i))
    result+=num
print(result)
        

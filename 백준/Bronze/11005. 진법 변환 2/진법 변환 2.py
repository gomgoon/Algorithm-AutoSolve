n,b = map(int, input().split())
i = 1
stringVal=[]
while n != 0:
    a = n%b
    n -= a
    n = int(n/b)
    if a > 9:
        stringVal.append(chr(ord('A') + (a-10)))
    else:
        stringVal.append(str(a))
stringVal.reverse()
stringVal = ''.join(stringVal)
print(stringVal)
strArray = input()
result = 0
for i in range(len(strArray)):
    if strArray[i] in 'ABC': result += 2
    elif strArray[i] in 'DEF': result += 3
    elif strArray[i] in 'GHI': result += 4
    elif strArray[i] in 'JKL': result += 5
    elif strArray[i] in 'MNO': result += 6
    elif strArray[i] in 'PQRS': result += 7
    elif strArray[i] in 'TUV': result += 8
    else: result += 9
print(result + len(strArray))
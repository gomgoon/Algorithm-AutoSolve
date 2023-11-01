n = int(input())
for _ in range(n):
    strArray=input()
    strLength = len(strArray)
    print(f"{strArray[0]}{strArray[strLength-1]}")
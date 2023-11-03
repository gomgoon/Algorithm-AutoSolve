n = int(input())
numList = list(map(int, input().split()))
maxNum = max(numList)
result = 0
for i in range(0,n):
    numList[i] = numList[i] / maxNum * 100
    result += numList[i]
print(f"{result/n}")
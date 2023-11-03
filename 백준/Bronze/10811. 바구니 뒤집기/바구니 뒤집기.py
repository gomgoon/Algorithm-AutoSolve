n,m = map(int, input().split())
numList = list(range(1,n+1))
for _ in range(m):
    i,j = map(int, input().split())
    numList[i-1:j] = reversed(numList[i-1:j])

for i in range(n):
    print(f"{numList[i]}", end=' ')
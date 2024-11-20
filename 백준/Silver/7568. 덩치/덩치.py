n = int(input())
arr = []
dungchi = []

for _ in range(n):
    x,y = map(int, input().split())
    dungchi.append([x,y])

for d in dungchi:
    n = 1
    for u in dungchi:
        if d[0] < u[0] and d[1] < u[1]:
            n+=1
    arr.append(n)

for rank in arr:
    print(rank, end=' ')
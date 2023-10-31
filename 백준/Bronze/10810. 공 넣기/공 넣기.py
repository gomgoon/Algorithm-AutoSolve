n,m = map(int,input().split())
lis = [0 for _ in range(n)]
for i in range(0,m):
    a,b,c = map(int,input().split())
    for j in range(a-1,b):
        lis[j]=c
for i in range(n):
    print(f"{lis[i]} ",end='')
n,x=map(int,input().split())
arr = list(map(int,input().split()))
for i in arr:
    if i < x:
        print(f"{i}",end=' ')
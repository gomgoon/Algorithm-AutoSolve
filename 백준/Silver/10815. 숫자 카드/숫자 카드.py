n = int(input())
arr = set(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in arr:
        print(1,end=' ')
    else:
        print(0,end=' ')
t = int(input())
for _ in range(t):
    r,s=input().split()
    r=int(r)
    for i in s:
        for j in range(r):
            print(i, end='')
    print()
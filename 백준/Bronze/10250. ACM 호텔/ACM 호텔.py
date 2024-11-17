t = int(input())
for _ in range(t):
    num = list(map(int, input().split()))
    h = num[2] % num[0]
    if h == 0:
        h = num[0]
    w = ((num[2]-1) // num[0]) + 1
    print(h*100 + w)
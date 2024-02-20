a,b,c,d,e,f = map(int, input().split())
answer = 0
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c and d*i + e*j == f:
            print(i,j)
            answer = 1
            break
    if answer == 1:
        break
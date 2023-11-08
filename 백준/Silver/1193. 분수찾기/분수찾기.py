n = int(input())
x,y=1,1
maxNum=1
for i in range(n):
    if i == n-1:
        if maxNum % 2 == 0:
            print(f"{x}/{y}")
        else:
            print(f"{y}/{x}")
    else:
        if x == maxNum:
            maxNum += 1
            y = maxNum
            x = 1
        else:
            y -= 1
            x += 1
t = int(input())
arr = [[i for i in range(1,16)] for _ in range(15)]
for i in range(1,15):
    for j in range(0,15):
        num = 0
        for k in range(0, j+1):
            num += arr[i-1][k]
        arr[i][j] = num
for _ in range(t):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])
n = int(input())
dp = []

for i in range(1, n+1):
    temp = list(map(int, input().split())) + [0] * (n - i)
    dp.append(temp)

for i in range(1, n):
    for j in range(0, n):
        if j != 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j]

print(max(dp[n-1]))
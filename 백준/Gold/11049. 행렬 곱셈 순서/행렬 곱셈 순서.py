n = int(input())
dp = [[0] * n for _ in range(n)]
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    dp[i - 1][i] = arr[i - 1][0] * arr[i - 1][1] * arr[i][1]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + (arr[i][0] * arr[k][1] * arr[j][1]))

print(dp[0][n-1])
            
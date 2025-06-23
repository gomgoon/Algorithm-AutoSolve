n = int(input())

arr = [0] * (n+3)
dp = [0] * (n+3)

for i in range(n):
    num = int(input())
    arr[i] = num

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], dp[1])

for i in range(3, n):
    dp[i] = max(
        dp[i - 1],
        dp[i - 2] + arr[i],
        dp[i - 3] + arr[i - 1] + arr[i]
    )

print(dp[n - 1])
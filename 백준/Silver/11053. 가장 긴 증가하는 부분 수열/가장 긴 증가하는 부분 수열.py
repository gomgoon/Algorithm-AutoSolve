n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    if dp[i] == 0:
        dp[i] = 1

print(max(dp))
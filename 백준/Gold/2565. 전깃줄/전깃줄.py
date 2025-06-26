n = int(input())
arr = []
dp = [1] * (n + 1)

for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    
arr = sorted(arr, key=lambda x: x[0])

for i in range(n):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
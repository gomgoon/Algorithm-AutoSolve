t = int(input())
for _ in range(t):
    
    # 입력
    k = int(input())
    arr = list(map(int, input().split()))
    
    # 누적합 생성
    prefix_sum = [0] * (k+1)
    for i in range(k):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
    
    # 구간 DP 생성
    dp = [[0] * k for _ in range(k)]
    for length in range(2, k + 1):
        for i in range(k - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for t in range(i, j):
                cost = dp[i][t] + dp[t + 1][j] + (prefix_sum[j + 1] - prefix_sum[i])
                dp[i][j] = min(dp[i][j], cost)
    print(dp[0][k - 1])
n, k = map(int, input().split())
things = []
dp = [0] * (k + 1)

for i in range(n):
    arr = list(map(int, input().split()))
    things.append(arr)

things = sorted(things, key = lambda x: x[0])

for i in range(n - 1, -1, -1):
    for j in range(k - 1, -1, -1):
        thing = things[i]
        if thing[0] + j <= k:
            dp[thing[0] + j] = max(dp[thing[0] + j], dp[j] + thing[1])
#print(dp)
print(max(dp))
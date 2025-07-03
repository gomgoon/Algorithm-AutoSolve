import sys 
sys.setrecursionlimit(10**5)

m, n = map(int, input().split())
arr = []
dp = [[-1] * (n) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(m):
    temp = list(map(int, input().split()))
    arr.append(temp)

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    for dir in range(4):
        ny, nx = y + dy[dir], x + dx[dir]
        if 0 <= ny < m and 0 <= nx < n:
            if arr[y][x] > arr[ny][nx]:
                dp[y][x] += dfs(nx, ny)
    return dp[y][x]

print(dfs(0,0))
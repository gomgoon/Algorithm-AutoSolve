from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
res = [[-1 for i in range(m)] for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for j in range(n):
    for i in range(m):
        if arr[j][i] == 2:
            x, y = i, j
            res[y][x] = 0
        if arr[j][i] == 0:
            res[j][i] = 0

queue = deque()
queue.append((y, x))

while queue:
    y, x = queue.popleft()
    num = res[y][x]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and res[ny][nx] == -1:
            res[ny][nx] = num + 1
            queue.append((ny, nx))

for j in range(n):
    for i in range(m):
        print(res[j][i], end=' ')
    print()

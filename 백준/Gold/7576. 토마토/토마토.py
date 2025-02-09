from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(m)]

#방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for j in range(m):
    for i in range(n):
        if arr[j][i] == 1:
            queue.append((j,i))

day = -1

while queue:
    day += 1
    for _ in range(len(queue)):
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and arr[ny][nx] == 0:
                arr[ny][nx] = 1
                queue.append((ny,nx))

for j in range(m):
    for i in range(n):
        if arr[j][i] == 0:
            print(-1)
            exit()

print(day)
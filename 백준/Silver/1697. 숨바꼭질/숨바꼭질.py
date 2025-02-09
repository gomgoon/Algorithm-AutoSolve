from collections import deque

n, k = map(int, input().split())
res = 100000
visited = [-1] * 100001
visited[n] = 0

queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()

    if x == k:
        print(visited[x])
        break

    for nx in (x * 2, x + 1, x - 1):
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            queue.append(nx)
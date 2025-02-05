from collections import deque

def bfs(arr, x, y, m, n):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append((x,y))
    arr[y][x] = 0 # 배추 제거

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
                arr[ny][nx] = 0 # 배추 제거
                queue.append((nx,ny))

def count_worms(m, n, k, positions):
    # 배추밭 배열 초기화
    arr = [[0] * m for _ in range(n)]

    # 배추 심기
    for x, y in positions:
        arr[y][x] = 1
    
    worm_count = 0 # 배추 군집 개수

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                bfs(arr, x, y, m, n)
                worm_count += 1

    return worm_count

t = int(input()) # 테스트 케이스 수
for _ in range(t):
    m, n, k = map(int, input().split())
    positions = [tuple(map(int, input().split())) for _ in range(k)]
    print(count_worms(m, n, k, positions))
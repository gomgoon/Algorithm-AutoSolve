from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    queue = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[-1 for _ in range(101)] for _ in range(101)]
    
    # 경계면 보드 만들기
    for rec in rectangle:
        for x in range(rec[0]*2 , rec[2]*2 + 1):
            for y in range(rec[1]*2, rec[3]*2 + 1):
                if rec[0]*2 < x < rec[2]*2 and rec[1]*2 < y < rec[3]*2:
                    visited[x][y] = 1
                elif visited[x][y] != 1:
                    visited[x][y] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # BFS 실행
    while queue:
        nowX, nowY, step = queue.popleft()
        
        if nowX == itemX * 2 and nowY == itemY * 2:
            return step // 2
    
        for i in range(4):
            nx = nowX + dx[i]
            ny = nowY + dy[i]
            if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                continue
            if visited[nx][ny] != 0:
                continue
            
            queue.append((nx,ny,step+1))
            visited[nx][ny] = 1
    
    return -1
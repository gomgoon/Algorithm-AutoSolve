import sys

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [0] * (n + 1)
num = 1
res = 0
link_arr = []

for i in range(m):
    u, v = map(int, input().split())
    link_arr.append([u, v])

for link in link_arr:
    if visited[link[0]] == 0 and visited[link[1]] == 0:
        #print(f'{link[0]}번 {link[1]}번 {num}번리스트 연결')
        visited[link[0]] = visited[link[1]] = num
        num += 1
    elif visited[link[0]] == 0 and visited[link[1]] != 0:
        #print(f'{link[0]}번 {link[1]}번의 {visited[link[1]]}번리스트 연결')
        visited[link[0]] = visited[link[1]]
    elif visited[link[1]] == 0 and visited[link[0]] != 0:
        #print(f'{link[1]}번 {link[0]}번의 {visited[link[0]]}번리스트 연결')
        visited[link[1]] = visited[link[0]]
    elif visited[link[0]] != visited[link[1]]:
        top = max(visited[link[0]], visited[link[1]])
        bottom = min(visited[link[0]], visited[link[1]])
        for i in range(1, n+1):
            if visited[i] == top:
                visited[i] = bottom

for i in range(1, n + 1):
    if visited[i] == 0:
        res += 1

print(max(visited) + res)
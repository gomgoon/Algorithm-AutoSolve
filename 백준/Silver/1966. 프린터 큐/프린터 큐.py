from collections import deque

queue = deque()
t = int(input())

for i in range(t):
    queue.clear()
    n, m = map(int, input().split())
    res = 1
    arr = list(map(int, input().split()))
    for i in range(n):
        queue.append([i, arr[i]])
    while queue:
        #priority check
        nf = 0
        for i in range(len(queue)):
            if queue[i][1] > queue[0][1]:
                queue.append(queue.popleft())
                nf = 1
                break
        
        if nf == 0:
            arr = queue.popleft()
            if arr[0] == m:
                print(res)
                break
            else:
                res += 1

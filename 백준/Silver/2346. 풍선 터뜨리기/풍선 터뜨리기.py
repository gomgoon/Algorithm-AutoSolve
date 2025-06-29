from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = list(map(int, input().split()))
array = []
for idx, num in enumerate(arr):
    array.append([num, idx])
queue = deque(array)

res = []
while queue:
    direction = queue.popleft()
    res.append(direction[1] + 1)
    if queue:
        if direction[0] > 0:
            for _ in range(direction[0] - 1):
                queue.append(queue.popleft())
        else:
            for _ in range(-direction[0]):
                queue.appendleft(queue.pop())
for i in res:
    print(f"{i} ")
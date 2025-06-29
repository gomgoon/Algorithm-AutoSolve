import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque()
output = []

for _ in range(n):
    cmd = input().strip()
    
    if cmd.startswith("1"):
        queue.appendleft(int(cmd[2:]))
    elif cmd.startswith("2"):
        queue.append(int(cmd[2:]))
    elif cmd == "3":
        output.append(queue.popleft() if queue else -1)
    elif cmd == "4":
        output.append(queue.pop() if queue else -1)
    elif cmd == "5":
        output.append(len(queue))
    elif cmd == "6":
        output.append(0 if queue else 1)
    elif cmd == "7":
        output.append(queue[0] if queue else -1)
    elif cmd == "8":
        output.append(queue[-1] if queue else -1)

print('\n'.join(map(str, output)))

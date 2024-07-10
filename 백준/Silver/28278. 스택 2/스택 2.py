import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
stack = []
index = 1

for _ in range(n):
    command = int(data[index])
    if command == 1:
        x = int(data[index + 1])
        stack.append(x)
        index += 2
    elif command == 2:
        print(stack.pop() if stack else -1)
        index += 1
    elif command == 3:
        print(len(stack))
        index += 1
    elif command == 4:
        print(1 if not stack else 0)
        index += 1
    else:
        print(-1 if not stack else stack[-1])
        index += 1

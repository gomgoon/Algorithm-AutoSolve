from collections import deque

deq_arr = deque()

n = int(input())

for _ in range(n):
    instruction = input().split()
    if instruction[0] == 'push':
        deq_arr.append(int(instruction[1]))
    elif instruction[0] == 'pop':
        if deq_arr:
            print(deq_arr.pop())
        else:
            print(-1)
    elif instruction[0] == 'size':
        print(len(deq_arr))
    elif instruction[0] == 'empty':
        if deq_arr:
            print(0)
        else:
            print(1)
    elif instruction[0] == 'top':
        if deq_arr:
            print(deq_arr[-1])
        else:
            print(-1)

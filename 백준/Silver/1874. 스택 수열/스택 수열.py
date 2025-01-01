from collections import deque

stack = deque()
n = int(input())
idx = 0
num = 1
arr = []

for i in range(n):
    arr.append(int(input()))
res = ''
while True:
    if num > arr[idx]:
        tmp = stack.pop()
        if tmp != arr[idx]:
            print('NO')
            break
        else:
            res += '-\n'
            idx += 1
    else:
        res += '+\n'
        stack.append(num)
        num += 1
    
    if not stack:
        if num > n:
            print(res)
            break
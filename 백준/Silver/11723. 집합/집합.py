import sys

s = set([])
all = range(1, 21)

m = int(input())
for _ in range(m):
    tmp = sys.stdin.readline().split()
    
    if len(tmp) == 1:
        instruction = tmp[0]
    else:
        instruction, num = tmp[0], int(tmp[1])
    
    if instruction == 'add':
        s.add(num)
    elif instruction == 'remove':
        s.discard(num)
    elif instruction == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif instruction == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif instruction == 'all':
        s.update(all)
    elif instruction == 'empty':
        s.clear()
        

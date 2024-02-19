import collections

n = int(input())
lis1 = list(map(int,input().split()))
m = int(input())
lis2 = list(map(int,input().split()))

clis1 = collections.Counter(lis1)

for num in lis2:
    print(f'{clis1[num]}',end=' ')
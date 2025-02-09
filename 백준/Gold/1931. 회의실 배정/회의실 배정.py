import sys 

input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    n, k = map(int, input().split())
    arr.append([n,k])
arr.sort(key = lambda x: (x[1], x[0]))

now_time = 0
res = 0

for start, end in arr:
    if now_time <= start:
        now_time = end
        res +=1

print(res)
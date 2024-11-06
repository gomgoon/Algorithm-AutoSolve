n = int(input())
time = list(map(int, input().split()))
time.sort()

now_time = 0
res = 0

for t in time:
    res += now_time + t
    now_time += t

print(res)
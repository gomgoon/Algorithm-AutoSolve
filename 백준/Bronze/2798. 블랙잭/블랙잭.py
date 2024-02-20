n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = []
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            res.append(arr[i]+arr[j]+arr[k])
res.append(m)
res.sort()
idx = res.index(m)
if idx != len(res)-1:
    if res[idx + 1] == m:
        answer = m
    else:
        answer = res[idx - 1]
else:
    answer = res[idx - 1]
print(answer)
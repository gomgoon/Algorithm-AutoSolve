n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
m = int(input())
crr = list(map(int, input().split()))
res = []

for i in range(n - 1, -1, -1):
    if arr[i] == 0:
        res.append(brr[i])

res += crr
for i in range(m):
    print(res[i], end = ' ')
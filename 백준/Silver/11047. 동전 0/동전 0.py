n, k = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

res = 0
idx = 0

while k > 0:
    if arr[idx] <= k:
        k -= arr[idx]
        res += 1
    else:
        idx += 1

print(res)
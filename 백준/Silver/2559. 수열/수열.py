n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [-float('inf')] * (n + 1)
prefix_sum[k-1] = sum(arr[:k])
for i in range(k, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i] - arr[i-k]

print(max(prefix_sum))
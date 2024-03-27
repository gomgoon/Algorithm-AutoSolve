n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[n-k])
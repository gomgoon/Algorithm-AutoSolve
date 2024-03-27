n = 5
arr = []
res = 0
for i in range(n):
    num = int(input())
    arr.append(num)
    res += num

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(int(res/5))
print(arr[2])
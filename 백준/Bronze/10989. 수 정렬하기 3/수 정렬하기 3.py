n = int(input())
arr = [0 for _ in range(10001)]
for i in range(n):
    num = int(input())
    arr[num] += 1

for i in range(1,10001):
    for _ in range(arr[i]):
        print(i)
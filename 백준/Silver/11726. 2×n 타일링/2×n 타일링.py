res = 0

n = int(input())

# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
# 5 = 8

arr = [0] * 1001
arr[1] = 1
arr[2] = 2
for i in range(3, n + 1):
    arr[i] = (arr[i-1] + arr[i-2]) % 10007

print(arr[n])
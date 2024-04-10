# BOJ 14425번 문자열 집합
n,m = map(int, input().split())
arr = []
arr2 = []
res = 0

for i in range(n):
    arr.append(input())

for i in range(m):
    arr2.append(input())

arr = set(arr)
for i in arr2:
    if i in arr:
        res += 1
print(res)
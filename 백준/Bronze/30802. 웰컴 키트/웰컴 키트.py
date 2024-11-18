t = 0
p, np = 0, 0

n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in arr:
    t += (i-1) // arr2[0] + 1
p = n // arr2[1]
np = n % arr2[1]

print(t)
print(p, np)
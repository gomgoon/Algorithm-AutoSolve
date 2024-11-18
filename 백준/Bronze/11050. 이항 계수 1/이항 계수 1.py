n,k = map(int, input().split())
f = 1
for i in range(1, n+1):
    f *= i
for i in range(1, k+1):
    f //= i
for i in range(1, (n-k)+1):
    f //= i
print(f)
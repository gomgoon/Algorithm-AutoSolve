def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    res = (n*m) // gcd(n,m)
    print(res)
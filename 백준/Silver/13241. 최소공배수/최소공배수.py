def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

n, m = map(int, input().split())
res = (n*m) // gcd(n,m)
print(res)
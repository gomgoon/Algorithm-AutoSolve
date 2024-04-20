def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
n, m = map(int, input().split())
lcm = (b*m) // gcd(b,m)
a = (lcm // b) * a
a += (lcm // m) * n

while gcd(a, lcm) != 1:
    num = gcd(a, lcm)
    a = a // num
    lcm = lcm // num

print(a, lcm)
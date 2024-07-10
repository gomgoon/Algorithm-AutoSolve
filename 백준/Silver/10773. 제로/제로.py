res = 0
k = int(input())
stack = []

for _ in range(k):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

for i in stack:
    res += i
print(res)
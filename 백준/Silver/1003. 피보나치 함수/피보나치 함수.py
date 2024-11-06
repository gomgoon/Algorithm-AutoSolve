t = int(input())
fibonacci = []

for i in range(0, 41):
    if i == 0:
        fibonacci.append([1, 0])
    elif i == 1:
        fibonacci.append([0, 1])
    else:
        a = fibonacci[i-1][0] + fibonacci[i-2][0]
        b = fibonacci[i-1][1] + fibonacci[i-2][1]
        fibonacci.append([a,b])

for _ in range(t):
    n = int(input())
    print(fibonacci[n][0], fibonacci[n][1])
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    if i == 0:
        x_min = x_max = a
        y_min = y_max = b
    else:
        if a < x_min:
            x_min = a
        if a > x_max:
            x_max = a
        if b < y_min:
            y_min = b
        if b > y_max:
            y_max = b
print((y_max - y_min) * (x_max - x_min))
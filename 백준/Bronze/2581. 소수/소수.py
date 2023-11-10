m = int(input())
n = int(input())
mat = [i for i in range(m,n+1)]
for num in range(m,n+1):
    for i in range(2, num // 2+1):
        if num % i == 0:
            mat.pop(mat.index(num))
            break
if m == 1:
    mat.pop(0)
if len(mat) == 0:
    print('-1')
else:
    print(sum(mat))
    print(min(mat))
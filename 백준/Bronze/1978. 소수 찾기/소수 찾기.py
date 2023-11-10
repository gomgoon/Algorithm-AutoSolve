n = int(input())
intArray = list(map(int,input().strip().split()))
result=0
for num in intArray:
    for i in range(2, num):
        if num % i == 0:
            n -= 1
            break
    if num == 1:
        n -= 1
print(n)
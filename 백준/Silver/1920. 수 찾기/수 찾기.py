n = int(input())
lis1 = list(map(int, input().split()))
m = int(input())
lis2 = list(map(int, input().split()))

lis1.sort()

for num in lis2:
    if num in lis1:
        print(1)
    else:
        print(0)
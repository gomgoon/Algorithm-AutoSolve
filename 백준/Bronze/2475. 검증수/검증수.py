res = 0
num = list(map(int,input().split()))
for i in num:
    res += i*i
print(res%10)

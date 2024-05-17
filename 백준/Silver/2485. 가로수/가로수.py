import math

n = int(input())

arr = []
k = int(input())
for i in range(n-1):
    temp = int(input())
    num = temp - k
    k = temp
    arr.append(num)

def gcd_of_arr(arr):
    gcd = max(arr)
    for i in arr:
        gcd = math.gcd(gcd,i)
    
    return gcd
gcd = gcd_of_arr(arr)
res=0
for i in arr:
    res += i // gcd - 1

print(res)
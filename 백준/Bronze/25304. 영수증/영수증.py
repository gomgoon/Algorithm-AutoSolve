bill=int(input())
n = int(input())
result=0
for i in range(0,n):
    price,count=map(int,input().split())
    result += price*count
if result == bill:
    print('Yes')
else:
    print('No')
h,m=map(int,input().split())
t=int(input())
m+=t
f=1
while(f):
    f=0
    if m>=60:
        m-=60
        h+=1
        f=1
    if h>=24:
        h-=24
        f=1

print(h,m)
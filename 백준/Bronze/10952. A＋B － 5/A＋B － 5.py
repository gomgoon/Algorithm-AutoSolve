f=1
while(f):
    a,b=map(int,input().split())
    if a==0 and b==0:
        f=0
    else:
        print(a+b)
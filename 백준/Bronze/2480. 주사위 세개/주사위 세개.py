a,b,c=map(int,input().split())
result=0
if a==b and b==c:
    result = 10000 + a*1000
else:
    if a==b:
        result = 1000 + a*100
    elif b==c:
        result = 1000 + b*100
    elif a==c:
        result = 1000 + a*100
    else:
        if a>=b:
            if a>=c:
                result=a*100
            else:
                result=c*100
        else:
            if b>=c:
                result=b*100
            else:
                result=c*100
                
print(result)
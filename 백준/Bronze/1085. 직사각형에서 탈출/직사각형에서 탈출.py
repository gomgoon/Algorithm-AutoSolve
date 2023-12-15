x,y,w,h = map(int,input().split())
result = 0
if w-x >= x:
    result = x
else:
    result = w-x

if h-y >= y:
    if result >= y:
        result = y
else:
    if result >= h-y:
        result = h-y
        
print(result)
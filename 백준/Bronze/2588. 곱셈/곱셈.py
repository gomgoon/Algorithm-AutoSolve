a=int(input())
b=int(input())
b1=a*(b%10)
b2=a*(int((b%100)/10))
b3=a*(int(b/100))
print(b1)
print(b2)
print(b3)
print(b1+b2*10+b3*100)
intArray=[1,1,2,2,2,8]
intInputArray=list(map(int,input().split()))
for i in range(0,6):
    intArray[i] -= intInputArray[i]
    print(intArray[i],end=' ')

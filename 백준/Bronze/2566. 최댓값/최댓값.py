row,col=9,9
matrix=[]
maxVal=0
x,y=1,1
for i in range(0,row):
    rowVal = list(map(int,input().strip().split()))
    matrix.append(rowVal)
    if maxVal < max(rowVal): 
        maxVal = max(rowVal)
        x=i+1
        y=rowVal.index(maxVal)+1
        
print(maxVal)
print(f"{x} {y}")
result=0
matrix = [[0 for _ in range(100)] for _ in range(100)]
n=int(input())

for _ in range(n):
    x,y=map(int,input().split())
    for i in range(x-1,x+9):
        for j in range(y-1,y+9):
            matrix[i][j]=1
            
for i in range(100):
    result += matrix[i].count(1)
print(result)
row, cul = map(int,input().split())
matrix1=[]
matrix2=[]
for _ in range(row):
    lis = list(map(int, input().strip().split()))
    matrix1.append(lis)
for _ in range(row):
    lis = list(map(int, input().strip().split()))
    matrix2.append(lis)
for i in range(0,row):
    for j in range(0,cul):
        matrix1[i][j] += matrix2[i][j]
        print(matrix1[i][j],end=' ')
    print()
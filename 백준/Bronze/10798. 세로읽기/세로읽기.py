matrix=[]
for _ in range(5):
    strArray=input()
    matrix.append(strArray)
for i in range(0,15):
    for j in range(0,5):
        if len(matrix[j])-1 >= i:
            print(f"{matrix[j][i]}",end='')
        else:
            continue
while True:
    n = int(input())
    mat = []
    
    if n == -1: break
    
    for i in range(1,n):
        if n % i == 0:
            mat.append(i)
    
    if sum(mat) == n:
        print(f"{n} = {' + '.join(str(i) for i in mat)}")
    else:
        print(f"{n} is NOT perfect.")
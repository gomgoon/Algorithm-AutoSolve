def square(x, y, nx, ny, arr):
    global blue, white
    if square_check(x, y, nx, ny, arr) == 1:
        if arr[y][x] == 1:
            blue +=1 
        else:
            white += 1
    else:
        if nx - x == 1:
            for a,b in ((x,y), (x,ny), (nx, y), (nx,ny)):
                if arr[b][a] == 1:
                    blue +=1 
                else:
                    white += 1
        else:    
            square_divide(x, y, nx, ny, arr)

def square_divide(x, y, nx, ny, arr):
    mx, my = x + (nx - x) // 2, y + (ny - y) // 2
    square(x, y, mx, my, arr)
    square(mx, y, nx, my, arr)
    square(x, my, mx, ny, arr)
    square(mx, my, nx, ny, arr)

def square_check(x, y, nx, ny, arr):
    start_num = arr[y][x]
    for i in range(y, ny):
        for j in range(x, nx):
            if arr[i][j] != start_num:
                return 0
    return 1

n = int(input())
arr = []
blue = 0
white = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

square(0, 0, n, n, arr)

print(white)
print(blue)
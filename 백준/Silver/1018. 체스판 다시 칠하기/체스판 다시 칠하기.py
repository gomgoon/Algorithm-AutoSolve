m,n = map(int, input().split())
board = []
for i in range(m):
    row = list(input())
    board.append(row)
res = 64

def board_check(board,m,n):
    wnum=0
    bnum=0
    for i in range(m, m+8):
        for j in range(n, n+8):
            if (i + j) % 2 == 0:
                if board[i][j] == 'W':
                    wnum += 1
                else:
                    bnum += 1
            else:
                if board[i][j] == 'B':
                    wnum += 1
                else:
                    bnum += 1
    return min(wnum, bnum)

for i in range(m-7):
    for j in range(n-7):
        res = min(board_check(board, i, j), res)

print(res)
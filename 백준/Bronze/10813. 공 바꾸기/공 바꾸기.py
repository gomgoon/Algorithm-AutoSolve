n,m = map(int,input().split())
numberList = list(range(1,n+1))
for _ in range(m):
    s_idx,d_idx=map(int,input().split())
    s_idx -= 1
    d_idx -= 1
    numberList[s_idx], numberList[d_idx] = numberList[d_idx], numberList[s_idx]
for i in range(0,n):
    print(f"{numberList[i]}",end=' ')
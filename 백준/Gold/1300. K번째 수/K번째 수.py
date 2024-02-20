n = int(input())
k = int(input())

def binary_search_k(k, start, end):
    while start <= end:
        mid = (start+end) // 2
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)
        
        if k <= cnt:
            end = mid - 1
        else:
            start = mid + 1
    return start
            
print(binary_search_k(k,1,n*n))
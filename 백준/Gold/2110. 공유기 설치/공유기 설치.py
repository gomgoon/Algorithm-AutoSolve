arr = []
n,c = map(int, input().split())
res = 0

for i in range(n):
    arr.append(int(input()))
arr.sort()
start = 1
end = arr[-1] - arr[0]

while start <= end:
    mid = (start + end) // 2
    router = arr[0] # 라우터를 첫 위치에 설치
    cnt = 1 # 현재 설치한 라우터는 1개
    
    for i in arr: # 모든 라우터에 대해
        if i >= router + mid: # 최소 설치 조건 + 이 전 공유기 위치 값
            cnt +=1 # 공유기 설치
            router = i # 가장 가까운 공유기를 갱신
    
    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
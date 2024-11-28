def nround(num):
    if num - float(int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    total = 0
    arr = []

    for _ in range(n):
        num = int(input())
        arr.append(num)
    arr.sort()

    # 절사 범위 계산
    jp = nround(n * 0.15)
    trimmed_arr = arr[jp:n - jp]

    # 절사된 배열의 평균 계산
    if len(trimmed_arr) == 0:  # 모든 값이 절사된 경우 예외 처리
        print(0)
    else:
        total = sum(trimmed_arr)
        print(nround(total / len(trimmed_arr)))

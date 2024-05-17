import math

n = int(input())
arr = []

def is_prime_number(x):
    if x == 0:
        return False

    if x == 1:
        return False

    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

for i in range(n):
    arr.append(int(input()))

for i in arr:
    num = i
    while True:
        if is_prime_number(num):
            print(num)
            break
        else:
            num+=1

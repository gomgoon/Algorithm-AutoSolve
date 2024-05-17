import math

def is_prime_number(x):
    if x <= 1:
        return False

    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, max_num + 1):
        if is_prime[i]:
            for j in range(2*i, max_num+1, i):
                is_prime[j] = False

    return is_prime


n = int(input())
arr = []
for i in range(n): arr.append(int(input()))

eratos = sieve_of_eratosthenes(1000001)

for i in arr:
    cnt = 0
    for j in range(0, i//2 + 1):
        if eratos[j] and eratos[i-j]:
            cnt += 1
    print(cnt)
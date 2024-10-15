import math
import itertools

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    unique_numbers = set()
    
    for i in range(1, len(num_list) + 1):
        permutations = itertools.permutations(num_list, i)
        for perm in permutations:
            num_str = ''.join(perm)
            num_int = int(num_str)
            unique_numbers.add(num_int)

    for num in unique_numbers:
        if is_prime(num):
            answer += 1

    return answer

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
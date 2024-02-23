n = int(input())
answer = 0

if n == 3 or n == 5:
    print(1)
elif n == 4 or n == 7:
    print(-1)
else:
    answer += n // 5
    n = n % 5
    
    if n == 0:
        print(answer)
    elif n == 1:
        print(answer + 1)
    elif n == 2:
        print(answer + 2)
    elif n == 3:
        print(answer + 1)
    else:
        print(answer + 2)
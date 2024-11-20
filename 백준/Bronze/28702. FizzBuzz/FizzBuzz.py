st = 1
num = 0

for i in range(3):
    n = input()
    if n != 'Fizz' and n != 'Buzz' and n != 'FizzBuzz':
        num = int(n)
        st = 1

    if num != 0 and (n == 'Fizz' or n == 'Buzz' or n == 'FizzBuzz'):
        st +=1

result = num + st
if result % 3 == 0 and result % 5 == 0:
    print('FizzBuzz')
elif result % 3 == 0 and result % 5 != 0:
    print('Fizz')
elif result % 5 == 0 and result % 3 != 0:
    print('Buzz')
else:
    print(result)
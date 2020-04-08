first = float(input())
second = float(input())
operation = input()

if operation == '+':
    print(float(first + second))
elif operation == '-':
    print(float(first - second))
elif operation == '*':
    print(float(first * second))
elif operation == 'pow':
    print(float(first ** second))
elif operation == '/':
    if second == 0:
        print('Деление на 0!')
    else:
        print(float(first / second))
elif operation == 'div':
    if second == 0:
        print('Деление на 0!')
    else:
        print(float(first // second))
elif operation == 'mod':
    if second == 0:
        print('Деление на 0!')
    else:
        print(float(first % second))
num = int(input())
if ((num % 10) + ((num % 100) // 10) + ((num % 1000) // 100)) == (((num % 10000) // 1000) + ((num % 100000) // 10000) + ((num % 1000000) // 100000)):
    print('Счастливый')
else:
    print('Обычный')
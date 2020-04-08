a = [int(i) for i in input().split()]
b = int(input())
i = 0
res = ''
while i < len(a):
    if a[i] == b:
        res = res + str(i) + ' '
    i += 1
if res == '':
    print('Отсутствует')
else:
    print(res)

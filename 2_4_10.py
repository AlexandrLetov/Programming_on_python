a = [int(i) for i in input().split()]
b = ''
i = 0
if len(a) == 1:
    b = str(a[0])
    print(b)
else:
    while i < len(a):
        if i == len(a) - 1:
            b = b + str((a[i - 1] + a[0])) + ' '
        else:
            b = b + str((a[i - 1] + a[i + 1])) + ' '
        i += 1
    print(b)

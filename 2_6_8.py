a = int(input())
i = 1
temp_res = ''
res = ''
while i <= a:
    temp_res = temp_res + ((str(i) + ' ') * i)
    i += 1
temp_res = temp_res.strip()
b = [int(i) for i in temp_res.split()]
i = 0
while i < a:
    res = res + str(b[i]) + ' '
    i += 1
print(res)

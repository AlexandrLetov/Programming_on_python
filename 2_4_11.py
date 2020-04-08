# a = [int(i) for i in input().split()]
# i = 0
# sm = len(a)
# temp = ''
# res = ''
# while i < sm:
#    temp = str(a[0])
#    a.remove(a[0])
#    if int(temp) in a and temp not in res:
#        res = res + temp + ' '
#    i += 1
# print(res)

a = [int(i) for i in input().split()]
b = []
res = ''
for i in a:
    if a.count(i) > 1 and i not in b:
        b.append(i)
for i in b:
    res = res + str(i) + ' '
print(res)

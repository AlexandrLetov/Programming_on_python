a = int(input())
b = int(input())
count = 0
srar = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        srar = srar + i
        count += 1
srar = srar / count
print(srar)

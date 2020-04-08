flag = 1
s = 0
kv = 0
while flag != 0:
    a = int(input())
    s = s + a
    kv = kv + a ** 2
    if s == 0:
        flag = 0
print(kv)

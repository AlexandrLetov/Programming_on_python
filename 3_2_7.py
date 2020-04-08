dic = {}
for i in range(0, int(input())):
    x = int(input())
    if x not in dic.keys():
        dic[x] = f(x)
    print(dic[x])

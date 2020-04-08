file = open('./test.txt', 'r', encoding="utf-8")
res = ''
count = 0
for line in file:
    text = line.lower().split(' ')
    while len(text) > 0:
        temp = text[0]
        if text.count(temp) > count:
            count = text.count(temp)
            res = temp
        while temp in text:
            text.remove(temp)
res = res + ' ' + str(count)
print(res)
file.close()

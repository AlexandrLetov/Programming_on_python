text = input().lower().split(' ')
while len(text) > 0:
    res = ''
    temp = text[0]
    count = text.count(temp)
    res = temp
    while temp in text:
        text.remove(temp)
    res = res + ' ' + str(count)
    print(res)

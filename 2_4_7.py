s = input()
s = s + ' '
i = 0
count = 0
temp = ''
result = ''
while i < len(s):
    if i == 0:
        temp = s[i]
        count = 1
    if i != 0:
        if temp[0] == s[i]:
            count += 1
        elif temp[0] != s[i]:
            result = result + temp[0] + str(count)
            count = 1
            temp = s[i]
    i += 1
print(result)

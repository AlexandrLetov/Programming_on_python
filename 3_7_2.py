code = {}
code2 = {}
keys = input()
values = input()
for i in range(0, len(keys)):
    code[keys[i]] = values[i]
for i in range(0, len(keys)):
    code2[values[i]] = keys[i]
text = input()
for i in text:
    print(code[i], end='')
print()
text = input()
for i in text:
    print(code2[i], end='')

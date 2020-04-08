import re

out = {}
out_count = {}
for i in range(1, 12):
    out[int(i)] = '0'
    out_count[int(i)] = 0
file = open('./test.txt', 'r', encoding='UTF-8')
for line in file:
    temp = line.rstrip().split('\t')
    out[int(temp[0])] = int(out[int(temp[0])]) + int(temp[2])
    out_count[int(temp[0])] = int(out_count[int(temp[0])]) + 1
file.close()
for i in range(1, 12):
    if out[i] != 0:
        out[i] = out[i] / out_count[i]
for i in range(1, 12):
    if out[i] == 0:
        out[i] = '-'
for i in range(1,12):
    print(str(i) + ' ' + str(out[i]))
print(out)
print(out_count)
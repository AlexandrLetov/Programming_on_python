import re

file = open('./test.txt', 'r', encoding='UTF-8')
sr1 = 0
sr2 = 0
sr3 = 0
count = 0
for line in file:
    arr = (re.sub("\n", '', line).split(';'))
    print((int(arr[1])+int(arr[2])+int(arr[3]))/3)
    sr1 = sr1 + int(arr[1])
    sr2 = sr2 + int(arr[2])
    sr3 = sr3 + int(arr[3])
    count += 1
sr1 = sr1/count
sr2 = sr2/count
sr3 = sr3/count
print(str(sr1) + ' ' + str(sr2) + ' ' + str(sr3))
file.close()

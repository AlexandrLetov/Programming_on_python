d = {}
arr2 = []
for i in range(0, int(input())):
    arr = input().split(';')
    if arr[0] not in d:
        d[arr[0]] = [1, 0, 0, 0, 0]
        arr2.append(arr[0])
    else:
        value = d.get(arr[0])
        value[0] += 1
        d[arr[0]] = value
    if arr[2] not in d:
        d[arr[2]] = [1, 0, 0, 0, 0]
        arr2.append(arr[2])
    else:
        value2 = d.get(arr[2])
        value2[0] += 1
        d[arr[2]] = value2
    if arr[1] > arr[3]:
        value = d.get(arr[0])
        value[1] += 1
        value[4] += 3
        d[arr[0]] = value
        value2 = d.get(arr[2])
        value2[3] += 1
        d[arr[2]] = value2
    if arr[1] < arr[3]:
        value = d.get(arr[0])
        value[3] += 1
        d[arr[0]] = value
        value2 = d.get(arr[2])
        value2[1] += 1
        value2[4] += 3
        d[arr[2]] = value2
    if arr[1] == arr[3]:
        value = d.get(arr[0])
        value[2] += 1
        value[4] += 1
        d[arr[0]] = value
        value2 = d.get(arr[2])
        value2[2] += 1
        value2[4] += 1
        d[arr[2]] = value2

for name in arr2:
    value = d.get(name)
    print(name + ':' + str(value[0]) + ' ' + str(value[1]) + ' ' + str(value[2]) + ' ' + str(value[3]) + ' ' + str(value[4]))
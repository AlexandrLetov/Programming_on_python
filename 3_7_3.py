arr = []
arr2 = set()
temp = []
for i in range(0, int(input())):
    arr.append(input().lower())
for i in range(0, int(input())):
    temp = input().split(' ')
    for j in range(0, len(temp)):
        arr2.add(temp[j])
for word in arr2:
    if word.lower() not in arr:
        print(word)

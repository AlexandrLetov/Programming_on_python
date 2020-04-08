file = open('./test.txt', 'r', encoding="utf-8")
for line in file:
    letters = []
    text = str(line)
    for letter in text:
        temp = str(letter)
        letters.append(temp)
    arr = []
    arr2 = []
    while len(letters) != 0:
        if str(letters[0]).isalpha():
            arr.append(letters[0])
            letters.pop(0)
        if len(letters) > 1 and str(letters[0]).isnumeric() and str(letters[1]).isnumeric():
            test = str(letters[0]) + str(letters[1])
            arr2.append(test)
            letters.pop(0)
            letters.pop(0)
        elif len(letters) > 1 and str(letters[0]).isnumeric():
            arr2.append(letters[0])
            letters.pop(0)
        elif len(letters) == 1 and str(letters[0]).isnumeric():
            arr2.append(letters[0])
            letters.pop(0)
    res = ''
    for i in range(0, len(arr)):
        res = res + str(arr[i]) * int(arr2[i])
    print(res)

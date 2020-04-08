def modify_list(l):
    temp = []
    for i in l:
        temp.append(i)
    l.clear()
    for i in temp:
        if i % 2 == 0:
            l.append(i // 2)
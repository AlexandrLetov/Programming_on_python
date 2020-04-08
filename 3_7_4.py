dot = [0, 0]
for i in range(0, int(input())):
    command = input().split(' ')
    if command[0] == 'север':
        dot[1] += int(command[1])
    if command[0] == 'юг':
        dot[1] -= int(command[1])
    if command[0] == 'восток':
        dot[0] += int(command[1])
    if command[0] == 'запад':
        dot[0] -= int(command[1])
print(str(dot[0]) + ' ' + str(dot[1]))

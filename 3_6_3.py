import requests

part1 = 'https://stepic.org/media/attachments/course67/3.6.3/'
part2 = '699991.txt'
flag = 1
count = 0
while flag == 1:
    send_request = requests.get(part1 + part2)
    text = send_request.text
    if text[0] != 'W' and text[1] != 'e':
        part2 = send_request.text
        print(text)
        count += 1
    else:
        flag = 0
        print(text)
print(count)

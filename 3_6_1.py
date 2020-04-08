import requests

file = open('./test.txt')
for line in file:
    url = line.strip()
file.close()
send_request = requests.get(url)
file = open('./test.txt', 'w')
file.write(send_request.text)
file.close()
count = 0
file = open('./test.txt')
for line in file:
    count += 1
file.close()
print(count)

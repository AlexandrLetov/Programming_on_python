word = input().lower()
print(((word.count('c') + word.count('g')) / len(word)) * 100)
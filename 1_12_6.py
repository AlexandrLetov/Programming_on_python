def end_word(n):
    if (n >= 5) and (n <= 20):
        return 'матов'
    elif (n % 100 >= 11) and (n % 100 <= 14):
        return 'матов'
    elif n % 10 == 1:
        return 'мат'
    elif (n % 10) >= 2 and (n % 10 <= 4):
        return 'мата'
    elif (n % 10 >= 5) and (n % 10 <= 9) or (n % 10 == 0):
        return 'матов'

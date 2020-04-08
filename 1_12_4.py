fig = input()
if fig == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    print(((p * (p - a) * (p - b) * (p - c))) ** 0.5)
if fig == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print(a * b)
if fig == 'круг':
    r = int(input())
    print(3.14 * r ** 2)

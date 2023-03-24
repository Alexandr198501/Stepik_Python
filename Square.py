'''Этот код вычисляет площадь введенной фигуры.'''

figure = str(input())
if figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
elif figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif figure == 'круг':
    r = int(input())
    S = 3.14 * r ** 2
else:
    print("Unknown figure!")
print(S)

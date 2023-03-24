'''Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все
числа отрезка [c;d].'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for s in range(c, d + 1):
    print('\t', '\t', s, end='')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print('\t', i*j, end='\t')
    print()


'''Эта программа принимает три целых числа и выводит их в следующем порядке:
максимальное, минимальное и оставшееся.'''

a, b, c = int(input()), int(input()), int(input())

if a >= b >= c:
    print(a, c, b, sep='\n')
elif a >= c >= b:
    print(a, b, c, sep='\n')
elif b >= a >= c:
    print(b, c, a, sep='\n')
elif b >= c >= a:
    print(b, a, c, sep='\n')
elif c >= a >= b:
    print(c, b, a, sep='\n')
elif c >= b >= a:
    print(c, a, b, sep='\n')

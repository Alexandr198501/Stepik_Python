'''Эта программа принимает 6 цифр и складывая первые 3 и последние 3 вычисляет, счастливй билет или нет.'''

n = int(input())
s1 = n // 100000
s2 = n // 10000 % 10
s3 = n // 1000 % 10
s4 = n // 100 % 10
s5 = n // 10 % 10
s6 = n % 10
if (s1 + s2 + s3) == (s4 + s5 + s6):
    print("Счастливый")
else:
    print("Обычный")






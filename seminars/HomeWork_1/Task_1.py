# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Enter number from 1 to 7: '))
if 5 < day < 8:
    print('Yes')
elif 0 < day < 6:
    print('No')
else:
    print('There is no such day of the week')

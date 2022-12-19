# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = input('Enter number: ')
sum = 0
for n in number:
    if n.isdigit():
        sum += int(n)
print(sum)

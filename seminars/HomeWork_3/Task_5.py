# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Enter number: '))
list_f = [0]
f1 = f2 = 1
if num > 0:
    list_f.insert(0, f1)
    list_f.append(f1)
    for i in range(1, num):
        f1, f2 = f2, f1+f2
        list_f.insert(0, -f1)
        list_f.append(f1)
print(list_f)

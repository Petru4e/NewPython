# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import sample

num_start = int(input('Enter start: '))
num_end = int(input('Enter end: '))

list = sample(range(num_start, num_end+1), num_end-num_start)
print(list)

sum = 0
for i in range(1, len(list), 2):
    sum += list[i]

print(sum)

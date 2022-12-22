# Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list, end=' => ')
maximum=round(list[0] % 1, 3)
minimum=round(list[0] % 1, 3)

for i in list:
    if i%1>0:
        maximum = max(round(i % 1, 3), maximum)
        minimum = min(round(i % 1, 3), minimum)
print(maximum-minimum)
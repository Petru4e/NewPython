# Задана натуральная степень k. Сформировать
# случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import sample

list = sample(range(0, 100), 3)
print(list)


path = 'file_task_4.txt'
file = open(path, 'w')

for i in list:
    file.write(f'k={i} => 2*x^{i}+4*x+5=0 x^{i}+5=0 10*x^{i}=0\n')

file.close()

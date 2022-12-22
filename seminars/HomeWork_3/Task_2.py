# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import sample

num_start = int(input('Enter start: '))
num_end = int(input('Enter end: '))

list = sample(range(num_start, num_end+1),  num_end-num_start)
print(list)

sum_list=[]

i=0
j=len(list)-1
while i<=j:
    sum_list.append(list[i]*list[j])
    i+=1
    j-=1
print(sum_list)

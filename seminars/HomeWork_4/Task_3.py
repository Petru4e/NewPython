# Задайте последовательность чисел. 
# Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


import random
list =[] 
for i in range(10):
    list.append(random.randint(1,10))
print(list)
new_list=[]
for i in list:
    flag=0
    for j in list:
        if i==j:
            flag+=1
    if flag<2:
        new_list.append(i)
print(new_list)
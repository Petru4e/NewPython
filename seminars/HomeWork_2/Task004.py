# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на
#  указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.

num = int(input('Enter number: '))
list=[]
for i in range(-num, num+1):
    list.append(i)
print(list)
pozition1 = input('Enter position1: ')
pozition2 = input('Enter position2: ')
pozition3 = input('Enter position3: ')
with open('file.txt', 'a') as file:
    file.write(f'{pozition1}\n')
    file.write(f'{pozition2}\n')
    file.write(f'{pozition3}\n')

path= 'file.txt'
file=open(path,'r')
pow=1
for position in file:
    int_pos=int(position)
    if int_pos>len(list) or int_pos<0:
        print('Working with exceptions has not been taught yet, so you can skip this number for now and continue working')
    else:
        pow*=list[int_pos]
print(pow)

file.close()


    
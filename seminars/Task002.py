# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

list = []
for i in range(5):
    i = list.append(int(input("Введите число:")))
max = list[0]
for i in list:
    if max < i:
        max = i
print(max)
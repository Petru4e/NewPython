# 11. Напишите программу,
#  которая принимает на вход число N и выдаёт
#   последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81


number = int(input ('Enter number '))
x=1
for i in range(1,number+1):
    print(x)
    x*=-3
  

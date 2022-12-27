# Задайте натуральное число N. 
# Напишите программу,
#  которая составит список простых множителей числа N.

def prime_factors(n):
   i = 2
   list_pf= []
   while i * i <= n:
       while n % i == 0:
           list_pf.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       list_pf.append(int(n))
   return list_pf

num=int(input('Enter number: '))
print(prime_factors(num))
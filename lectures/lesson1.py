# Ввод\вывод данных


# print('Введите а ')
# a = input()
# print('Введите b ')
# b = input()
# print(a, b)
# print('{} -- {} строки5'.format(a, b))
# print(a+b)
# x = int(input('Введите x \nx='))
# y = int(input('Введите y \ny='))
# print(x, '+',  y, '=', x+y)
# print(f'{x} + {y} = {x+y}')


# Типы данных


# i=int(input('i= '))
# f=float(input('f= '))
# s=input('s= ')
# n=None
# print(type(i))
# print(type(f))
# print(type(s))
# print(type(n))


# Арифметические операции


# exp1 = 2**3-10 % 5+2*3
# exp2 = 2**3-10/5+2*3
# exp3 = 2**3-10//5+2*3
# exp4 = (2**3)-(10/5)+(2*3)
# print(f'{exp1} {type(exp1)}')
# print(f'{exp2} {type(exp2)}')
# print(f'{exp3} {type(exp3)}')
# print(f'{exp4} {type(exp4)}')


# Логические операции


# f=[1,2,3,4]
# print(f)
# print(not 2 in f)

# # is_odd=f[0]%2==0
# is_odd= not f[0]%2
# print(is_odd)


# Управляющие конструкции


# a=int(input('a='))
# b=int(input('b='))
# if a>b:
#     print(a)
# else:
#     print(b)

# user_name=input('Введите имя: ')
# if user_name=='Маша':
#     print('Маша')
# elif user_name=='Марина':
#     print('Марина')
# else:
#     print(user_name)

# original = 235
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 235456
# inverted = 0
# print(original)
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('End')
# print(inverted)

# for i in 1,2,3,4:
#     print(i)

# r=range(5)
# for i in r:
#     print(i)

# for i in range(5,7):
#     print(i)

# for i in range(-8,3):
#     print(i)

# for i in range(-8,8,3):
#     print(i)

# for i in range(8,-8,-1):
#     print(i)

# #line=""
# for i in range(5):
#     line=""
#     for j in range(5):
#         line+="*"
#     print(line)


# Строки

# text='съешь ещё этих мягких французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.split())
# text=text.replace('ещё', 'уже').upper()
# print(text)
# for char in text[:5]:
#     print(char)
# print(text.title())

# text='съешь ещё этих мягких французских булок'
# print(text[0])
# print(text[len(text)-1])
# print(text[-8])
# print(text[:2])
# print(text[6:-10])
# print(text[::6])
# print(text[0:len(text):6])
# print(text[2:9]+text[-5]+text[:2])
# print(text[:6]+text[10:15]+text[-17:-10]+text[-2:len(text)])

# Списки

# num=[1,2,3]
# print(num)

# num=list(range(9,-1,-1))
# print(num)

# num[len(num)-1]='пуск' #так делать не хорошо
# print(num)

# num=list(range(10))
# for i in num:
#     i=i**2
#     print(i)
# print(num)

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e,end=' ')
# print()
# for e in colors:
#     print(e*2,end=' ')
# print()
# colors.append('gray')
# print(colors==['red', 'green', 'blue','gray'])
# colors.remove('red')
# for e in colors:
#     print(e,end=' ')

#Функции

def function(x):
    return x**2
print(function(8))


def f(x):
    if x==1:
        return 'int'
    elif x==2.3:
        return 23
    else:
        return
print(f(1))
print(f(2.3))
print(f(28))
print(type(f(1)))
print(type(f(2.3)))
print(type(f(28)))

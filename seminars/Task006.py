#  Напишите программу, в которой пользователь будет
#  задавать две строки, а программа -
#   определять количество вхождений одной строки в другой.

tex1 = input('Enter text1 ')
tex2 = input('Enter text2 ')

print(tex1.count(tex2))

count=0
for i in range(len(tex1)-len(tex2)-1):
    if tex1[i:i+len(tex2)]==tex2:
        count+=1
print(count)

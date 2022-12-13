# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
flag = True
result=True
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ~(x & y & z) == (~ x) | (~ y) | (~ z):
                flag=True
            else:
                flag= False
            print(f'x = {x}, y = {y}, z = {z}, FLAG = {flag}')
    result = result&flag        
print()
print(f'The result for all values is predicate = {flag}')
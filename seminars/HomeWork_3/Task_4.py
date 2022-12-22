# ; Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# ; Пример:

# ; - 45 -> 101101
# ; - 3 -> 11
# ; - 2 -> 10
num = int(input('Enter number: '))

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

print(convert_to(num, 2))
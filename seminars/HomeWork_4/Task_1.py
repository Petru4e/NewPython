# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

num = (input("Enter number: ").split('.'))
accuracy=len(num[1])
print(round((math.pi),accuracy))

# e = 1/0! + 1/1! + 1/2! + ...
import math
precision = float(input("Введите точность: "))

result = 0
i = 0
addMember = 1
while addMember > precision:
    addMember = 1 / math.factorial(i)
    result += addMember
    i += 1

print(f"Результат: {result}")
print(f"Константа: {math.e}")

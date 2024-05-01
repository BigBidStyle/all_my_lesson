a = 14
b = 7

# if a > b:
#     res = a
# else:
#     res = b

res = a if a > b else b # <-- Тернарный оператор.
print(res)
print("-------------")
# ------------------------------------ #
# Пример # 2
p = "python"
t = 'upper'

res = p.upper() if t == 'upper' else p
print(res)
print("-------------")
# ------------------------------------ #
a = 14
b = 17

res = [1, 2, a if a < b else b , 45, 55]
print(res)
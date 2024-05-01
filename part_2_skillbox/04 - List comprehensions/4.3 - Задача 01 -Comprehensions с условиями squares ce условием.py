# Простой пример.... (Квадрат нечетный числе)
squares = []
for x in range(10):
    if x % 2 != 0:
        squares.append(x ** 2)

print(squares)
# -------------------
# Можем упростить и ускорить этот код.
squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]
print(squares_odds)

# Добавляем значение else

squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]
squares_cubes = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10)]
print(squares_odds)
print(squares_cubes)

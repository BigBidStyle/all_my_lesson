# Простой пример....
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)
# -------------------
# Можем упростить и ускорить этот код.
squares = [x ** 2 for x in range(10)]
print(squares)
# ------------------
def get_higher_price(procent, price):
    return round(price * (1 + procent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_persent = int(input("Повышение на первый год: "))
second_persent = int(input("Повышение на второй год: "))

prices_first = [get_higher_price(first_persent, i_price) for i_price in prices_now]
prices_second = [get_higher_price(second_persent, i_price) for i_price in prices_first]

print(f"Сумма цен за каждый год: {round(sum(prices_now), 2)}, "
      f"{round(sum(prices_first), 2)}, {round(sum(prices_second), 2)}")
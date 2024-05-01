# Команде программистов отдали на тестирование новую модель суперкомпьютера.
# Для начала программисты решили проверить, как у компьютера обстоят дела с вычислениями
# вещественных чисел. Разработчики компьютера предупредили, что на входе он работает только
# с экспоненциальной формой числа.

# Пользователь вводит число N в экспоненциальной форме, где мантисса всегда равна числу от 1 до 9,
# а порядок меньше нуля. Также есть переменная Х, которая изначально равна единице. Посчитайте,
# сколько раз нужно прибавить N к Х, чтобы оно перевалило за двойку.

# Дополнительно: обеспечьте контроль ввода.

# Пример 1:
# Введите число в эксп. форме: 1e-3
# Кол-во прибавлений: 1001

# Пример 2:
# Введите число в эксп. форме: 5.02e-1
# Кол-во прибавлений: 2

x = 1
count = 0
n = float(input("Введите число в эксп. форме: "))
while (x + n) <= 2:
    x += n
    print(x)
    count += 1
print(f"Кол-во интераций: {count}")

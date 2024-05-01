print("Урок 10.1 Работа со вложенными циклами.")
print("Задача № 1 - Таблица умножения.")
for a in range(1,11):
    for b in range(1,11):
        print(a, "*", b, "=", a * b)
    print()

print("Задача № 2 - Таблица умножения- переделанная.")
for row in range(1,11):
    for col in range(1,11):
        print(row *  col, end = " \t ")
    print()
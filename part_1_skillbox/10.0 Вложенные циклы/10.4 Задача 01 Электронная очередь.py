print("Урок 10.4 Решение задач с помощью вложенных циклов.")
print("Задача № 1. - очередь  ")
people = int(input("Введите кол-во людей: "))
for hour in range(people +1):
    print("Идет час: ", hour)
    for num in range(hour, people):
        print("Номер в очереди: ", num)
    print()
print("Очередь обслужена!!")
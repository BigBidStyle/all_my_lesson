number_list = [1, 5, 2, -7, 6]                                                                 # Список.

for _ in range(5):
    new_num = int(input("Введите значение переменной: "))
    number_list.append(new_num)                                                           # Добавление в конец списка дополнительного значения.

for number in number_list:
    print(f"{number} ** 2 = {number ** 2}")

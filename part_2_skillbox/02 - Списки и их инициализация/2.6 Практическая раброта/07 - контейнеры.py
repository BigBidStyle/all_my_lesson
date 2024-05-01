# Контейнеры на складе лежат в ряд в порядке убывания или равно.
# массы в килограммах. На склад привезли ещё один контейнер, который тоже нужно
# положить на определённое место.

# Напишите программу, которая получает на вход невозрастающую последовательность
# натуральных чисел. Они означают массу каждого контейнера в ряду. После этого
# вводится число X — масса нового контейнера. Программа выводит номер, под которым
# будет лежать новый контейнер. Если в ряде есть контейнеры с массой, как у нового,
# то его нужно положить после них.

# Обеспечьте контроль ввода: все числа не превышают 200.

# Пример:
# Количество контейнеров: 8
# Введите вес контейнера: 165
# Введите вес контейнера: 163
# Введите вес контейнера: 160
# Введите вес контейнера: 160
# Введите вес контейнера: 157
# Введите вес контейнера: 157
# Введите вес контейнера: 155
# Введите вес контейнера: 154

# Введите вес нового контейнера: 162

# Номер, который получит новый контейнер: 3

max_weight = 200
list_container = []

def input_container(i, n):
    while i != n:
        print(f"Введите вес контейнера: ", end="")
        weight_container = int(input())
        if weight_container > max_weight:
            print("Вес контейнера должен быть меньше 200 кг.")
            input_container(i, n)
            break
        elif weight_container < max_weight and len(list_container) == 0:
            list_container.append(weight_container)
            i += 1
        elif weight_container < max_weight and list_container[-1] >= weight_container:
             list_container.append(weight_container)
             i += 1
        else:
            print("Вес контейнера должен быть меньше либо равно предыдущему контейнеру.")
    return

index_number = 0
number_container = int(input("Количество контейнеров: "))
input_container(index_number,number_container)

weight_new_container = int(input("\nВведите вес нового контейнера: "))
for i in range(number_container):
    if weight_new_container >= list_container[i]:
        list_container.insert(i, weight_new_container)
        print(list_container)
        print(f"Номер, который получит новый контейнер: {i + 1}")
        break
    elif weight_new_container <= list_container[number_container-1]:
        list_container.insert(number_container + 1, weight_new_container)
        print((list_container))
        print(f"Номер, который получит новый контейнер: {number_container + 1}")
        break



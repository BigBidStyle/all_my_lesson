# IP-адрес компьютера состоит из 4 чисел, разделённых точкой.
# Каждое число находится в диапазоне от 0 до 255 (включительно).

# Пример правильного адреса: 192.168.1.0
# Пример неправильного адреса: 192.168.300.0
# Напишите программу, которая получает на вход 4 числа и выводит
# на экран IP-адрес. Используйте переменную ip_address в качестве шаблона.
# Обеспечьте контроль ввода.

ip_address = "{0}.{1}.{2}.{3}"
count = 0
numbers = []
while count < 4:
    new_number = int(input("Введите число от 0 до 255: "))
    if 0 <= new_number <= 255:
        count += 1
        numbers.append(new_number)
    else:
        print("Не верное число!!!")

print(ip_address.format(*numbers))
# * полезный инструмент, но и без него можно справиться,
# вручную прописав элементы по индексам

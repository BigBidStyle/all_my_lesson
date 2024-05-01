print("Урок 7.4 Функция range с началом отсчета.")
print("Теория - Задача № 1 - От и до")
start_number = int(input("Нипишите число начала: "))
stop_number = int(input("Напишите число конца: "))
for number in range(start_number, stop_number + 1):
    print(number ** 2)
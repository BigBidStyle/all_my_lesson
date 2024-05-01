print("Задание № 2 - Сумма чисел.")
start_number = int(input("Нипишите первое число: "))
stop_number = int(input("Напишите второе число: "))
summ = 0
for number in range(start_number, stop_number+1):
    summ += number
print("Сумма чисел от ", start_number, "до", stop_number, "равна", summ)

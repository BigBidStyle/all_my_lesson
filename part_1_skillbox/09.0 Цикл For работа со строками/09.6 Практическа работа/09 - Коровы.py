# Задача 9. Коровы
# Что нужно сделать
# Для коров есть 10 стойл. В каждом стойле разные условия для животных, поэтому и молока они
# дают по-разному. В первом стойле производят 2 литра в день, во втором 4,
# в третьем - 6, потом 8, 10, 12, 14, 16, 18, 20. Но коровы стоят не во всех стойлах.
# Свободные и занятые обозначаются строкой из букв a и b, где a - свободное стойло, b - занятое.

# Напишите программу для подсчета получаемого молока в коровнике, с учетом следующего
# взаимодействия пользователя с программой: пользователь вводит строку из 10 символов a и b.
# Необходимо определить, сколько в итоге будет произведено молока за день.

# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием);
# Переменные имеют значащие имена, не только a, b, c, d (видео 2.3)

count_milk = 0
total_milk = 0
for i in range(1,10+1):
    milk = input(f"Стойло {i} свободно? a-свободно, b-занято: ")
    count_milk += 2
    if milk == "a":
        total_milk += count_milk
print(f"В итоге будет произведено {total_milk} литров молока.")

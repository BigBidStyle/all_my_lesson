print("Практическая работа. Задача №5. Марсоход 2.")
# print("\n")
# # К роботу Валли отправили ещё одного робота - Билли. Это его первая высадка на Марс,
# # поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров. Марсоход
# # высаживается в центре комнаты (в точке 8, 10), после чего управление им передаётся оператору -
# # пользователю вашей программы. Программа спрашивает, в какую сторону оператор хочет направить
# # робота: север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D). Оператор
# # делает выбор, марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию
# # марсохода. Если марсоход упёрся в стену, то он не должен пытаться перемещаться в сторону стены,
# # в этом случае его позиция не меняется. Создайте программу для управления роботом Билли.
#
# # Пример:
# # [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# # [Оператор]: A
# # [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# # [Оператор]: W
# # [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# # [Оператор]: W
# # [Программа]: Марсоход находится на позиции 5, 20, введите команду:


length = 20                     # Длина комнаты.
width = 15                      # Ширина комнаты.
landing_length = 10          # Координата длины высадки.
length_width = 8             # Координата ширины высадки.
print("[Программа]: Марсоход находиться на координатах ", landing_length, ",", length_width, ". Введите команду:")
operator = input("[Оператор ]: ")
while landing_length < length and landing_length > 0 and length_width < width and length_width > 0:
    if  operator == "w" or operator == "W" or operator == "ц" or operator == "Ц":
        landing_length += 1
        print("[Программа]: Марсоход находиться на координатах: ", landing_length, ",", length_width, ". Введите команду:")
        operator = input("[Оператор ]: ")
    if operator == "s" or operator == "S" or operator == "ы" or operator == "Ы":
        landing_length -= 1
        print("[Программа]: Марсоход находиться на координатах: ", landing_length, ",", length_width, ". Введите команду:")
        operator = input("[Оператор ]: ")
    if operator == "d" or operator == "D" or  operator == "в" or operator == "В":
        length_width += 1
        print("[Программа]: Марсоход находиться на координатах: ", landing_length, ",", length_width, ". Введите команду:")
        operator = input("[Оператор ]: ")
    if operator == "a" or operator == "A" or operator == "ф" or operator == "Ф":
        length_width -= 1
        print("[Программа]: Марсоход находиться на координатах: ", landing_length, ",", length_width, ". Введите команду:")
        operator = input("[Оператор ]: ")
else:
    print("Марсоход достиг границы периметра")

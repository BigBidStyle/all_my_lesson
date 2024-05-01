# Дана строка S и номер позиции символа в строке.
# Напишите программу, которая выводит соседей этого символа
# и сообщение о количестве таких же символов среди этих соседей:
# их нет, есть ровно один или есть два таких же.

# Пример 1:
# Введите строку: abbc
# Номер символа: 3

# Символ слева: b
# Символ справа: c

# Есть ровно один такой же символ.

# Пример 2:
# Введите строку: abсd
# Номер символа: 3

# Символ слева: b
# Символ справа: d

# Таких же символов нет.


# Мой вариант решения.
user_msg = input("Введите строку: ")
message = list(user_msg)
message_n = len(message)

what_replace = int(input("Номер символа: "))
symbol_replace = message[what_replace]
symbol_L = message[what_replace - 1]
symbol_R = message[what_replace + 1]

if what_replace > 0 and what_replace < message_n:
    print(f"\nСимвол слева: {symbol_L}")
    print(f"Символ справа: {symbol_R}")

elif what_replace == 0:
    print(f"Символа слева не существует.")
    print(f"Символ справа: {symbol_R}")
else:
    print(f"\nСимвол слева: {symbol_L}")
    print(f"Символа cправа не существует.")

if symbol_L == symbol_replace and symbol_R == symbol_replace:
    print("\nЕсть два таких же символа.")
elif symbol_R != symbol_replace and symbol_L != symbol_replace :
    print("\nТаких же символов нет.")
else:
    print("Есть ровно один такой же символ.")

# SkillBox решение
msg = input("Введите строку: ")
index_of_letter = int(input("Номер символа: ")) - 1  # сразу отнимаем 1, чтобы превратить номер в индекс
letters = list(msg)
count = 0
if index_of_letter > 0:
    print("Символ слева:", letters[index_of_letter - 1])
    if letters[index_of_letter - 1] == letters[index_of_letter]:
        count += 1
if index_of_letter < len(letters) - 1:
    print("Символ справа:", letters[index_of_letter + 1])
    if letters[index_of_letter + 1] == letters[index_of_letter]:
        count += 1

if count == 0:
    print("Таких же символов нет.")
elif count == 1:
    print("Есть ровно один такой же символ.")
elif count == 2:
    print("Таких символов два.")
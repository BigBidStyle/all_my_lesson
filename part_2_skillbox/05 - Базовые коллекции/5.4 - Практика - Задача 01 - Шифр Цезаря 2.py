# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
# Напомним, что в таком способе шифрования каждая буква
# заменяется на следующую по алфавиту через K позиций по кругу.

# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
# Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.

# def caesar_cipher(string, user_shift):
#     char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != " " else " ") for sym in string]
#     new_str = " "
#     for i_char in char_list:
#         new_str += i_char
#     return new_str
#
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя.".lower()
# input_str =  input("\nВведите сообщение: ").lower()
# shift = int(input("Введите сдвиг: "))
#
# output_str = caesar_cipher(input_str, shift)
#
# print(f"Зашифрованное сообщение: {output_str}")

#  решение SkillBox
text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]  # заполняем список буквами алфавита
# Думаем над структурой алгоритма: [вариант_1 если условие_1 иначе вариант_2 for буква in текст]
new_text = [alphabet[(alphabet.index(letter) + shift) % len(alphabet)] if letter in alphabet else letter for letter in text.lower()]
print(''.join(new_text))
# Юлий Цезарь использовал свой способ шифрования текста.
# Каждая буква заменялась на следующую по алфавиту через
# K позиций по кругу. Если взять русский алфавит и K = 3, то в слове,
# которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.

# Пользователь вводит сообщение, а также значение сдвига.
# Напишите программу, которая зашифрует это сообщение при помощи шифра Цезаря.

# Пример:
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.


# Программные параметры.
a = 1072
b = 1104

# Вводим параметры
entered_text = input("Введите сообщение: ")

shift = int(input("Введите сдвиг: "))

# Меняем буквенное значение в код UTF
number_text = []
text = [number_text.append(ord(word)) for word in entered_text ]
print(number_text, " < --- number_text")

# Проверяем сдвиг.
checking_shift = [i if (i + shift) <= b else a + (i + shift) % a for i in number_text ]
print(checking_shift, " < --- checking shift")

# Меняем цифры на введеный сдвиг.
crypt_number = [digit + shift if a <= digit <= b else digit for digit in checking_shift]
print(crypt_number, " < --- crypt_number")

# Переводим в зашифрованный текст.
crypt_text = []
text = [crypt_text.append(chr(number)) for number in crypt_number ]

print(f"Зашифрованное сообщение: ", end="")
end_result = [print(i, end="") for i in crypt_text]

# я сделал так...
# хотя в пример получается совсем не так как у меня....
# -------------------------------------------------------------------------------
# Решение SkillBox
def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != " " else " ") for sym in string]
    new_str = " "
    for i_char in char_list:
        new_str += i_char
    return new_str

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя."
input_str =  input("\nВведите сообщение: ")
shift = int(input("Введите сдвиг: "))

output_str = caesar_cipher(input_str, shift)

print(f"Зашифрованное сообщение: {output_str}")
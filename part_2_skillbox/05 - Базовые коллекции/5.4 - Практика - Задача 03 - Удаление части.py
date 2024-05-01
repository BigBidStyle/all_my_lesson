# На вход в программу подаётся строка, состоящая из прописных и заглавных букв кириллицы.
# Напишите код, который проверяет,
# каких букв в строке больше, прописных или заглавных.
# Если заглавных букв больше,
# то сделать все буквы строки заглавными, иначе сделать все прописными.

# Подсказка: используйте методы islower() и/или isupper().


text = input("Введите текст: ")
lowers = len([letter for letter in text if letter.islower()])
uppers = len([letter for letter in text if letter.isupper()])

if lowers > uppers:
    print("Результат:", text.lower())
else:
    print("Результат:", text.upper())

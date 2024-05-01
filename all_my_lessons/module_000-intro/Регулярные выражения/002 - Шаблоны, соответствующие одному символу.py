import re

# . <-- Один любой символ, кроме новой строки \n.
print(re.findall(r'.', 'Привет,'))  # ['П', 'р', 'и', 'в', 'е', 'т', ',']
print('-' * 40)

# \d <-- Любая цифра.
print(re.findall(r'\d', 'СУ35, СУ111, АЛСУ14'))  # ['3', '5', '1', '1', '1', '1', '4']
print(re.findall(r'\d\d', 'СУ35, СУ111, АЛСУ14'))  # ['35', '11', '14']
print(re.findall(r'СУ\d\d', 'СУ35, СУ111, АЛСУ14'))  # ['СУ35', 'СУ11', 'СУ14']
print('-' * 40)

# \D <-- Любой символ, кроме цифры.
print(re.findall(r'926\D123', '926)123, 1926-1234'))  # ['926)123', '926-123']
print('-' * 40)

# \s <-- Любой пробельный символ (пробел, табуляция, конец строки и т.п.).
print(re.findall(r'бор\sода', '	бор ода, борода, борода'))  # ['бор ода']
print('-' * 40)

# \S <-- Любой не пробельный символ.
print(re.findall(r'\S123', 'X123, я123, !123456, 1 + 123456'))  # ['X123', 'я123', '!123']
print('-' * 40)

# \w <-- Любая буква (то, что может быть частью слова), а также цифры и _
print(re.findall(r'\w', 'Год, f_3, qwert'))
print('-' * 40)

# \W <-- Любая не-буква, не-цифра и не подчёркивание.
print(re.findall(r'com\W', 'com! com&'))  # ['com!', 'com&']
print('-', 40)

# [..] <-- Один из символов в скобках, а также любой символ из диапазона a-b
print(re.findall(r'[0-9][0-9A-Fa-f]', '12, 1F, 4B'))  # ['12', '1F', '4B']
print('-' * 40)

# [^..] <-- Любой символ, кроме перечисленных.
print(re.findall(r'[^>]', '<1>, <a>, <>>'))  # ['<', '1', ',', ' ', '<', 'a', ',', ' ', '<']
print('-' * 40)

# [abc-], [-1] <-- если нужен минус, его нужно указать последним или первым.
print(re.findall(r'[-1]', ' -123, 123'))    # ['-', '1', '1']
print('-' * 40)

# \b <-- Начало или конец слова (слева пусто или не-буква, справа буква и наоборот).
#     В отличие от предыдущих соответствует позиции, а не символу.
print(re.findall(r'\bвал', 'вал, перевал, Перевалка, валун'))   # ['вал', 'вал']
print('-' * 40)

# \B <-- Не граница слова: либо и слева, и справа буквы,
#     либо и слева, и справа НЕ буквы/
print(re.findall(r'\Bвал', 'вал, перевал, Перевалка, валун'))   # ['вал', 'вал']
print('-' * 40)
print(re.findall(r'\Bвал\B', 'вал, перевал, Перевалка, валун')) # ['вал']



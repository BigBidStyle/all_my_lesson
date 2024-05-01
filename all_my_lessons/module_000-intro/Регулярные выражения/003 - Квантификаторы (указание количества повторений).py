import re

# {n} <--	Ровно n повторений	\d{4}	1, 12, 123, 1234, 12345
print(re.findall(r'\d{4}', '1, 12, 123, 1234, 12345')) # ['1234', '1234']
print('-' * 40)

# {m, n} <-- От m до n повторений включительно	\d{2,4}	1, 12, 123, 1234, 12345
print(re.findall(r'\d{2,4}', '1, 12, 123, 1234, 12345')) # ['12', '123', '1234', '1234']
print('-' * 40)

# {m, } <-- Не менее m повторений	\d{3,}	1, 12, 123, 1234, 12345
print(re.findall(r'\d{3,}', '1, 12, 123, 1234, 12345')) # ['123', '1234', '12345']
print('-' * 40)

# {, n} <-- Не более n повторений	\d{,2}	1, 12, 123
print(re.findall(r'\d{,2}', '1, 12, 123')) # ['1', '', '', '12', '', '', '12', '3', '']
print('-' * 40)

# ?	<-- Ноль или одно вхождение, синоним {0,1}	валы?	вал, валы, валов
print(re.findall(r'валы?', 'валы?	вал, валы, валов')) # ['валы', 'вал', 'валы', 'вал']
print('-' * 40)

# *	<-- Ноль или более, синоним {0,}	СУ\d*	СУ, СУ1, СУ12, ...
print(re.findall(r'СУ\d*', 'СУ, СУ1, СУ12')) # ['СУ', 'СУ1', 'СУ12']
print('-' * 40)

# +	<-- Одно или более, синоним {1,}	a\)+	a), a)), a))), ba)])
print(re.findall(r'a\)+', 'a), a)), a))), ba)])')) # ['a)', 'a))', 'a)))', 'a)']
print('-' * 40)

# *?, +?, ??, {m,n}?, {, n}?, {m, }? <-- По умолчанию квантификаторы жадные —
# захватывают максимально возможное число символов.
# Добавление ? Делает их ленивыми,
# они захватывают минимально возможное число символов
print(re.findall(r'\(.*\)', '(a + b) * (c + d) * (e + f)')) # ['(a + b) * (c + d) * (e + f)']
print('-' * 40)
print(re.findall(r'\(.*?\)', '(a + b) * (c + d) * (e + f)')) # ['(a + b)', '(c + d)', '(e + f)']


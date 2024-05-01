import re

text = 'AV is largest Analytics community of India. India!'
result_1 = re.findall(r'.', text) # Взять все символы из текста включая пробелы.
result_2 = re.findall(r'\w', text)  # Взять из текста все числа и буквы.
result_3 = re.findall(r'\w+', text)  # Взять из текста все слова.
result_4 = re.findall(r'\b[aeiouAEIOU]\w+', text) # Взять из текста все слова, которые начинаются с букв из списка.

print(result_4) # ['A', 'V', ' ', 'i', 's', ' ', ....
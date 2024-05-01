import re  # regular expressions (регулярные выражения)

text = 'AV - Analytics Vidhya AV'
result = re.match(r'AV', text)  # <-- Поиск в начале строки по шаблону.
print('Поиск в начале строки по шаблону: ', result)
print(result.group(0))  # Если есть объект, то вытаскиваем результат...
print(result.start())  # С какого индекса начинается шаблон.
print(result.end())  # Каким индексом заканчивается шаблон.

result = re.match(r'Analytics', text)
print(result)

print('=' * 40)
result = re.search(r'Analytics', text)  # Поиск в строке по шаблону.
print('Поиск в строке по шаблону: ', result)
print(result.group(0))

print('=' * 40)
result = re.findall(r'AV', text)  # Все совпадения по шаблону.
print('Все совпадения по шаблону: ', result)
print('=' * 40)

text_2 = 'AV is largest Analytics community of India. India!'
result = re.sub(r'India', 'the world', text_2)  # Замена всех найденных шаблонов.
print('Замена всех найденных шаблонов: ', result)
print('=' * 40)

pattern = re.compile('AV')
result = pattern.findall(text)
print(result)
result2 = pattern.findall(text_2)
print(result2)

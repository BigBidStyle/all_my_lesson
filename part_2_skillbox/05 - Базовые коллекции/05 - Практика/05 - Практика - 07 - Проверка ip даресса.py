# Что нужно сделать
#
# При написании клиент-серверного приложения часто приходится работать с теми самыми IP-адресами.
# Как вы уже знаете, IP-адрес состоит из четырёх целых чисел в диапазоне от 0 до 255, разделённых точками.
#
# Пользователь вводит строку. Напишите программу, которая определяет, является ли заданная строка правильным
# IP-адресом. Обеспечьте контроль ввода, где предусматривается ввод целых чисел от 0 до 255, а также точки между ними.

# Пример 1:
# Введите IP: 128.16.35.a4
# a4 — это не целое число.

# Пример 2:
# Введите IP: 128.16.35.a4
# 340 превышает 255.

# Пример 3:
# Введите IP: 34.56.42,5
# Адрес — это четыре числа, разделённые точками.

# Пример 4:
# Введите IP: 128.0.0.255
# IP-адрес корректен.

# # ----------------

# def check_ip():
#     ip = input("Введите IP: ")
#     ip = ip.split(".")
#     if len(ip) != 4:
#         print(f'Здесь чисел {len(ip)}, а должно быть четыре.')
#         check_ip()
#
#
#
#     for (number) in ip:
#         if int(number) > 255:
#             print(f"{number} превышает 255")
#             check_ip()
#         if int(number) < 0:
#             print(f"{number} меньше нуля")
#             check_ip()
#
#     return print('IP-адрес корректен.')
#
#
# check_ip()

# count_point = ip.count(".")
#     if 0 <= count_point > 3:
#         print("Адрес — это четыре числа, разделённые точками.")
# ------------------------------------
# import string library function
import string

# Storing the sets of punctuation in variable result
result = string.punctuation

# Printing the punctuation values
print(result)

from string import punctuation
from string import whitespace
#==============================================================================
def check_IP(s):
    p = set(s) & set(punctuation) - set('-')
    print(set(s))
    print(p)
    if p != set('.'):
        return f'{p}Адрес — это числа, разделенные точками.'
    lis = s.split('.')
    lis_n = []
    for e in lis:
        try:
            lis_n.append( int(e) )
        except:
            if e in whitespace:
                return f'Пробельный символ - это не целое число.'
            return f'{e} - это не целое число.'
    if len( lis_n ) != 4:
        return f'Здесь чисел { len( lis_n ) }, а должно быть четыре.'
    for n in lis_n:
        if n < 0:
            return f'{n} меньше нуля.'
        if n > 255:
            return f'{n} превышает 255.'
    return 'IP-адрес корректен.'
#==============================================================================
s = input('Введите IP: ')
print( check_IP(s) )
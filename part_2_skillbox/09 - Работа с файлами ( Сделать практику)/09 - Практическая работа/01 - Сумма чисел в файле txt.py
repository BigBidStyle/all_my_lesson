# Задача 1. Сумма чисел 2
# Что нужно сделать
# Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк.
# Напишите программу, которая выводит сумму чисел во выходной файл answer.txt.

# Пример:
# Содержимое файла numbers.txt
#      2
# 2
#   2
#         2
#
# Содержимое файла answer.txt
# 8

# Решение задачи 1.
numbers_file = open('numbers.txt', 'r', encoding='utf-8') # 'r' <-- считать файл.
data = numbers_file.read() # Записываем в переменную data.
numbers_file.close() # Закрываем файл.
sum_numbers = 0

for seed in data:
    for e_num in range(0, 9):
        if seed == str(e_num):
            sum_numbers += e_num

save_answer = open('answer.txt', 'w', ) # Открываем файл для записи.
save_answer.write(str(sum_numbers)) # Записываем значение.
save_answer.close() # Закрываем файл.




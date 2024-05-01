# Задача 5. Текстовый редактор
# Что нужно сделать

# Мы продолжаем разрабатывать новый текстовый редактор, и в этот раз нам поручили
# написать для него код, который считает количество любой буквы и любой цифры в тексте
# (а не только буквы Ы, как раньше).

# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое
# в нём количество цифр K и букв N. Функция должна вывести на экран информацию о
# найденных буквах и цифрах в определённом формате.

# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л
# Количество цифр 0: 2
# Количество букв л: 1

# Что оценивается
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# формат вывода соответствует примеру;
# вывод содержит описание результата (выведенные числа сопровождаются текстовым описанием).

def count_letters(text,K,N):
    count_K = count_N = 0
    for symbol in text:
        if symbol == K:
            count_K += 1
        elif symbol == N:
            count_N += 1
    print(f"Кол-во цифр {K} в тексте: {count_K}")
    print(f"Кол-во букв {N} в тексте: {count_N}")

text = input("Введите текст: ")
K = input("Какую цифру ищем: ")
N = input("Какую букву ищем: ")

count_letters(text,K,N)
# Задача 2. Я стал новым пиратом!
# Что нужно сделать
# Старому капитану необходимо пополнить команду. Но попадут на его корабль только достойные!
# Он отобрал 10 человек и те, кто из них крикнет слово “Карамба”, попадут на борт.

# Пользователь вводит 10 слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».
# Что оценивается
# Задание считается успешно выполненным, если:
# результат вывода соответствует условию;
# input содержит корректное приглашение для ввода;
# Программа игнорирует регистр первой буквы “К”
# Переменные имеют значащие имена, не только a, b, c, d (видео 2.3)

count = 0
for people in range (1,10):
    word = input("Введити слово: ")
    if (word == "карамба") or (word == "Карамба"):
        count += 1
print("Пиратов, правильно произнесших слово и попавших на борт: ", count)
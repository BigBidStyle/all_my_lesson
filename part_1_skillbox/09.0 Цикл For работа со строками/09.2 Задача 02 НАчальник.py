# Задача 2. Начальник
# Напишите программу для робота-начальника. Он спрашивает у пользователя, выполнил ли он
# задание, которые выдавал вчера, и продолжает это делать до тех пор, пока тот не ответит ему
# “Да, конечно, сделал”.
answer = ""
while answer != "Да, конечно, сделал" :
    answer = input("Выполнил ли он задание, которые выдавал вчера?: ")
    
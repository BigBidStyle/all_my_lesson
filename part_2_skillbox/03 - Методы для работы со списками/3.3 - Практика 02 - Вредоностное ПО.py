# Гера решил попрактиковаться в программировании и захотел написать небольшой скрипт,
# который после двух сообщений отправляет ещё одно на основе первых двух.
#
# Пользователь вводит две строки. В каждой из них есть какое-то количество специальных символов ! и ?.
# Напишите программу, которая считает количество этих символов отдельно в первой строке и отдельно во второй.
# Если в первой строке их больше, чем во второй, то на экран выводится первая строчка, объединённая со второй,
# а иначе — вторая с первой. При равном количестве символов в строках выводится «Ой».

# Пример 1:
# Первое сообщение: Привет!
# Второе сообщение: Как дела? Что делаешь?
# Третье сообщение: Как дела? Что делаешь? Привет!

# Пример 2:
# Первое сообщение: Хм!!
# Второе сообщение: ?
# Третье сообщение: Хм!!?

count = 0
def count(massage):
    count_massage_1 = massage.count("!")
    count_massage_2 = massage.count("?")
    count = count_massage_1 + count_massage_2
    return count

print("Первое сообщение: ", end="")
first_massage = input()
print("Второе сообщение: ",end="")
last_massage = input()

count_first_massage = int(count(first_massage))
count_last_message = int(count(last_massage))

if count_first_massage > count_last_message:
    print(first_massage,  last_massage)
elif count_first_massage < count_last_message:
    print(last_massage,  first_massage)
else:
    print("Ой")


# Решенеи SkillBox
first_word = input("Первое сообщение: ")
second_word = input("Первое сообщение: ")
first_count = first_word.count("!") + first_word.count("?")
second_count = second_word.count("!") + second_word.count("?")
if first_count < second_count:
    first_word, second_word = second_word, first_word  # пусть первым словом будет то, в котором больше знаков

print(first_word + second_word)
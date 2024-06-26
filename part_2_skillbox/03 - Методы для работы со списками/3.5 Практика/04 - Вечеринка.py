# В честь своего дня рождения Артём решил закатить вечеринку у себя на даче.
# Он не стал рассылать приглашения, а просто сообщил всем: «Если хотите — приходите и своих друзей тоже зовите».
# В ходе вечеринки люди приходили и уходили, ночевать остались не все. К тому же и сама дача не резиновая — на ней помещается всего шесть человек.

# Дан изначальный список гостей — имена тех, кто пришёл к началу:

# guests = [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
# Напишите программу, которая спрашивает у пользователя, ушёл человек или пришёл новый гость, и,
# исходя из ответа, добавляет в список или удаляет из него нужное имя.
# При этом гостей может быть не больше шести. Имена запрашиваются до тех пор, пока пользователь не введёт сообщение «Пора спать».

# Пример:

# Сейчас на вечеринке 5 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’]
# Гость пришёл или ушёл? пришёл
# Имя гостя: Алекс
# Привет, Алекс!

# Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# Гость пришёл или ушёл? пришёл
# Имя гостя: Гоша
# Прости, Гоша, но мест нет.

# Сейчас на вечеринке 6 человек: [‘Петя’, ‘Ваня’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# Гость пришёл или ушёл? ушёл
# Имя гостя: Ваня
# Пока, Ваня!

# Сейчас на вечеринке 5 человек: [‘Петя’, ‘Саша’, ‘Лиза’, ‘Катя’, ‘Алекс’]
# Гость пришёл или ушёл? Пора спать

# Вечеринка закончилась, все легли спать.

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

while True:
    humans = len(guests)
    print(f"Сейчас на вечеринке {humans} человек: {guests}")

    print(f"Гость пришел или ушел?: ", end="")
    comand = input()

    if comand == "пришел":
        print("Имя гостя: ", end="")
        name = input()
        if humans <= 5:
            guests.append(name)
            print(f"Привет {name}!\n")
        else:
            print(f"Прости, {name}, но мест нет.\n")

    elif comand == "ушел":
        print("Имя гостя: ", end="")
        name = input()
        guests.remove(name)
        print(f"Пока {name}!\n")

    elif comand == "пора спать":
        print("Вечеринка закончилась.")
        break



# Что нужно сделать
# Мы пишем приложение для удобного прослушивания музыки.
# У Вани есть список из девяти песен группы Depeche Mode. Каждая песня состоит
# из названия и продолжительности с точностью до долей минут:

# violator_songs = [
#     ['World in My Eyes', 4,86],
#     ['Sweetest Perfection', 4,43],
#     ['Personal Jesus', 4,56],
#     ['Halo', 4,9],
#     ['Waiting for the Night', 6,07],
#     ['Enjoy the Silence', 4,20],
#     ['Policy of Truth', 4,76],
#     ['Blue Dress', 4,29],
#     ['Clean', 5,83]
# ]

# Из этого списка Ваня хочет выбрать N песен и закинуть их в особый плейлист с другими треками. И
# при этом ему важно, сколько времени в сумме эти N песен будут звучать.
# Напишите программу, которая запрашивает у пользователя количество песен из списка
# и затем названия этих песен, а на экран выводит общее время их звучания.

# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean

# Общее время звучания песен: 14,93 минуты

# Решение задачи.
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]]

print("Сколько песен брать: ", end="")
number = int(input())
time = 0
for n in range(number):
    print(f"Название {n + 1}-й песни: ",end="")
    search_song = input()
    for i_song in violator_songs:
        if i_song[0] == search_song:
            time += i_song[1]
print(f"\nОбщее время звучания песен: {round(time, 2)} минуты.")


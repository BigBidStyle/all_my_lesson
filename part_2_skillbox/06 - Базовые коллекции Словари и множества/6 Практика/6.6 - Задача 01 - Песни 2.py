# Что нужно сделать

# Мы продолжаем писать приложение для удобного прослушивания музыки, но теперь наши
# песни хранятся в виде словаря, а не вложенных списков. Каждая песня состоит из названия
# и продолжительности с точностью до долей минут.

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }

# Напишите программу, которая запрашивает у пользователя количество песен из списка и
# названия этих песен, а на экран выводит общее время их звучания.

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

print("Сколько песен брать: ", end="")
number = int(input())
time = 0
for n in range(number):
    print(f"Название {n + 1}-й песни: ", end="")
    search_song = input()
    for i_song in violator_songs:
        if i_song == search_song:
            time += violator_songs[i_song]
print(f"\nОбщее время звучания песен: {round(time, 2)} минуты.")
def is_film_exist(movie, films_list):
    for i_movie in films_list:
        if i_movie == movie:
            return True
    return False

films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия",
         "Город грехов", "Мементо", "Отступники", "Деревня"]

my_list = []

while True:
    print("\nВаш текущий список фильмов: ", my_list)
    new_movie = input("Название  фильма: ")
    if is_film_exist(new_movie, films):
        print("Команды: добавить, удалить, вставить")
        comand = input("Введите команду: ")
        if comand == "Добавить":
            my_list.append(new_movie)
        if comand == "Удалить":
            if is_film_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print("Такого фильма нет в вашем рейтинге.")
        if comand == "Вставить":
            index = int(input("На какое место вставить: "))
            my_list.insert(index - 1, new_movie)

    else:
        print("Такого фильма нет на сайте.")

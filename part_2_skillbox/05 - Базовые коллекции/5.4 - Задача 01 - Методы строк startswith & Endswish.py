user_name = input("Введите имя пользователя: ")
file_name = input("Введите имя файла: ")

path = "c:/{user}/docs/folder/{new_file}".format(user=user_name, new_file=file_name)

if not path.endswith(".txt"):
    print("Ошибка! Неверное расширение файла!")
elif not path.startswith("c:/"):
    print("Ошибка! Неверно указан диск!")
else:
    print("Путь к файлу: ", path)
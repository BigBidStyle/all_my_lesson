def ask_user(question,
             complaint='Неверный ввод. Введите да/нет. ',
             retries=4):     # Вопрос, ошибка, кол-во попыток
    while True:
        answer = input(question).lower()
        if answer == "да":
            return
        if answer == "нет":
            return
        retries -= 1
        if retries == 0:
            print("Кол-во попыток истекло.")
            break
        print(complaint)
        print('Осталось попыток', retries)


ask_user("Вы действительно хотите выйти? ")
ask_user("Удалить файл? ", "Так удали ть или нет? ")
ask_user("Записать файл? ", retries=2)

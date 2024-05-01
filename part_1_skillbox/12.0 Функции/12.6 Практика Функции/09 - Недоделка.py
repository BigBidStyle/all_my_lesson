# Задача 9. Недоделка
# Что нужно сделать

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория — дети и их родители. У прошлого программиста
# было задание сделать две игры в одном приложении, чтобы пользователь
# мог выбирать одну из них. Однако программист, на место которого вы пришли,
# перед увольнением не успел сделать эту задачу и оставил только небольшой
# шаблон проекта. Используя этот шаблон, реализуйте игры «Камень,
# ножницы, бумага» и «Угадай число».

# Правила игры «Камень, ножницы, бумага»: программа запрашивает у
# пользователя строку и выводит, победил он или проиграл. Камень бьёт ножницы,
# ножницы режут бумагу, бумага кроет камень.

# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор,
# пока он его не отгадает.
import random
def rock_paper_scissors():
    # Здесь будет игра "Камень, ножницы, бумага"
    robot = random.choice(['камень', 'ножницы', 'бумага'])
    human = str(input("\nЧто выбираете: камень, ножницы, бумага?: "))

    if (robot == 'камень' and human == 'бумага') or (robot == 'ножницы' and human == 'камень') or (
                robot == 'бумага' and human == 'ножницы'):
        print(f"Победа!!! Робот выбрал {robot}\n")
    elif robot == human:
        print(f"Ничья! Робот выбрал {robot}\n")

    else:
        print(f"Вы проиграли! Робот выбрал {robot}\n")
    mainMenu()

def guess_the_number():
    # Здесь будет игра "Угадай число"
    code = random.randint(1,100)
    count = 0
    while True:
        number = int(input("\nКакое число загадано? (1 до 100) : "))
        if number > code:
            print("Число больше, чем нужно. Попробуйте ещё раз!")
            count += 1
        elif number < code:
            print("Число меньше, чем нужно. Попробуйте ещё раз!")
            count += 1
        else:
            print("Вы угадали! Число попыток", count, "\n")
            break
    mainMenu()

def mainMenu():
    # Здесь главное меню игры
    choice = int(input("Какую игру выбираете? \n"
                       "1 - камень,ножницы,бумага\n"
                       "2 - Угадай число\n"
                       "3 - Выход\n"
                       "Ваш выбор: "))

    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    elif choice == 3:
        print("")
    else:
        print("Ошибка ввода!")
    mainMenu()

mainMenu()

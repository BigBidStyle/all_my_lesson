# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
first_name = ''
age = 0
phone = ''
email = ''
mail_index = ''
postal_address = ''
info = ''

# bank profile
ogrnip = ''
inn = ''
payment_account = ''
name_bank = ''
bik = ''
correspondent_account = ''

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break

            if option2 == 1:
                # input general info
                first_name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    else:
                        print('Возраст должен быть положительным')

                uphone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ch = ''
                for ch in uphone:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')
                mail_index = int(input("Введите почтовый индекс: "))
                postal_address = input('Введите почтовый адрес (без индекса): ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input bank requisites
                def count_digit(n):
                    digit = 0
                    while n > 0:
                        i = n // 10
                        n = i
                        digit += 1
                    return digit

                while 1:
                    ogrnip = int(input("Введите ОГРНИП: "))
                    count = count_digit(ogrnip)
                    if count == 15:
                        break
                    else:
                        print("ОГРНИП должен содержать 15 цифр")

                inn = int(input("Введите ИНН: "))

                while 2:
                    payment_account = int(input("Введите расчетный счет: "))
                    count = count_digit(payment_account)
                    if count == 20:
                        break
                    else:
                        print("Расчетный счет должен содержать 20 цифр")

                name_bank = input("Введите название банка: ")
                bik = int(input("Введите БИК: "))
                correspondent_account = int(input("Введите корреспондентский счет: "))

            else:
                print('Введите корректный пункт меню')

    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))

            def option():
                print(SEPARATOR)
                print('Имя: ', first_name)
                if 11 <= age % 100 <= 19:
                    years_name = 'лет'
                elif age % 10 == 1:
                    years_name = 'год'
                elif 2 <= age % 10 <= 4:
                    years_name = 'года'
                else:
                    years_name = 'лет'

                print(f"Возраст: {age, years_name}")
                print(f"Телефон: {phone}")
                print(f"E-mail: {email}")
                print(f"Почтовый индекс: {mail_index}")
                print(f"Почтовый адрес: {postal_address}")
                if info:
                    print(f"'Дополнительная информация:{info}")

            if option2 == 0:
                break

            if option2 == 1:
                # print general information
                option()

            elif option2 == 2:
                # print full information
                option()
                print("\nИНФОРМАЦИЯ О ПРЕДПРИНИМАТЕЛЕ")
                print(f"ОГРНИП: {ogrnip}")
                print(f"ИНН: {inn}")
                print(f"Введите расчетный счет: {payment_account}")
                print(f"Название банка: {name_bank}")
                print(f"БИК: {bik}")
                print(f"Корреспондентский счет: {correspondent_account}")
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')

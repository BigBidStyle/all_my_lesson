rate_check = False
while True:
    active = int(input("Продолжаем работать? 1/0: "))
    if active == 0:
        print("Приложение закрывается....")
        break
    rate = int(input("Поставите оценку приложению? 1/0: "))
    if rate == 1:
        rate_check = True
print("Работа завершена")
if rate_check:
    print("Пользователь оставил оценку")
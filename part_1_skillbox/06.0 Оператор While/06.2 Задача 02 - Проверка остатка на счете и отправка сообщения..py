print("Задача № 2 -Проверка остатка на счете и отправка сообщения.")
balance = int(input("Сколько денег пришло?: "))
while balance >= 5000:
    product_cost = int(input("Стомость товара: "))
    balance -= product_cost
    print("В кошельке осталось", balance)
print("На счету осталось мало денег! Остановись!!!!")
print("Баланс", balance, "рублей")
print("Задача № 3 - Накопления.")
money = int(input("Сколько отложить денег?: "))
summa = 0
while money < 500000:
    summa += money
    print("Накоплено: ",summa, "рублей")
    money = int(input("Сколько отложить денег?: "))
print("Накопили нужную сумму")
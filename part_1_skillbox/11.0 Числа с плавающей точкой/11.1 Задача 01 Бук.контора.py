bet = int(input("Сумма ставки?: "))
coeff = float(input("Какой коэфициент?: "))
win = round(bet * coeff - bet, 2)
print("Потенциальный выйгрыш : ", win, "рублей")
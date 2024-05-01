print("Теория - Задача № 1 - Лотерея")
winner = 0
for ticket in 345,20,87,1020,421,555:
    if ticket % 5 == 0:
        print(ticket, " <--- cчастливый билетик!")
        winner += 1
print("Кол-во победителей", winner)
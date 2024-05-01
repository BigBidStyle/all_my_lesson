summ = 0
total_months = int(input("Сколько месяцев будет копить Алексей: "))
for total_count in range(total_months):
    money = int(input("Сколько откладывать денег каждый месяц: "))
    summ += money
    print("Через", total_count + 1, "месяцев Алексей накопит", summ, "рублей")

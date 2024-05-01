# Задача 7. Стипендия
# Что нужно сделать
#
# Ежемесячная стипендия студента составляет educational_grant рублей, а
# расходы на проживание превышают стипендию и составляют expenses рублей в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца. Составьте
# программу расчёта суммы денег, которую необходимо получить у родителей один раз в
# начале обучения, чтобы можно было прожить учебный год (десять месяцев), используя
# только эти деньги и стипендию.

# Пример:
# Введите стипендию: 10000
# Введите расходы на проживание: 13000
# У родителей необходимо попросить 49030.431

educational_grant = int(input("Ежемесячная стипендия составляет: "))
expenses = int(input("Введите расходы на проживание: "))
summ = expenses - educational_grant
for i in range(1, 9 + 1 ,1):
    expenses += expenses / 100 * 3
    print(expenses)
    summ += expenses - educational_grant
print(f"У родителей на учебу надо попросить {summ} денег. ")
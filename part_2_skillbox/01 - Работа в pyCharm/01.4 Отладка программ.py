number = int(input("Введите число: "))
summa = 0

while number != 0:
    last_num = number % 10
    summa += last_num
    if last_num == 5:
        print("Обнаружен разрыв")
        break
    number //= 10
    print("Текущая сумма цифр", summa)

print("\nИтоговая сумма цифр: ", summa)
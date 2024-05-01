for attempt in range(1,4):
    pincode = int(input("Введите пин-код: "))
    if pincode == 1234:
        print("Пин код верный. Заберите ваши деньги.")
        break
    print(f"Не верный пин-код. Осталось {3- attempt} попытки.")
else:
    print("Ваша карта заблокирована.")
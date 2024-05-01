height = float(input("Введите рост человека? : "))
weight = float(input("Введите вес человека? : "))
index = round(weight / height ** 2, 2)
print("Ваш индекс массы тела : ", index, "кг.")

if index < 18.5:
    print("У вас недостаточная масса тела.")
elif index < 25:
    print("У вас нормальная масса тела.")
elif index < 30:
    print("У вас избыточная масса тела.")
else:
    print("У вас ожирение!")
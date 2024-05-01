def calculate_tax(price, tax):
    total = price + (price * tax / 100)
    print(total)
    return total

myPrice = float(input("Введите цену: "))
myTax = int(input("Введите налог в процентах: "))

totalPrice =  calculate_tax(myPrice, myTax)

newTax = int(input("Введите новый налог: "))
totalPrice = calculate_tax(totalPrice, newTax)

print(f"Итоговая цена: {totalPrice}")
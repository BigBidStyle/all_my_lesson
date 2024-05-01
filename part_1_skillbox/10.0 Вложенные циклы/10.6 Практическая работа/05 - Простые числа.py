countNumber = 0
for number in range(int(input("Введите кол-во чисел: "))):
    isPrime = True
    number = int(input("Введите число: "))
    for divider in range(2, number):
        if number % divider == 0:
            isPrime = False
            break
    if isPrime:
        print("Натуральное число")
        countNumber += 1
print(f"Кол-во простых чисел: {countNumber}")


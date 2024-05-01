n = int(input("Введите число: "))
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(row, end =' ')
    print()
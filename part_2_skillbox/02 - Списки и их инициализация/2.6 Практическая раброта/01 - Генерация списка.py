N = int(input("Введите челое число: "))
numbers = []

for i in range(N):
    if i % 2 != 0:
        numbers.append(i)
print(f"Список из нечетных чисел от одного до N: {numbers}")
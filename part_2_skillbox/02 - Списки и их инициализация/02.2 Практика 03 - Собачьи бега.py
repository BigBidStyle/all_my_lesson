# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен баг:
# собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.

# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

N = int(input('Кол-во чисел в списке: '))
nums_list = []

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

if nums_list:
    maximum = nums_list[0]
    minimum = nums_list[0]

    minimum_index = 0
    maximum_index = 0
    for index, i in enumerate(nums_list):

        if maximum < i:
            maximum = i
            maximum_index = index

        if minimum > i:
            minimum = i
            minimum_index = index

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)

    print(nums_list)
    nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
    print(nums_list)
else:
    print('В списке нету чисел')


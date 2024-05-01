# Частная контора даёт в прокат ролики самых разных размеров.
# Человек может надеть ролики любого размера, которые не меньше размера его ноги.
#
# Пользователь вводит два списка размеров: N размеров коньков и K размеров ног людей.
# Реализуйте код, который определяет, какое наибольшее число человек сможет одновременно взять ролики и пойти покататься.

# Пример:
# Кол-во коньков: 4
# Размер 1-й пары: 41
# Размер 2-й пары: 40
# Размер 3-й пары: 39
# Размер 4-й пары: 42

# Кол-во людей: 3
# Размер ноги 1-го человека: 42
# Размер ноги 2-го человека: 41
# Размер ноги 3-го человека: 42

# Наибольшее кол-во людей, которые могут взять ролики: 2

size_list = []
number = int(input("Кол-во коньков: "))

for i in range(number):
    print(f"Размер {i + 1}-й пары: ", end="")
    size = int(input())
    size_list.append(size)
size_list.sort()

print("\n")
human_list = []
human = int(input("Кол-во людей: "))

for man in range(human):
    print(f"Размер ноги {man + 1}-го человека: ", end="")
    size_human = int(input())
    human_list.append(size_human)
human_list.sort()

count = 0
for count_1 in range(len(human_list)):
    for count_2 in range(len(size_list)):
        if human_list[count_1] >= size_list[count_2]:
            size_list[count_2] = 0
            count += 1
            break
print(f"Наибольшее кол-во людей, которые могут взять ролики: {count}")

while True:
    grats_template = input("Введите шаблок поздравления. \nВ шаблоне надо использовать"
                       "конструкцию {name}\n: ")

    if "{name}" in grats_template:    # если эта строка есть в этой строке.
        break
    print("Ошибка! Отсутствует конструкция {name}\n")

print("Введите список имен (заканчивается на end):")
names_list = []
while True:
    name = input("Имя: ")
    if name != "end":
        names_list.append(name)
    else:
        break

for i_name in names_list:
    print(grats_template.format(name=i_name))
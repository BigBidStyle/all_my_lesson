# text = input("Содержимое файла: ")
# word_list = text.split()
#
# print(word_list)
#
# new_text = "---".join(word_list)
# print(new_text)
# # ------------------------------------------
while True:
    # Создаем переменную grats_template и в нее вписываем, что мы наблон
    grats_template = input("Введите шаблон поздравления. \nВ шаблоне надо использовать"
                       " конструкцию {name} и {age}\n: ")

    # Проверяем есть ли в переменной grats_template конструкции {name} и {age}
    if "{name}" in grats_template and "{age}" in grats_template:    # если эта строка есть в этой строке.
        break
    print("Ошибка! Отсутствует конструкция {name} или {age}\n")

# создаем переменную names_list и вносим людей через запятую с пробелом так как указщано в split....
names_list = input("Список людей через запятую с пробелом: ").split(", ")

# создаем переменную age_str и вносим туда возраста через пробел
age_str = input("Возраст людей через пробел: ")

# создаем лист  ages через переменную age_str и вносим уже в список (int) числовые значения
ages = [int(i_number) for i_number in age_str.split()]

# Через переменную i_man в цикле выводим сообщение на экран
for i_man in range(len(names_list)):
    print(grats_template.format(name=names_list[i_man], age=ages[i_man]))


people = [" ".join([names_list[i_man], str(ages[i_man])])
          for i_man in range(len(names_list))]

people_str = ", ".join(people)
print("\nИменины", people_str)
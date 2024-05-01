# Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):

# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }

# Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, кол-во лет и дети.
# Затем, с помощью метода get и установки значения по умолчанию, проверьте есть ли ребёнок с именем Bob.
# Затем в отдельную переменную получите фамилию этого ребёнка и выведите её на экран.
# Если у него нет фамилии, то получите значение ‘Nosurname’.

family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6},
        {
            "name": "Bob",
            "age": 8}]}




# Созадем словарь (дети)
childrens_dict = {}

search_bob = childrens_dict.get("Bob")
if search_bob:
    print("Bob найден")
else:
    print("Bob-а нету!")

childrens_surname = family_member.get("surname")
if childrens_surname:
    print(childrens_surname)
else:
    print("Nosurname")
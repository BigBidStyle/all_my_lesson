# Старое решение  Решали в задаче 02.2 Задача 01
# monster_count = int(input("Кол-во монстров: "))
# mage_index = int(input("Номер мага в списке: "))
# monsters_damage = []
#
# for monster in range(monster_count):
#     print("Урон у", monster + 1 , "монстра: ", end=" ")
#     damage = int(input())
#     monsters_damage.append(damage)
#
# for i_monster in range(monster_count):
#     if monsters_damage[i_monster] < 100 and i_monster != mage_index - 1:
#         monsters_damage[i_monster] += monsters_damage[mage_index - 1]
#
# print(f"Итоговый урон монстров: {monsters_damage}")

# -------------------------------------------------
import random
# Заполняем список (меотдом рандов в промежутке от 50 до 80 и вывеси ресчет от 0 до 10.
squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3_conditioin =[("Погиб" if squad_1[i_damage] + squad_2[i_damage] > 100 else "Выжил")
                     for i_damage in range(10)]

print(f"Урон первого отряда: {squad_1}")
print(f"Урон второго отряда: {squad_2}")
print(f"Состояние третьего отряда:: {squad_3_conditioin}")
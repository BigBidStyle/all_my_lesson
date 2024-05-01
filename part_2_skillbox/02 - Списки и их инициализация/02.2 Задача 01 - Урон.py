monster_count = int(input("Кол-во монстров: "))
mage_index = int(input("Номер мага в списке: "))
monsters_damage = []

for monster in range(monster_count):
    print("Урон у", monster + 1 , "монстра: ", end=" ")
    damage = int(input())
    monsters_damage.append(damage)

for i_monster in range(monster_count):
    if monsters_damage[i_monster] < 100 and i_monster != mage_index - 1:
        monsters_damage[i_monster] += monsters_damage[mage_index - 1]

print(f"Итоговый урон монстров: {monsters_damage}")


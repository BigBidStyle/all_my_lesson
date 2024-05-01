print("Теория - Задача № 2 - Здоровый сон")
wake_up = int(input("Во сколько проснулся Саша?: "))
awake_hours = 0
calories_sum = 0
for hour in range(wake_up, 23):
    print("Сейчас", hour,"Часов")
    calories = int(input("Сколько съел за час?: "))
    calories_sum += calories
    awake_hours += 1
    if calories_sum > 2000:
        print("Хорошо поел, можно и поспать!))")
        break
print("Съедено калорий за день: ", calories_sum)
print("Часов не спал: ", awake_hours)
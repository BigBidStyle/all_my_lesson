values = ["a", "b", "c"]
for count, value in enumerate(values):
    print(count, value)     # 0 a 1 b 2 c

# Здесь можно увидеть, что доступ к значениям с индексом 0 дает первый элемент a. Бывает так, что необходимо запустить
# счетчик не с 0. В этом случае используйте аргумент start для enumerate(), чтобы изменить начальный счетчик:
print('-------')
for count, value in enumerate(values, start=1):
   print(count, value)  # 1 a 2 b 3 c


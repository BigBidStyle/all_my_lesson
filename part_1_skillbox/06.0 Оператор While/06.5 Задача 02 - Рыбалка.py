print("Задача №2 .")
bags =int(input("Сколько нужно перетащить мешков?: "))
totalWeight = 0
bag_count = 0
while bag_count < bags:
    weight = int(input("Сколько весит мешок?: "))
    totalWeight += weight
    bag_count += 1
print("Общий вес мешков", totalWeight)
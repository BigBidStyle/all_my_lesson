import marisa_trie

# Создание экземпляра дерева префиксов
trie = marisa_trie.Trie(["apple", "banana", "orange", "app"])

# Проверка наличия элементов
print("apple" in trie)  # Вывод: True
print("pear" in trie)  # Вывод: False

# Получение значения элемента
print(trie["banana"])  # Вывод: banana

# Поиск всех элементов с заданным префиксом
prefixes = trie.items("app")
print(list(prefixes))  # Вывод: [('app', 0), ('apple', 3)]

# Автодополнение
suggestions = trie.keys("app")
print(list(suggestions))  # Вывод: ['app', 'apple']
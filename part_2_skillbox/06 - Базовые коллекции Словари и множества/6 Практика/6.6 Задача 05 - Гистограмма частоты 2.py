# Мы уже писали программу для лингвистов, которая получала на вход текст и считала,
# сколько раз в строке встречается каждый символ. Теперь задача немного поменялась:
# максимальную частоту выводить не нужно, однако необходимо написать функцию, которая
# будет инвертировать полученный словарь. То есть в качестве ключа будет частота, а в
# качестве значения — список символов с этой частотой. Реализуйте такую программу.

# Пример:
# Введите текст: здесь что-то написано
# Оригинальный словарь частот:

#   : 2
# - : 1
# З : 1
# а : 2
# д : 1
# е : 1
# и : 1
# н : 2
# о : 3
# п : 1
# с : 2
# т : 2
# ч : 1
# ь : 1

# Инвертированный словарь частот:
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
# 2 : ['с', ' ', 'т', 'н', 'а']
# 3 : ['о']

count = 0
text = input("Введите текст: ").split()
original_dict = {(" ".join(sym)).lower() : count for word in text for sym in word}

for letter in original_dict:
    for word_text in text:
        for letter_word in word_text:
            if letter == letter_word:
                original_dict[letter] = original_dict[letter] + 1
print(f"Оригинальный словарь частот: {original_dict}")

invert_dict = {num_count: "" for num_count in original_dict.values()}

for sym_i in invert_dict:
    print(sym_i, " <-- Sym_I")
    for sym_o in original_dict:
        print(sym_o, " <-- Sym_0")
        if original_dict[sym_o] == sym_i:
            invert_dict[sym_i] += sym_o
            print(f"найдено совпадение {invert_dict}")


print(f"Инвертированный словарь частот: {invert_dict}")



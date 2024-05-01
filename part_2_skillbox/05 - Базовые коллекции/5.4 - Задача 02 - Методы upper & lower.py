word_list = []

for i_num in range(3):
    print(f"Введите {i_num + 1} слово: ", end="")
    word = input().lower()
    word_list.append(word)

text = input("Слово из текста: ").lower().split()


print(f"\nПодсчет слов в тексте: ")
for index in range(3):
    print(f"{word_list[index]} : {text.count(word_list[index])}")

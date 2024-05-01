word_list = [["", 0], ["", 0], ["", 0]]

for i_num in range(3):
    print(f"Введите {i_num + 1} слово: ", end="")
    word = input()
    word_list[i_num][0] = word

text = input("Слово из текста: ")
while text != "":
    for index in range(3):
        if word_list[index][0] == text:
            word_list[index][1] += 1
    text = input("Слово из текста: ")

print(f"\nПодсчет слов в тексте: ")
for index in range(3):
    print(f"{word_list[index][0]} : {word_list[index][1]}")
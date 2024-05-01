word_list = []
counts = [0, 0, 0]

for i in range(3):
    print(f"Введите {i +1} слово: ", end=" ")
    word = input("")
    word_list.append(word)

text = input("Слово из текста: ")
while text != "end":
    for index in range(3):
        if word_list[index] == text:
            counts[index] += 1
    text = input("Слово из текста: ")

print(f"\nПодсчет слов в тексте")
for i in range(3):
    print(word_list[i], ":", counts[i])
speakers_file = open('speakers.txt', 'r', encoding='utf-8')
data = speakers_file.read(14)
speakers_file.seek(0)
data_2 = speakers_file.read(22)

speakers_file.close()
print(data)
print(data_2)
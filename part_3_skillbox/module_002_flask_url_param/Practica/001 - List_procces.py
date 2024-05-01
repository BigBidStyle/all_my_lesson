import os

# Можно использовать  библиотеку.
# from humanize import naturalsize
# print(naturalsize(1536))  # "1.5 КБ"
# print(naturalsize(1048576, binary=True))  # "1.0 МиБ"

# Можно воспользоваться таким способом.
def human_size(size):
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def get_summary_rss():
    file_name = "output_file.txt"  # <-- Название файла.
    os.system(f'ps aux > {file_name}')   # <-- Запускаем эту команду и сохраняем выданный результат в файл.
    file_path = os.path.abspath(file_name)  # <-- Путь к файлу.

    total_size = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]    # Удаляем строку с заголовками.
        for i_line in lines:
            list_line = i_line.split()
            total_size += int(list_line[5])

        print(f'{total_size} Б -> {human_size(total_size)}')

if __name__ == "__main__":
    get_summary_rss()
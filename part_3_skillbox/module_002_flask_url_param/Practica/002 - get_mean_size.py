import sys
from humanize import naturalsize    # <- Модуль преобразовывает размер файла в человеческий формат.

def get_mean_size(ls_input: list) -> str:
    """Функция рассчитывает средней размер файла в рабочий директории"""
    total_sum = 0
    count_line = 0
    for i_line in ls_input:
        count_line += 1
        list_line = i_line.split()
        total_sum += int(list_line()[4])
    return naturalsize(total_sum / count_line)

if __name__ == "__main__":
    data = sys.stdin.readlines()[1:]    # <-- Получаем входные данные в виде списка строк
    if not data:
        print('Данная директория пуста')
    else:

        mean_size = get_mean_size(data)
        print(f'Средний размер файлов в рабочей директории: {mean_size}')


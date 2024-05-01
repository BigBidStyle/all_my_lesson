cnt: int    # <-- Элемент аннотации типов.
cnt = -5.13 # <-- Появилась подсказка, что cnt должен быть целым числом.
# можно записать и так...
cnt_1: int = 0
# --------------------------- #
from typing import Union, Optional, Any, Final, Callable
# Union <-- Объединение нескольких типов в один. Union[int, float]
# Optional <-- Позволяет указать один тип данных + None.
# Any <-- Любой тип данных.
# Final <-- Служит для отметки констант.
# Callable <-- Используется для аннотации вызываемый объектов.

# Union ------------------------------------------ #
# Можно прописать так...
# def mul2(x: Union[int, float], y: Union[int, float] = 2) -> Union[int, float]:
#     return  x * y

# Можно прописать так...
def mul2(x: int | float, y:int | float = 2) -> int | float:
    return  x * y

# # Можно прописать так...
# Digit = Union[int, float]
# def mul2(x: Digit, y: Digit = 2) -> Digit:
#     return  x * y

res = mul2(5.2, 4)
print(res)
print(mul2.__annotations__)
print("-" * 40)

# Optional ------------------------------------------ #
def show_x(x: Any, descr: Optional[str] = None) -> None:
    if descr:
        print(f'{descr}{x}')
    else:
        print(f'x = {x}')
show_x(55.444, 'x : ')
print("-" * 40)

# Final  ------------------------------------------ #
MAX_VALUE: Final = 1000 # <-- Предполагается что эта переменная будет константой.т.е если мы попытаемся ее изменить,
# то python будет предупреждать нас об этом...
MAX_VALUE = 2000 # Ругается...

# list  ------------------------------------------ #
lst: list[int] = [1, 2, 3]

# tuple  ------------------------------------------ #
addr: tuple[int, str] = (1, 'qwer')
book: tuple[str, str, int]
book = ("Изучение Python", 'Water-Wave', 2024)
elems: tuple[float, ...]
elems = (1.0,)
elems = (1.0, 2.0)

# dict  ------------------------------------------ #
word: dict[str, int] = {'one':1, 'two':2}

persons: set[str]= {'qwer', 'asdf', 'zxcv'}

# Callable --------------------------------------- #

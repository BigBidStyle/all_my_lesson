from typing import Union, Optional, Any, Final,Callable

def get_positive(digits: list[int | float]) -> list[Union[int, float]]:
    return list(filter(lambda x: x > 0, digits))
print(get_positive([1, -2, 3, 4, -5, 2.2]))
print("-" * 40)
# --------------------------------------------------------------------------- #
def get_digits(flt: Callable[[int], bool], lst: list[int] = None) -> list[int]:
    if lst is None:
        return []
    return list(filter(flt, lst))

def even(x: int):
    return  bool(x % 2 == 0)

print(get_digits(even, [1, 2, 3, 4, 5, 6, 7]))



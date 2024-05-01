from typing import Any, Type, TypeVar
from __future__ import annotations
class Geom: pass
class Point2D(Geom):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def copy(self) -> Point2D:
        return Point2D(self.x, self.y)


p = Point2D(10, 20)



# T = TypeVar('T', bound=Geom)
#
# def factory_object(cls_obj: Type[T]) -> T:
#     return cls_obj()
#
# geom: Geom = factory_object(Geom)
# point: Point2D = factory_object(Point2D)


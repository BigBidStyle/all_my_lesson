class Geom: pass
class Line(Geom): pass

print(Geom.__name__)
g = Geom()
l = Line()

print(l.__class__)
print(issubclass(Line, Geom)) # = True Работает только с классами.
print(issubclass(Geom, Line)) # = False Работает только с классами.
print(isinstance(l, Geom)) # = True Работает с экземплярами и классами.
# ----------------------------------- #
class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))

v = Vector([1, 2, 3,])
print(v) # 1 2 3



from math import sqrt
from pprint import pformat


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return pformat({"x": self.x, "y": self.y})

    def __str__(self) -> str:
        return f"{[self.x, self.y]}"  # stringified array containing x and y

    def __eq__(self, __other: object) -> bool:
        if type(__other) != type(self):
            raise TypeError(f"Vector2 may not be compared with {repr(type(__other))}")
        else:
            return self.x == __other.x and self.y == __other.y

    def __add__(self, __other):
        if type(__other) != type(self):
            raise TypeError(f"Vector2 may not be added with {repr(type(__other))}")
        else:
            return Vector2(self.x + __other.x, self.y + __other.y)

    def __sub__(self, __other):
        if type(__other) != type(self):
            raise TypeError(f"Vector2 may not be added with {repr(type(__other))}")
        else:
            return Vector2(self.x - __other.x, self.y - __other.y)

    def __mul__(self, __multiplier: float):
        # Multiplier can be either float or int
        if type(__multiplier) != type(0.1) and type(__multiplier) != type(1):
            raise TypeError(
                f"Vector2 may not be multiplied with {repr(type(__multiplier))}"
            )
        else:
            return Vector2(self.x * __multiplier, self.y * __multiplier)

    def getNormalized(vector) -> float:
        # magnitude is equal to hypotenuse so use a**2 + b **2 = c**2
        magnitude: float = sqrt(vector.x ** 2 + vector.y ** 2)
        return Vector2(vector.x / magnitude, vector.y / magnitude)

    def __iter__(self) -> list[float, float]:
        return iter([self.x, self.y])


Vector2.up = Vector2(0, 1)
Vector2.down = Vector2(0, -1)
Vector2.right = Vector2(1, 0)
Vector2.left = Vector2(-1, 0)

from abc import ABC, abstractmethod
from typing import Union


class Shape(ABC):
    @abstractmethod
    def area(self) -> Union[float, int]:
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def __str__(self):
        return f"Square with length: {self.length}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self) -> str:
        return f"Rectangle with length {self.length} and width {self.width}"


sq1 = Square(10)
print(f"{sq1}: {sq1.area()}")

sq2 = Square(200)
print(f"{sq2}: {sq2.area()}")

rc1 = Rectangle(10, 15)
print(f"{rc1}: {rc1.area()}")

rc2 = Rectangle(120, 500)
print(f"{rc2}: {rc2.area()}")
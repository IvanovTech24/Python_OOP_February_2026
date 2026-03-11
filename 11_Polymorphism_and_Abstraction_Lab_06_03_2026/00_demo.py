class Shape:
    def calculate_area(self):
        return None

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * 2

class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def calculate_area(self):
        return 0.5 * self.length * self.height

shapes = [Triangle(3, 7), Square(5), Square(3), Triangle(2, 9)]
for shape in shapes:
    print(shape.calculate_area())


# Abstraction
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("name must be at least 2 characters")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("age must be positive")
        self.__age = value
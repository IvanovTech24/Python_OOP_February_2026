# Static Methods
class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18


print(Person.is_adult(5)) # False
girl = Person("Amy")
print(girl.is_adult(20)) # True

# Class Methods
class Pizza:
    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @classmethod
    def pepperoni(cls):
        return cls("Pepperoni",["tomato sauce", "parmesan", "pepperoni"])

    @classmethod
    def quattro_formaggi(cls):
        return cls("Quattro Formaggi", ["mozzarella", "gorgonzola", "fontina", "parmigiano"])

    def __str__(self):
        return f"You ordered pizza {self.name}"


first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi()
print(first_pizza)
print(second_pizza)

my_pizza = Pizza("My Pizza", ["tomato sauce", "prosciutto"])
print(my_pizza)

# Overriding Using Class Methods
class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def __validate_age(cls, value):
        if value < cls.min_age or \
            value > cls.max_age:
            raise ValueError()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value



class Employee(Person):
    min_age = 16
    max_age = 150


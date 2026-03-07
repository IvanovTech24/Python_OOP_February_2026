class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._test_protected = "test protected"
        self.__test_private = "test private"

    def __str__(self):
        return f"I am a person with name {self.name} and age {self.age}"

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

class Teacher(Person):
    def __init__(self, name, age, teaching_hours):
        super().__init__(name, age)
        self.teaching_hours = teaching_hours

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

class Car:
    def __init__(self):
        self.__max_speed = 200

    def drive(self):
        print('driving max speed ' + str(self.__max_speed))


class Card:
    def __init__(self, number, exp_date, cvv, password):
        self.number = number
        self.exp_date = exp_date
        self.__cvv = cvv
        self.__password = password

    def get_cvv(self, password):
        if password == self.__password:
            return self.__cvv
        raise Exception("Invalid password")


class Persons:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name)
        print(self.__age)

    def get_age(self): # getter
        return self.__age

    def set_age(self, age): # setter
        if not isinstance(age, int):
            raise Exception("age must be an integer")
        if age < 0 or age > 100:
            raise Exception("age must be between 0 and 100")
        self.__age = age

# Getter and Setter
class Person2:
    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
        else:
            self.__age = age


# Name Mangling a Method
class Person3:
    def __init__(self):
        self.first_name = 'Peter'
        self.last_name = 'Parker'

    def __full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return self.__full_name()

# Built-In Functions for Accessing Attributes

class Person4:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        return None

person = Person('Peter')
print(getattr(person, 'name')) # True
print(getattr(person, 'age')) # AttributeError
print(getattr(person, 'age', None)) # None


class Person5:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(hasattr(person, 'name')) # True
print(hasattr(person, 'age')) # False


class Person6:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(setattr(person, 'name', 'George')) # None
print(person.name) # George
print(setattr(person, 'age', 21)) # None
print(person.age) # 21


class Person7:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(person.name) # Peter
print(delattr(person, 'name')) # None
print(person.name) # AttributeError


class Employee:
    name = 'Diyan'
    salary = '25000'

    def show(self):
        print(self.name)
        print(self.salary)

employee = Employee()
print(getattr(employee, 'name')) # Diyan
print(hasattr(employee, 'name')) # True
setattr(employee, 'height', 152)
print(getattr(employee, 'height')) # 152
delattr(Employee, 'salary')


p = Person("Ivan", 25)
print(p.name)
print(p.age)


red_car = Car()
red_car.drive() # driving max speed 200
red_car.__max_speed = 10 # won't change because it is name mangled
red_car.drive() # driving max speed 200


person = Persons("Simeon", 13)
person.set_age("sdf")

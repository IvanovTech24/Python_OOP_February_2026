from abc import ABC, abstractmethod

# make abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "woof-woof"

class Cat(Animal):
    def make_sound(self):
        return "meow"

class Pig(Animal):
    def make_sound(self):
        return "gruh"

class Turtle(Animal):
    def make_sound(self):
        return "turtle sound"

#refact method
def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Pig(), Turtle()]
animal_sound(animals)

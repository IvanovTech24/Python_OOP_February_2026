class Dog:
    def __init__(self, name: str):
        self.name = name

    def change_name(self, new_name: str) -> None:
        self.name = new_name

    def __str__(self):
        return f"I am a dog with name {self.name}"

class Person:
    kind = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Example:
    text = "Hello"

    def __init__(self, name):
        self.name = name

    def print_text(self):
        return "SoftUni"

example1 = Example("Test1")
example2 = Example("Test2")
# print(example1.name)
# print(example2.name)
# print(example1.text) # Accessing a class attribute through the instance.
# print(example2.text) # Accessing a class attribute through the instance.
#
# example1.text = "changed" # Changing the class attribute through the instance, it remains changed,
# print(example1.text)      # only for the current instance.
# print(example2.text)
#
# Example.text = "changed" # Changing the class attribute through the class, it changes for all instances
# print(example1.text)
# print(example2.text)
# print(Example.text)

puppy = Dog("Max")
print(puppy)
puppy.change_name("Rex")
print(puppy.name)
print(puppy)
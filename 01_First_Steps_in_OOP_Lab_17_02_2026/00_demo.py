# ------------------------------ Scopes --------------------------------
# x = 1 # Global Scope
#
# def some_func(): # Local Scope
#     x = 2
#
#     def nested_func(): # Enclosing Scope
#         # global x -> change variable x in Global Scope
#         # nonlocal x -> change variable x in Local Scope
#         x = 3
#         print(x)
#
#     nested_func()
#     print(x)
#
# print(x) # Built-In Scope
#
# some_func()
#
# print(x)

# ------------------------ Class ----------------------------------
# class Phone:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size
#
#     def turn_on(self):
#          return "The phone is turned on"

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sleep(self):
#         return "sleeping"
#
# animal = Animal("cat")
# print(animal.sleep())

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def eat(self):
        return "eating.."

person = Person("Ivan", 22)
print(person.eat())
# Single Inheritance
class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, faculty_number):
        super().__init__(first_name, last_name)
        self.faculty_number = faculty_number

    def get_full_name(self):
        result = super().get_full_name() + " " + str(self.faculty_number)
        return result

    def present_faculty_info(self):
        return f"I am a student with faculty number {self.faculty_number}"

# Multilevel Inheritance
class Parent:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age

class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def get_address(self):
        return self.address

# Hierarchical Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f"Hi! I am {self.name}"

class Daughter(Parent):
    def __init__(self, name):
        super().__init__(name)
        self.test = "test"

    def relation(self):
        return "I am my parent's daughter"

class Son(Parent):
    def __init__(self, name):
        super().__init__(name)
        self.something = "something"

    def relation(self):
        return "I am my parent's son"

person1 = Person("Ivan", "Ivanov")
print(person1.first_name)
print(person1.last_name)
print(person1.get_full_name())

student1 = Student("Petar", "Petrov", 2)
print(student1.first_name)
print(student1.last_name)
print(student1.get_full_name())
print(student1.present_faculty_info())

grand_child = GrandChild("Grand Name", 19, "Address 15-17")
print(grand_child.name)
print(grand_child.age)
print(grand_child.address)

print(grand_child.get_address())
print(grand_child.get_age())
print(grand_child.get_name())

d = Daughter("Daughter")
s = Son("Son")

print(d.name)
print(s.name)

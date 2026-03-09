class MyClass:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def my_class_method(cls):
        return cls("Test Name")

    @staticmethod
    def my_static_method():
        return "Some text"

my = MyClass("Ivan")
my_class_method = MyClass.my_class_method()
print(my)
print(my_class_method)
print(my.my_static_method())
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value


p = Person("Pesho")
print(p.name) 
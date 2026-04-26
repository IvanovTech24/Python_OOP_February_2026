from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair("Victorian chair")

    def create_sofa(self):
        return Sofa("Victorian sofa")

    def create_table(self):
        return Table("Victorian table")


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair("Modern chair")

    def create_sofa(self):
        return Sofa("Modern sofa")

    def create_table(self):
        return Table("Modern table")


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair("Futuristic chair")

    def create_sofa(self):
        return Sofa("Futuristic sofa")

    def create_table(self):
        return Table("Futuristic table")


victorian_factory = VictorianFactory()
moder_factory = ModernFactory()


my_chair = victorian_factory.create_chair()
my_sofa = victorian_factory.create_sofa()
my_table = victorian_factory.create_table()

daughter_table = moder_factory.create_table()
daughter_chair = moder_factory.create_chair()

print(my_chair)
print(my_sofa)
print(my_table)
print("====================================")
print(daughter_table)
print(daughter_chair)
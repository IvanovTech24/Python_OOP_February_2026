from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Graphic):
    def draw(self):
        print("Drawing circle")


class Square(Graphic):
    def draw(self):
        print("Drawing square")


class CompositeGraphic(Graphic):
    def __init__(self):
        self._children: list[Graphic] = []

    def add(self, graphic: Graphic):
        self._children.append(graphic)

    def remove(self, graphic: Graphic):
        self._children.remove(graphic)

    def draw(self):
        for child in self._children:
            child.draw()


c1 = Circle()
c2 = Circle()
s = Square()

composite = CompositeGraphic()
composite.add(c1)
composite.add(c2)
composite.add(s)

composite.draw()
print("=========================")
composite.remove(c1)
composite.draw()
class A:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        return "This is class A"

class B(A):

    def do_something(self):
        return "This is class B"

class C(A):

    def do_something(self):
        return "This is class C"

class D(B, C):
    pass

d = D("D")
print(d.do_something())
print(D.mro())
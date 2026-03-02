class Worker:
    """
    Worker class documentation
    """
    salary = 1500

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 2000

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.salary}"

    def __repr__(self):
        # tell the id that this is a repr so it puts quotes
        return f"Worker ({self.first_name!r}, {repr(self.last_name)})"

    def change_salary(self):
        Worker.salary += 500

w1 = Worker("Petar", "Petrov")
w2 = Worker("Ivan", "Ivanov")

print(w1.salary)
print(w2.salary)

Worker.salary = 2000

print(w1.salary)
print(w2.salary)

w1.salary = 2500

print(w1.salary)
print(w2.salary)
print(Worker.salary)

print(w1.__dict__)
print(w2.__dict__)

print(w2.__doc__)

print(str(w1))
print(w1.__str__())
print(w1)

print(w1.__repr__())
print(repr(w1))

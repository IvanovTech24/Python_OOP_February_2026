# Iterator
class MyIterator:
    def __init__(self, my_iterable):
        self.my_iterable = my_iterable
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.my_iterable):
            self.counter += 1
            return self.my_iterable[self.counter - 1]
        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for el in my_iterator:
    print(el)


# Generator
def my_generator(my_iterable):
    for element in my_iterable:
        yield element ** 2

my_gen = my_generator(my_list)

for i in my_gen:
    print(i, end=", ")

# Generators
def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


result = first_n(5)
for el in result:
    print(el)




def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


solution = my_gen()
for el in solution:
    print(el)
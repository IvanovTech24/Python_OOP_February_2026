def genrange(start: float, end: float):
    while start <= end:
        yield start
        start += 1


for el in genrange(1, 10):
    print(el)


print(list(genrange(1, 10)))
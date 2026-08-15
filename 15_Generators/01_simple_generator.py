def numbers():

    yield 10
    yield 20
    yield 30

generators = numbers()

print(next(generators))
print(next(generators))
print(next(generators))
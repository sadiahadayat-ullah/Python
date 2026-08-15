def fibonacci(limit):

    first = 0
    second = 1

    for _ in range(limit):
        yield first
        first, second = second, first + second

for number in fibonacci(10):
    print(number)
        
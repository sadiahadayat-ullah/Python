class Number:

    def __init__(self, limit):
        self.counter = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.limit:
           value = self.counter
           self.counter += 1
           return value
        raise StopIteration

counter = Number(5)

for number in counter:
    print(number)
# Program: __next__() Dunder Method
# Description: Demonstrates how __next__() controls the next value
# produced by a custom iterator.

class Counter:

    def __init__(self, limit):
        self.counter = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter <= self.limit:
            return self.counter
        else:
            raise StopIteration

counter = Counter(3)

print(next(counter))
print(next(counter))
print(next(counter))

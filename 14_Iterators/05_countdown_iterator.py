class Countdown:

    def __init__(self, limit):
        self.counter = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= 1:
            value = self.counter
            self.counter -= 1
            return value
        raise StopIteration

countdown = Countdown(5)

for number in countdown:
    print(number)
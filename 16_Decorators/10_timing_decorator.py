import time

def timer(function):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print("Execution time", end - start, "seconds.")
        return result
    return wrapper

@timer
def calculate():
    total = 0

    for i in range(100000):
        total += i
    return total

result = calculate()
print(result)
def decorator(function):

    def wrapper(*args, **kwargs):
        print("Starting...")
        result = function(*args, **kwargs)
        print("Ending...")
        return result
    return wrapper

@decorator
def add(a, b):
    return a+b

result = add(10, 5)
print(result)
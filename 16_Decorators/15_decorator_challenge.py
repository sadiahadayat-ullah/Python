def validate_positive(function):

    def wrapper(*args, **kwargs):
        if  all(value > 0 for value in args):
            return function(*args, **kwargs)
        else:
            print("Arguments must be positive.")
    return wrapper

@validate_positive
def multiply(a, b):
    return a*b

print(multiply(5, 3))
print(multiply(-5, 3))
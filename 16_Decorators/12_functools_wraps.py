from functools import wraps

def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

@decorator
def greet():
    '''Greets the user.'''
    print("Hello Python")

print(greet.__name__)
print(greet.__doc__)
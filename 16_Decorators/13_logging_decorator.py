from functools import wraps

def log_call(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Calling function:", function.__name__)
        return function(*args, **kwargs)
    return wrapper
    

@log_call
def greet():
    print("Hello Python")

greet()
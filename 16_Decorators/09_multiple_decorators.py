def first_decorator(function):

    def wrapper():
        print("First before")
        function()
        print("First after")
    return wrapper

def second_decorator(function):

    def wrapper():
        print("Second before")
        function()
        print("Second after")
    return wrapper

@first_decorator
@second_decorator
def greet():
    print("Hello Python")

greet()
def decorator(function):

    def wrapper():
        print("Starting...")
        function()
        print("Ending...")
    return wrapper

@decorator
def greet():
    print("Hello Python")

greet()
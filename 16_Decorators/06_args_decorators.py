def decorator(function):

    def wrapper(*args):
        print("Starting...")
        function(*args)
        print("Ending...")
    return wrapper

@decorator
def greet(name):
    print(f"Hello {name}")

greet("Ali")
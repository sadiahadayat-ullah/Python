def decorator(function):

    def wrapper(*args, **kwargs):
        print("Starting...")
        function(*args, **kwargs)
        print("Ending...")
    return wrapper

@decorator
def student(name, age):
    print(f"My name is {name} and age is {age}.")

student(name="Ali", age=17)
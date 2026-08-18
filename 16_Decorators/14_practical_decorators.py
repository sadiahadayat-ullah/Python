def double_result(function):

    def wrapper(*args, **kwargs):
        print("Starting...")
        result = function(*args, **kwargs)
        print("Ending...")
        return result * 2
    return wrapper

@double_result
def add(a, b):
    return a+b

result = add(10, 5)
print(result)
def add(a, b):
    return a+b

def calculate(function, a, b):
    return function(a, b)

result = calculate(add, 10, 5)
print(result)
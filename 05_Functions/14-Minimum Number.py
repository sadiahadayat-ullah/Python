# Using if-else
def min(a,b):
    if a < b:
        return a
    else:
        return b
result = min(10,5)
print(result)
# Using Lambda Function
minimum = lambda a,b: min(a,b)
print(minimum(10,5))
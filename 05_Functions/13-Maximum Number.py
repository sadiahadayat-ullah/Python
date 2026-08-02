# Using if-else
def max(a,b):
    if a>b:
        return a
    else:
        return b
result = max(10,5)
print(result)
# Using Lambda Function
maximum = lambda a,b: max(a,b)
print(maximum(10,5))
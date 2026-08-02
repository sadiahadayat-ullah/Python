# Using if-elif-else
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(largest(10,5,3))
# Using return()
def largest(a,b,c):
    return max(a,b,c)
print(largest(10,5,3))
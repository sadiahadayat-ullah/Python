# Using if-elif-else
def smallest(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
print(smallest(10,5,3))
# Using return()
def smallest(a,b,c):
    return min(a,b,c)
print(smallest(10,5,3))
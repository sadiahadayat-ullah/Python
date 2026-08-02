terms = int(input("Enter the number of terms:"))
a = 0
b = 1
for i in range(terms):
    print(a)
    c = a + b
    a = b
    b = c

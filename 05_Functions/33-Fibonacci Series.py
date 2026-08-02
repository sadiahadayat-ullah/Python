def terms(num):
    a = 0
    b = 1
    for i in range(num):
        print(a)
        c = a+b
        a = b
        b = c
number = int(input("Enter a number: "))
terms(number)
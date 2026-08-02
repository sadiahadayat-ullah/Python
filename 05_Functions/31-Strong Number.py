def strong(n):
    total = 0
    temp = n
    length = len(str(n))
    for i in range(length):
        digit = temp % 10
        fact = 1
        for j in range(1,digit+1):
            fact *= j
        total += fact
        temp = temp // 10
    return total
number = int(input("Enter a number: "))
strong_number = strong(number)
if strong_number == number:
    print("Strong Number")
else:
    print("Not a Strong Number")
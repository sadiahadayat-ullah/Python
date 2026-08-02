numbers = [10,13,17,25,43,67]
print("Original list:",numbers)
prime_numbers = []
for number in numbers:
    if number < 2:
        continue
    prime = True
    for i in range (2,number):
        if number % i == 0:
            prime = False
            break
    if prime:
        prime_numbers.append(number)
print("Prime number:",prime_numbers)
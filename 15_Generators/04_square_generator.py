def square(limit):

    number = 1
    while number <= limit:
       yield number ** 2
       number += 1

for number in square(5):
    print(number)


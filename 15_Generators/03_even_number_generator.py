def even_numbers(limit):

    number = 2
    while number <= limit:
        if number % 2 == 0:
            yield number
        number += 1

for number in even_numbers(10):
    print(number)
def count_upto(limit):

    number = 1
    while number <= limit:
        yield number
        number += 1

for number in count_upto(5):
    print(number)
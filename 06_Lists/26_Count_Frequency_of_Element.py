numbers = [10,20,10,30,20,10]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
for number in unique_numbers:
    count = 0
    for item in numbers:
        if item == number:
            count += 1
    print(number,"appear",count,"times")

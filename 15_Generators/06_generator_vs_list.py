square_list = [number ** 2 for number in range(1,6)]

for number in square_list:
    print(number)

square_generator = (number ** 2 for number in range(1,6))

for number in square_generator:
    print("Generator:", number)
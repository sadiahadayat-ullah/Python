import random
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
random_number = random.randint(start, end)
print(f"Random number between {start} and {end} is {random_number}")
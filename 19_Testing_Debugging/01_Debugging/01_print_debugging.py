def calculate_total(price, quantity):
    total = price * quantity    

    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)

    return total

result = calculate_total(10, 3)
print(result)
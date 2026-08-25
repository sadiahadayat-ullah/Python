# 1. Syntax Error
# Python can't understand the code because the colon is missing.
# if 10 > 5
#     print("Yes")

# 2. Runtime Error
# The code is syntaically correct, but an error occurs while running.
try:
    number = 10/0
except ZeroDivisionError:
    print("Runtime Error: Can't divide by zero.")

# 3. Logical Error
# The program runs successfully, but the result is incorrect.
def calculate_total(price, quantity):
    # Logical mistake: price * quantity
    return price + quantity

result = calculate_total(100, 3)

print("Logical Error Example:")
print("Expected:", 300)
print("Actual:", result)
# Program: Safe calculator
# Description: Performs basic arithmetic operations using exception handling

try:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    print("Addition: ", num1 + num2)
    print("Subtraction: ", num1 - num2)
    print("Multiplication: ", num1 * num2)
    print("Division: ", num1 / num2)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("\nCalculation completed successfully")
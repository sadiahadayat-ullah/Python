# Program: List Index Checker
# Description: Check the index in list using exception handling

try:
    numbers = [10,20,30,40,50]
    index = int(input("Enter index: "))
    print("Element:",numbers[index])

except IndexError as e:
     print("Invalid index")

except ValueError:
    print("Please enter a valid number")

finally:
    print("Program ended")

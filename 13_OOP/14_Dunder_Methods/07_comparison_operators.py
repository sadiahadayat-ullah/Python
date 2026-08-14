# Program: Comparison Operator Overloading
# Description: Demonstrates how comparison dunder methods define the
# behavior of comparison operators for custom objects.

class Number:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

num1 = Number(10)
num2 = Number(5)

print("Less than: ", num1 < num2)
print("Greater than: ", num1 > num2)
print("Less than or equal: ", num1 <= num2)
print("Greater than or equal: ", num1 >= num2)

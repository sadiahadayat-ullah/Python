# Program: __iter__() Dunder Method
# Description: Demonstrates how __iter__() makes a custom object
# iterable and allows it to be used in a for loop.

class Team:

    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return iter(self.members)

team = Team(["Ali", "Sara", "Ahmed"])

for member in team:
    print(member)

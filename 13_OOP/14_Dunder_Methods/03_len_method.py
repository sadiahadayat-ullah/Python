# Program: __len__() Dunder Method
# Description: Demonstrates how __len__() allows the len() function
# to determine the length of a custom object.

class Team:

    def __init__(self,members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Ali", "Babar", "Rizwan", "Shadab"])
team_length = len(team)
print(team_length)



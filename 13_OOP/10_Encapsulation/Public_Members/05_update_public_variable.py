# Program: Update Public Variable
# Description: Demonstrates how to modify a public variable after creating an object.

class Mobile:

    def __init__(self,company):
        self.company = company

company_name = input("Enter company name: ")

mobile = Mobile(company_name)
print("Original Company:", mobile.company)

mobile.company = "Apple"
print("Updated Company:", mobile.company)

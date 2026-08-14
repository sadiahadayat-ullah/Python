# Program: Update Protected Variable
# Description: Demonstrates how to modify a protected variable after creating an object.

class Mobile:

    def __init__(self,company):
        self._company = company

company_name = input("Enter company name: ")
company = Mobile(company_name)
print("Original Company:",company._company)

company._company = "Apple"
print("Updated Company:",company._company)
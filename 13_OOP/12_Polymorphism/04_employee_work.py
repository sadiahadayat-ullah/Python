# Program: Employee Work using Polymorphism

# Description: Demonstrates polymorphism by using the same work()
# method in different classes with different behaviors.

class Developer:

    def work(self):
        print("Developer writes code")

class Designer:

    def work(self):
        print("Designer creates design")

class Tester:

    def work(self):
        print("Tester tests software")

def do_work(employee):
    employee.work()

do_work(Developer())
do_work(Designer())
do_work(Tester())
# Program: Hybrid Method Resolution Order (MRO)
# Description: Demonstrates how Python determines the method resolution order in hybrid inheritance.

class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("B")
        super().show()

class C(A):

    def show(self):
        print("C")
        super().show()

class D(B, C):

    def show(self):
        print("D")
        super().show()

d = D()
d.show()

print(D.mro())
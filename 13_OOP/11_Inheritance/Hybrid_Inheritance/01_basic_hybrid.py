# Program: Basic Hybrid Inheritance
# Description: Demonstrates hybrid inheritance by combining hierarchical and multiple inheritance.

class A:

    def show_a(self):
        print("Class A")

class B(A):

    def show_b(self):
        print("Class B")

class C(A):

    def show_c(self):
        print("Class C")

class D(B, C):

    def show_d(self):
        print("Class D")

d = D()
d.show_b()
d.show_c()
d.show_d()
d.show_a()
# Program: Hierarchical Constructors
# Description: Demonstrates constructors, super(), and child-specific attributes in hierarchical inheritance.

class Animal:

    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Animal:", self.name)

class Dog(Animal):

    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
    def display_dog(self):
        print("Dog:", self.breed)

class Cat(Animal):

    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    def display_cat(self):
        print("Cat:", self.color)

dog = Dog("Tommy", "Labrador")
dog.display_name()
dog.display_dog()

cat = Cat("Kitty", "White")
cat.display_name()
cat.display_cat()

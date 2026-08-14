# Program: Basic Polymorphism

# Description: Demonstrates polymorphism by using the same method
# sound() in different classes with different behaviors.

class Dog:

    def sound(self):
        print("Dog barks")

class Cat:

    def sound(self):
        print("Cat meows")

class Cow:

    def sound(self):
        print("Cow moos")

dog = Dog()
cat = Cat()
cow = Cow()

for animal in [dog, cat, cow]:
    animal.sound()
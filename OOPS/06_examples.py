# Create class Car() with a method drive() that prints "Car is moving".Create obj of car and call drive.

class Car:
    def drive(self):
        print("Car is moving")

c = Car()
c.drive()


# Create a class Person with a constructor ( __init__ ) that accepts name and age as arguments and stores them as instance attributes. Create an object and print the person’s name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Ronak", 22)
print(p.name, p.age)


# Create a base class Animal with a method sound() that prints "Some sound". Create a derived class Dog that overrides sound() to print "Bark!". Create an object of Dog and call sound().

class Animal:
    def sound(self):
        print("Some Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
a.sound()
d = Dog()
d.sound()
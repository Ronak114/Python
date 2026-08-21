class Animal:  # Parent class (superclass)
    location = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now....")


class Dog(Animal):  # inheritance
    def speak(self):
        super().speak()  # to call parent class
        print("Woof!")


a = Animal("Dog")
a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)

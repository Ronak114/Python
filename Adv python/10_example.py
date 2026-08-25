# Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function "Hello!" .

def logger(func):
    def wrapper():
        print("Function is being called")
        return func()

    return wrapper

@logger
def say_hello():
    print("Hello!")

say_hello()


# 2. Write a decorator timer that calculates how long a function takes to execute.Test it with a function that sums numbers from 1 to 1,000,000.

from time import time

def timer(func):
    def wrapper():
        t1 = time()
        print(func())
        t2 = time()
        print(t2 - t1)
        return func()

    return wrapper

@timer
def sum():
    total = 0
    for i in range(1000001):
        total += i
    return total

sum()


# 3.Create a class Employee with a private attribute _salary. Use @property to define a getter for salary. Use @salary.setter to prevent setting negative values (print a warning instead). Create an object and test by setting positive and negative salaries.

class Employee:
    def __init__(self, salary):
        self.s = salary

    @property
    def get_salary(self):
        return self.s

    @get_salary.setter
    def set_salary(self, val):
        if val < 0:
            print("Not possible")
        else:
            self.s = val

e = Employee(3500000)
print(e.get_salary)
e.set_salary = -4000000
print(e.get_salary)


""" Static & Class Methods
4. Create a class MathUtils with:
    1.@staticmethod called add(a, b) that returns a + b.
    2.@classmethod called description(cls) that prints "This is a utility class for math operations."
4.1. Call both methods without creating an object."""

class MathUtlis:

    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")

a = MathUtlis()
print(a.add(4, 6))
a.description()

print(MathUtlis.add(55, 6))
MathUtlis.description()


"""
5.Create a class Book with attributes title and author.
Implement __str__() so that printing the object displays "Title by Author" .
Implement __len__() so that len(book) returns the length of the title.
5.2. Create two Book objects and test these methods."""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

b1 = Book("It Ends with Us", "Coollen hoover")
b2 = Book("Verity", "Coollen hoover")

print(b1.__str__())
print(b2.__len__())


'''Exception Handling and Custom Errors
6.Write a program that asks the user to enter a number and handles:
    1. ValueError if the input is not a number
    2. ZeroDivisionError if you try to divide by zero
6.2. Create a custom exception NegativeNumberError and raise it when the user enters a negative number.'''

class NegativeNoError(Exception):
    pass 

while True:
    try:
        a=int(input("Enter no 1: "))
        b=int(input("Enter no 2: "))

        if a<0 or b<0:
            raise NegativeNoError("No should be positive")
        
        print(a/b)

    except ValueError:
        print("Plz enter no")

    except ZeroDivisionError:
        print("2nd no should not be 0")

    except NegativeNoError:
        print("Dont enter negative no")


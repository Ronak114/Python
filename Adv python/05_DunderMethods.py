# Dunder - double score methods


class Employee:
    company = "HP"  # class attribute.

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # for users
    def __str__(self):
        return f"Name is {self.name} and salary is {self.salary}"

    # for developer
    def __repr__(self):
        return f"Name:{self.name} and salary:{self.salary}"

    def __len__(self):
        return len(self.name)


e = Employee("Ronak", 3500000)
print(e.name, e.salary)
print(str(e))
print(repr(e))
print(len(e))

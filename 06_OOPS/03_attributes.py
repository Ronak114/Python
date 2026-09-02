# Attributes:
# - Class Attribute
# - Instance Attribute

class Employee:
    company = "Asus"  # This is class attribute

    def __init__(self, company):
        self.company = company

e = Employee("Tesla")
print(e.company)  # always print instance attribute whenever present
print(Employee.company)  # always print the class attribute

# Object introspection
print(dir(e))

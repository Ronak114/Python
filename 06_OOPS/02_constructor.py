# constructor:

class Employee:

    def __init__(self, salary, name, bond): # __init__ -> by default creates constructor
        self.salary = salary  # Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(
            f"The name of the employee is {self.name}. Salary is {self.salary} and the bond is for {self.bond} years"
        )


e = Employee(300000, "Mira", 1)
print(e.get_salary())
e.get_info()

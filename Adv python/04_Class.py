class Employee:
    company = "HP" # class attribute.

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Even this will work as 3rd parameter = self.
    # def sum(self,a, b):
    #     return a + b

    # Static Method - dont req self
    @staticmethod
    def sum(a, b):
        return a + b

    # Class Methods
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Ronak", 350000000)
e2 = Employee("ABC", 34355)
print(Employee.company)
# print(Employee.name) # this will throw an error
e1.print_info()
e2.print_info()

print(e2.sum(5, 23))
print(e1.sum(5, 23))

print(Employee.company)
e1.change_company("Acer")
print(Employee.company)

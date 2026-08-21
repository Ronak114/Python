# Class: Class is a blueprint or a template. Ex: car
# Object: Specific instance created from the template (class.). EX:Audi

class Employee:
    company = "Google"

    def get_salary(self): # self -  self-reference the object of the class which is being created
        return 34000


e = Employee()  # An Object of class Employee is created
print(e.get_salary())  # Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)
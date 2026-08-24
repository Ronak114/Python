# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     # fun to display first name.
#     def first_name(self):
#         l = self.name.split(" ")
#         return l[0]

#     # function to set first name.
#     def set_first_name(self, Newfirst):
#         l = self.name.split(" ")
#         new_name = f"{Newfirst} {l[1]}"
#         self.name = new_name


# e = Employee("Ronak Pawar", 3500000)
# print(e.first_name())
# e.set_first_name("Rahi")
# print(e.name)

# # print(e.first_name)
# # e.first_name = "John"
# # print(e.name)


# ANOTHER WAY
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    # function to set first name
    @first_name.setter
    def set_first_name(self, Newfirst):
        l = self.name.split(" ")
        new_name = f"{Newfirst} {l[1]}"
        self.name = new_name


e = Employee("Ronak Pawar", 3500000)
# print(e.first_name())
# e.set_first_name("Rahi")
# print(e.name)

print(e.first_name)
e.set_first_name = "Rahi"
print(e.name)
# BASIC SYNTAX.
print("Hello, World!")
print(3 + 4)

# VARIABLES
# In Python, variables are used to store data that can be used and manipulated throughout a program.

# Rule of defining a variable in Python
# Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# They can contain letters, numbers, and underscores.
# Variable names are case-sensitive (age and Age are different).
# Avoid using Python keywords (e.g., if, for, while) as variable names.

# 34age = 4 # Invalid because variable cannot start with a number
age = 32  # Valid
# a$$ge = 45 # Invlaid because variables cannot contain special characters other than _
__age = 34  # Valid

# DATATYPES.
#     Integers (int): Whole numbers (e.g., 10, -5).
#     Floats (float): Decimal numbers (e.g., 3.14, -0.001).
#     Strings (str): Text data enclosed in quotes (e.g., "Hello", 'Python').
#     Booleans (bool): Represents True or False.
#     Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
#     Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
#     Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
#     Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25}).

age = 3
print(age)
print(type(age))

cgpa = 8.2
print(cgpa)
print(type(cgpa))

name = "Ronak"
print(name)
print(type(name))

is_completed = True  # can also be False
print(is_completed)
print(type(is_completed))


# ERROR
"""print("Hi
Ronak
good
morning")"""

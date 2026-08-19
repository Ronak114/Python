# Strings are IMMUTABLE.
s = "hello World"
# s[0] = "R" # You cannot do this
print(len(s))  # length of string

# Methods (original string is not changed)
print(s.upper(), s)
print(s.lower())
print(s.capitalize())
print(s.title())

text = "   Python is fun and fun    "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.find("is"))  # Output: 7 Index of first occurence
print(text.replace("fun", "awesome"))

fruits = "Apples,Bananas,Pineapples"
print(fruits.split(","))
print(",".join(["Apples", "Bananas", "Pineapples"]))

text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False
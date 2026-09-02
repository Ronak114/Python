# MODULES.
# Two types of modules in Python:
# - Built-in Modules
# - External Modules

# built-in Modules
import math
import os

print(math.sqrt(16))

# Creating a module
import mymodule

mymodule.hello()  # calling the function from mymodule.py

# External Modules. (pip install requests)
import requests

r = requests.get("https://www.google.com")
print(r.text)

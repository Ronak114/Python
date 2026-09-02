# SCOPE
def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1  # It creates a local variable called z which is destroyed after this function returns
    return c


print(sum(4, 6))

z = 8  # z is a global variable
print(z)
print("------------")


# global
def sum(a, b):
    print("Hey I am good ")
    c = a + b
    global z  # Please modify global z
    z = 0  # This will refer to global z and not create a local variable
    return c


z = 3
print(sum(3, 12))
print(z)


# DOC string
def sum(a, b):
    """This will sum two numbers"""
    c = a + b
    return c


print(sum.__doc__)

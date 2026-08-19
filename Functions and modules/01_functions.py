# Functions are a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.


# function definition - def(keyword).
def average(a, b, c):  # parameters.
    d = (a + b + c) / 3.0
    return d


print(average(3, 5, 1))  # function calling with positional arguments

x = average(4, 2, 1)
print(x)


# function with default arguments
def add(a, b, plus=0):
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)  # keyword arguments.
print(c1)

# operates on iterable.

# MAP
numbers = [1, 2, 3, 45, 4, 21]

def square(x):
    return x * x

# new = list(map(square, numbers))
new = list(map(lambda x: x * x, numbers))
print(new)


# FILTERS
def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False

a = [1, 3, 5, 234, 34, 32, 6543, 23, 2, 5, 6, 7, 43]

# new = list(filter(lambda x: x > 9, a))
new = list(filter(is_greater_than_9, a))
print(new)


# REDUCE.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

def sum(a, b):
    return a + b

c = reduce(sum, numbers)
print(c)

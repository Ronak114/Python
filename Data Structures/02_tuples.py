# Tuples are immutable, meaning that once they are created, their elements cannot be changed.

a = (3, 2, 22, 13)
b = (3,)  # single element tuple, note the comma.

print(a)
print(a[2])
# a[3] = 32 # cannot change


# tuple unpacking
t = (3, 2, 45)
a, b, c = t
print(a, b, c)


# methods
tuple = (3, 12, 1, 54, 23, 12)

print(tuple.count(12))
print(tuple.index(12))

# faster than lists,
# used for dictionary keys, and for fixed data that does not need to change.

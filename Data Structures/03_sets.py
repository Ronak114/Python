# sets - unordered, unique

set = {3, 23, 2, 11}
print(set, type(set))
# print(set[3])  # Error bcz not ordered.


# Methods.
s = {34, 23, 1, 3, 22}

print(s)

s.add(32)
print(s)
s.remove(32)
print(s)

# s.remove(434234)  # as 4253 is not present Throws an error
s.discard(42323) # Does not throw an error even if the element is not present in the set.
print(s)


# set operations.
a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)  # Contains all the elements in a along with all the elements in b
print(c)

d = a.intersection(b)  # Contains only the elements that are present in a as well as b
print(d)
fruits = ["apple", "banana", "cherry"]

# print 1st fruit.
print(fruits[0])
# replace banana with orange
fruits[1] = "orange"
print(fruits)
# print length of fruits.
print(len(fruits))


# Print the first and the last three numbers using slicing.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a=[i for i in range(1,11)]

print(a[0:3])
print(a[-3:])


# Sort ascending order,Append 10 and remove 2.
numbers = [5, 2, 9, 1, 7]

# list.sort(numbers) - works
numbers.sort()
print(numbers)
numbers.append(10)
numbers.remove(2)
print(numbers)


# use the insert() to add "David" at index 1 .
names = ["Alice", "Bob", "Charlie"]

names.insert(1, "David")
print(names)


"""Create a tuple coordinates = (10, 20) and print both elements.
Try to modify the tuple by setting coordinates[0] = 50 — note what
happens.Convert the tuple to a list, change its first element to 50 , and convert it back to a tuple."""

t = (10, 20)
print(t)
print(t[0])
# print(t[0])=50 # error
print(t)

t_list = list(t)  # changing tuple to list.
print(t_list)
t_list[0] = 50
t = tuple(t_list)  # changing list to tuple.
print(t)


# Add 5 to the set, remove 2 , and check if 4 is in the set.
my_set = {1, 2, 3, 3, 4}
print(my_set)
my_set.add(5)
my_set.remove(2)
print(4 in my_set)
print(my_set)


# Find Union, Intersection and Difference
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# Print the value of "name". Change "grade" to "A+". Add a new key "city" = "Delhi".
student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])
student["grade"] = "A+"
student["city"] = "Delhi"
print(student)


# find the product with the highest price
prod = {"laptop": 80000, "phone": 50000, "earphones": 5000}

highest_product = max(prod, key=prod.get)
print(highest_product, prod[highest_product])

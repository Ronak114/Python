# list - ordered, mutable and mixed data type
marks = [54, 23, 64, 93, 32]
mixed = [43, "Hello", False, 4.2]

print(marks[2:4])
print(marks[2])
# print(mixed[4])  # Error Index out of bound


# Methods
extra_marks = [53, 23, 32]

extra_marks.append(63)  # This will change the original list
print(extra_marks)
extra_marks.pop()
print(extra_marks)

marks.extend(extra_marks)
print(marks)


# lIST comprehension
# Create a list containing the table of 5
table = []
for i in range(1, 11):
    table.append(5 * i)
print(table)

# via list comprehension
table1 = [5 * i for i in range(1, 11)]
print(table1)
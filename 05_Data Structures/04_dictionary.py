marks = {"Ronak": 100, "Teja": 85, "Rahi": 100}

print(marks, type(marks))
print(marks["Rahi"])
marks["Ronak"] = 3
print(marks)


# Methods
print(marks.keys())
print(marks.values())
marks.pop("Rahi")
print(marks)
marks.clear()
print(marks)

# dictionary comprehension
table_of_5 = {i: 5 * i for i in range(1, 11)}

print(table_of_5)
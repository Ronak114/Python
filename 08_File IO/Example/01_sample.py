# 1. Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
f = open("notes.txt", "w")
f.write("Learning Python is fun!")
f.close()


# 2. Open notes.txt , read its content, and print it to the console
f = open("notes.txt", "r")
content = f.read()
print(content)


# 3. Write a program that writes three lines of text to a file tasks.txt .
f = open("tasks.txt", "w")
f.write("""
Hello
Good morning
Have a nice day""")
f.close()


# 4. Open tasks.txt in append mode and add a new line "Task Completed!".Read the file and print all lines as a list using readlines() .
f = open("tasks.txt", "a")
f.write("Task Completed!")
f.close()
f = open("tasks.txt", "r")
content = f.readlines()
print(content)
f.close()

# Write a program that reads a file and creates another file with all words converted to uppercase.
f = open("notes.txt", "r")
content = f.read()
f.close()

f = open("notes_upper.txt", "w")
f.write(content.upper())
f.close()

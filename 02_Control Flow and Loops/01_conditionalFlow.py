# IF
a = 12
if a > 18:
    print("You can drive")
print("End of program")

# IF ELSE
age = int(input("Enter your age: "))
if age > 18:
    print("You can drive")
else:
    print("You cannot drive")
print("End of program")

# IF ELIF ELSE
age1 = int(input("Enter your age: "))
if age1 > 18:
    print("You can drive")
elif age1 == 18:
    print("Lets schedule an interview")
elif age1 == 0:
    print("Hey you are just born")
else:
    print("Sorry you cannot drive")
print("End of program")
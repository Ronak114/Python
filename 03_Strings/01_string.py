# Intro
name = "HI"
name = '''Good morning'''  # multiple line allowed
name = "Ronak"
print(name)

# Indexing
name = "R   o   n  a   k"
#         0   1   2  3   4
#        -5  -4  -3 -2  -1

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # error

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])  # name[-4+5] name[1]
print(name[-5])
print(name[-6]) # error

# Slicing
name = "Ronak9876543210"
print(name[0:2]) # goes from 0 to n-1
print(name[0:10:1]) # Skip n-1 characters
print(name[0:10:1])  # Skip 0 character
print(name[0:10:3])  # Skip 3-1 ie 2 characters
print(name[:4])  # Replace the first empty number with 0 # name[0:4]
print(name[1:])  # Replace the second empty number with length # name[1:15]
# Count vowel in a string
s = "Hello World"
vowels = ["a", "e", "i", "o", "u"]

c = 0
for char in s.lower():
    if char in vowels:
        c += 1
print(c)

# check palindrome
x = "racecar"
y = "racecar"

if x[::-1] == y:
    print("Palindrome")
else:
    print("Not palindrome")
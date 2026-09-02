# Print whether a number is positive, negative or zero
a=int(input("Enter a number: "))
if a>0:
    print("Positive number")
elif a==0:
    print("Zero")
else:
    print("Negative No")

# Guess no is EVEN or ODD.
b=int(input("Enter no:"))
if b%2==0:
    print("EVEN")
else:
    print("ODD")

# Enter number corresponding day of week will print
num = int(input("Enter No:"))
match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("saturday")
    case _:
        print("enter from 1 to 7")

# Calculte the sum of all no from 1 to 100.
sum=0
for i in range(1,101):
    sum+=i
print(sum)

# WAP that keeps asking user to enter a number until we enter a negative number. Once a negative number is entered, print the sum of all the numbers entered.
sum = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    else:
        sum += num
print(sum)

# Use loop to reverse a no.
a=123
reverse=0
while a>0:
    last_digit=a%10
    reverse=reverse*10+last_digit
    a=a//10
print(reverse)
# # EXCEPTION HANDLING.
# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The division is {a / b}")

#     except Exception as e:
#         print("Unknown error occurred!", e)

#     except ValueError:
#         print("Enter only numbers")

#     except ZeroDivisionError:
#         print("Dont divide by 0")


# RAISING AND ERROR
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please dont divide by 0")
print(f"The division is {a / b}")


# ELSE - Gets executed when there is no error in the try block
try:
    a = 345 / 10

except Exception as e:
    print(e)

else:
    print("Hey I am good")


# FINALLY
def divide(a, b):
    try:
        c = a / b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

    # This is always executed no matter if try completely executes or not
    finally:
        print("This is always executed")

X = int(input("Enter number 1: "))
Y = int(input("Enter number 2: "))
divide(X,Y)

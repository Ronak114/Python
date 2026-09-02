# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper

def say_hello():
    print("Hello!")

# one way
say_hello()
f = decorator(say_hello)
f()


# # another way
# @decorator
# def say_hello():
#     print("Hello!")

# say_hello() # make say_hello() as decorator
# args
def sum(*args):
    # args will be a tuple of all the values passed to sum
    total = 0
    for item in args:
        total += item
    return total

print(sum(342, 2, 7, 9))


# kwargs
def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(a=34, b=54, c=34, d=90, e=45)


# Combined Args Kwargs.
def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, a=34, b=32, c=31)

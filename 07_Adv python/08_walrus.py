# WAlrus(:=) - new operator / assignment operator.


def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70


# calling once and then using its value.
# a = very_slow_func()
# if(a>10):
#     print(a)
# else:
#     print("Its not greater than 10")


# Via Walrus
if (a := very_slow_func()) > 10:
    print(a)
else:
    print("Its not greater than 10")

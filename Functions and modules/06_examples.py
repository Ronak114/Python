# Write a lambda fuction that add 2 no.
add = lambda a, b: a + b
print(add(2, 3))


# Use map() with lambda to get squares.
x = [1, 2, 3, 4]
sq = lambda a: a * a

ans = list(map(sq, x))
print(ans)


# Write a recursive funtn that returns factorial.
def factorial(n):
    # base case
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(2))
print(factorial(5))
print(factorial(10))


# Write a recursive funtn that returns sum of all digits of given no.
def sum_of_digits(x):
    if x == 0:
        return 0
    return x % 10 + sum_of_digits(x // 10)

print(sum_of_digits(1234))


# Write a recursive function that prints the first n Fibonacci numbers.
def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    fibonacci(n - 1, b, a + b)

fibonacci(5)

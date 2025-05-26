def multiply(a, b):
    # base case
    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b - 1)

    # incase it is negative
    else:
        return -multiply(a, -b)


print(multiply(5, 2))


# number 2
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)


print(power(2, 3))


# number3
# Countdown
def count(n):
    # Base case: if n is less than 0, stop recursion
    if n < 0:
        return
    # Print the current number
    print(n)
    # Recursive call with n - 1
    count(n - 1)


count(3)


# Countdown modified
def count(n, d=0):
    # Base case: if n is less than 0, stop recursion
    if d > n:
        return
    # Print the current number
    print(d)
    # Recursive call with n - 1
    count(n, d + 1)


count(2)


# Reverse Strings
def reverse(s):
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    # Recursive case: last character + reverse of the rest
    return s[-1] + reverse(s[:-1])


print(reverse("cat"))


def is_prime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)


print(is_prime(7))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
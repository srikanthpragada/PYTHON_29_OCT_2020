# Number related function

PI = 22 / 7


def iseven(n):
    """
    Returns true if the given number is even otherwise false
    Args:
      n -> number
    Returns
      True for even, False for odd
    """
    return n % 2 == 0


def isprime(n):
    """
    Returns true if the given number is prime number otherwise false
    """
    pass


# Test when module is run as script
if __name__ == '__main__':
    print(isprime(11))
    print(iseven(10))
    print(PI)
else:
    print("Importing number_funs")
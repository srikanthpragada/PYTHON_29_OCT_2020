def operation(func, a, b):
    print(func(a, b))


def multiply(x, y):
    return x * y


def add(x, y):
    return x + y


operation(multiply, 10, 20)  # Pass function as param
operation(add, 100, 200)

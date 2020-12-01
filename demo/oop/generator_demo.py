def numbers():
    for i in range(1, 3):
        yield i


n = numbers()
print(type(n))

print(next(n))
print(next(n))
print(next(n))


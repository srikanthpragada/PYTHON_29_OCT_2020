squares = []
for n in range(1, 10):
    squares.append(n * n)

print(squares)

squares = [n * n for n in range(1, 10)]
print(squares)

uppers = [c for c in "Python Language" if c.isupper()]
print(uppers)
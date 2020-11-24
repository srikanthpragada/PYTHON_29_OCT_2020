def add(n1, n2):
    if isinstance(n1, str):
        return int(n1) + int(n2)
    else:
        return n1 + n2


print(add(10, 20))
print(add("10", "20"))

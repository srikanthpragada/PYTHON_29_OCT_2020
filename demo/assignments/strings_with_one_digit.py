def has_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


values = ['abc', 'xyz', '123', 'a12', 'pqr3', '2bc', 'def']

for v in filter(str.isdigit, values):
    print(v)

for v in filter(has_digit, values):
    print(v)
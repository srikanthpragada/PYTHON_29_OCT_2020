
s1 = "Python"
s2 = "JavaScript"

# Without intersection
for c in set(s1):
    if c in s2:
        print(c)

# With intersection
for c in set(s1) & set(s2):
    print(c)
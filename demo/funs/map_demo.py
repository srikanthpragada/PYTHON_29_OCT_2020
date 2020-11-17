names = ['abc', 'xyz', 'pqr', 'de']

for v in map(len, names):
    print(v)

for v in map(str.upper, names):
    print(v)

marks = "70,69,78,89,54"

# Doesn't work
# print(sum(marks.split(",")))

print(sum(map(int, marks.split(","))))

data = ['Bill,80', 'Scott,90', 'Tom,87', 'Steve,87', 'Bob,76', 'Scott,70']

students = {}
for e in data:
    n, m = e.split(',')  # Unpack name and marks
    students[n] = m

for n, m in sorted(students.items()):
    print(f"{n:10} - {m:3}")

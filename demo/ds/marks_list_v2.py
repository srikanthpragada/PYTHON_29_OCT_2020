data = ['Bill,80', 'Scott,90', 'Tom,87', 'Steve,87', 'Bob,76',
        'Scott,70', 'Bill,87', 'Tom,76', 'Tom,90']

students = {}
for e in data:
    n, m = e.split(',')  # Unpack name and marks
    if n in students:
        students[n] += int(m)
    else:
        students[n] = int(m)

for n, total in sorted(students.items()):
    print(f"{n:10} - {total:3}")

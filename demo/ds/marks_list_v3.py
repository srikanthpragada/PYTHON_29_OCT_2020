data = ['Bill,80,90,76', 'Scott,90,88', 'Tom,87,77,88,65', 'Steve,87,88', 'Bob,76']

students = {}
for e in data:
    parts = e.split(',')  # Unpack name and marks
    name = parts[0]
    total = 0
    for m in parts[1:]:
        total += int(m)

    students [name] = total

for n, total in sorted(students.items()):
    print(f"{n:10} - {total:3}")

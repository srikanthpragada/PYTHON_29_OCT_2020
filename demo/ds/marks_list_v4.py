data = ['Bill,80,90,76', 'Scott,90,88', 'Tom,87,77,88,65', 'Steve,87,88', 'Bob,76']

students = {}
for e in data:
    parts = e.split(',')  # Unpack name and marks
    name = parts[0]
    marks = [int(m) for m in parts[1:]]
    students [name] = marks

for n, marks in sorted(students.items()):
    print(f"{n:10} - {sum(marks):3} -  {marks}")

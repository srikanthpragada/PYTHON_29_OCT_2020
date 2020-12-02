# Take details from marks.txt and print name, average, total
students = {}

with open("marks.txt", "rt") as f:
    for line in f:
        parts = line.strip().split(",")
        name = parts[0]
        total = sum(map(int, parts[1:]))  # Convert each entry to int
        average = total / (len(parts) - 1)
        students[name] = (total, average)

for name, (total, average) in sorted(students.items()):
    print(f"{name:20} {total:3} {average:5.2f}")

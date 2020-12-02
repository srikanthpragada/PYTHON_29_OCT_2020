with open("names.txt", "rt") as f:
    names = []

    for line in f.readlines():
        parts = line.split(",")
        names.extend([p.strip() for p in parts if len(p.strip()) > 0])
        #names.extend(map(str.strip, parts))

for name in sorted(names):
    print(name)

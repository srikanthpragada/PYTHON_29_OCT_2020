values = [-10, 11, -5, 20, -40, 6]
names = ['Abc', 'ab', 'XYZA', 'pqrst']
codes = ['AB122', 'BB39393', 'AC39393', 'BA933']


for v in sorted(names, key=lambda s: s[:2].upper()):
    print(v)
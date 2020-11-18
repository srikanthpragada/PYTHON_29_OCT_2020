values = [-10, 11, -5, 20, -40, 6]
names = ['Abc', 'ab', 'XYZA', 'pqrst']
codes = ['AB122', 'BB39393', 'AC39393', 'BA933']

for v in sorted(values, key=abs, reverse=True):
    print(v)

for v in sorted(names, key=str.upper):
    print(v)


def first2(s):
    return s[:2]


for v in sorted(codes, key=first2):
    print(v)

for v in sorted(codes, key=lambda s : s[::-1]):
    print(v)
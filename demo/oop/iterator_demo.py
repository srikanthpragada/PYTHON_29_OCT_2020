l = [1, 2, 3]
li = l.__iter__()  # iter(l)
print(type(l), type(li))
print(li.__next__())  # next(li)
print(li.__next__())
print(li.__next__())
#print(li.__next__())

li = iter(l)
for v in li:
    print(v)

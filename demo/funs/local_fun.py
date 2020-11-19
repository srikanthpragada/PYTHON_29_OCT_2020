def f1():
    a = 0

    def f2():
        nonlocal a
        a = a + 1

    f2()
    f2()
    print(a)


f1()

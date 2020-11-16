def fun(**kwargs):
    print(kwargs)


def display(*args, **kwargs):
    print(args)
    print(kwargs)


fun(a=10, b=20)
fun(name='Python', ver=3.9)
display(10, 20, 30, a=100, b=200)

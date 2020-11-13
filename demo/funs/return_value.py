
def next_even(num):
    if num % 2 == 0:
        return num + 2
    else:
        return num + 1


n = next_even(10)
print(n)
n = next_even(15)
print(n)


print(1, 2, end=' ')
for num in range(3, 101, 2):  # Take only odd numbers
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')

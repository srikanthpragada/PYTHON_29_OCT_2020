# Take a number and display its factors

num = int(input("Enter a number :"))

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i, end=' ')


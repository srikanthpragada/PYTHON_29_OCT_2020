# Take a number and display whether it is prime

num = int(input("Enter a number :"))
prime = True
for i in range(2, num // 2 + 1):
    if num % i == 0:
        prime = False
        break


if prime:
    print("Prime number!")
else:
    print("Not a prime number!")


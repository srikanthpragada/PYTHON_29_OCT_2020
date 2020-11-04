# Take 5 numbers and print total
i = 1
total = 0
while i <= 5:
    num = int(input("Enter a number :"))
    total = total + num  # total += num
    i += 1

print("Total = ", total)
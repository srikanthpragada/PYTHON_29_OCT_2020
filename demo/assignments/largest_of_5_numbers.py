# Take 5 numbers and print largest
i = 1
largest = 0
while i <= 5:
    num = int(input("Enter a number :"))
    if num > largest:
        largest = num
    i += 1

print("Largest = ", largest)
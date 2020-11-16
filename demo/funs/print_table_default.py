# Function to print table for the given number
def print_table(num=15, length=10):
    for i in range(1, length + 1):
        print(f"{num:2} * {i:2} = {i * num:4}")


print_table()
print_table(15)  # Call function using positional arguments
print_table(10, 5)
print_table(length=5, num=23)  # Using keyword arguments
print_table(num=23)  # Using keyword arguments

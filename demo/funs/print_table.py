# Function to print table for the given number
def print_table(num, length):
    for i in range(1, length + 1):
        print(f"{num:2} * {i:2} = {i * num:4}")


print_table(15, 5)  # Call function using positional arguments
print_table(length=5, num=23)  # Using keyword arguments

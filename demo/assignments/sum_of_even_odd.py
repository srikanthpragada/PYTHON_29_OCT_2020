# Print sum of even numbers and odd numbers between 1 and 100

i = 1
even_sum = odd_sum = 0
while i <= 100:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

    i += 1

print(f"Even sum = {even_sum}, Odd sum = {odd_sum}")


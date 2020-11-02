# Calculate net price with 10% discount and 12% tax

price = float(input("Enter price :"))
discount = price * 0.10
after_discount = price - discount
tax = after_discount * 0.12
net = after_discount + tax
print('Net price = ', net)

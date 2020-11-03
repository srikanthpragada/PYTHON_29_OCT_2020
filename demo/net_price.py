# Calculate net price with 10% discount and 12% tax

price = float(input("Enter price :"))
if price > 10000:
    discount = price * 0.20
else:
    discount = price * 0.10

after_discount = price - discount
tax = after_discount * 0.12
net = after_discount + tax

# display details
print(f"Price            {price:10.2f}")
print(f"- Discount       {discount:10.2f}")
print("                  -----------")
print(f"After Discount   {after_discount:10.2f}")
print(f"+ Tax            {tax:10.2f}")
print("                  -----------")
print(f"- Net price      {net:10.2f}")


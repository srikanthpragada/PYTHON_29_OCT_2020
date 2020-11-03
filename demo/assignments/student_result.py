# Take two marks and display result
# If more than 60 in each subject  - pass
# If more than 90 in any one subject - pass

m1 = int(input("Marks in subject 1 :"))
m2 = int(input("Marks in subject 2 :"))

if m1 > 60 and m2 > 60:
    print("Passed")
elif m1 > 90 or m2 > 90:
    print("Passed")
else:
    print("Failed")

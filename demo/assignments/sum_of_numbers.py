st = "80,86,xyz,55,66,70,80,90,abc"
marks = [int(v) for v in st.split(",") if v.isdigit()]
print(marks)
print(sum(marks))

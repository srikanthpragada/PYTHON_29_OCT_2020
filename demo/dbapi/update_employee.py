import sqlite3

con = sqlite3.connect(r"c:\classroom\oct29\hr.db")
cur = con.cursor()
id = int(input("Enter id :"))
salary = int(input("Enter new salary :"))
try:
    cur.execute("update employees set salary = ? where id = ?", (salary, id))
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()
    else:
        print("Sorry! Employee id not found!")
except Exception as ex:
    print("Error : ", ex)

cur.close()
con.close()

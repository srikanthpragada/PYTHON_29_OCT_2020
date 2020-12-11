import sqlite3

con = sqlite3.connect(r"c:\classroom\oct29\hr.db")
cur = con.cursor()
cur.execute("select fullname,salary from employees order by salary desc")

for name, salary in cur.fetchall():
    print(f"{name:30}  {salary:10}")

cur.close()
con.close()

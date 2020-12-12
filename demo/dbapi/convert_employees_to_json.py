import sqlite3
import json

con = sqlite3.connect(r"c:\classroom\oct29\hr.db")
cur = con.cursor()
cur.execute("select * from employees")

employees = []
for id, name, job, salary in cur.fetchall():
    emp = {'id': id, 'name': name, 'job': job, 'salary': salary}
    employees.append(emp)

cur.close()
con.close()

print(json.dumps(employees))

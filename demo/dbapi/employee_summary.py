import sqlite3

con = sqlite3.connect(r"c:\classroom\oct29\hr.db")
cur = con.cursor()
cur.execute("select count(id), sum(salary), avg(salary) from employees")

summary = cur.fetchone()
print(f'No. of employees : {summary[0]:10}')
print(f'Total salary     : {summary[1]:10}')
print(f'Avg. salary      : {summary[2]:10.0f}')

cur.close()
con.close()

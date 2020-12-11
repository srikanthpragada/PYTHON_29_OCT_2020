import sqlite3

con = sqlite3.connect(r"c:\classroom\oct29\hr.db")
print(con)
con.close()
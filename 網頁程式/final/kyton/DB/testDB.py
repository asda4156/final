import sqlite3
dbfile = "db.sqlite3"
conn = sqlite3.connect('../kyton/db.sqlite3')
rows = conn.execute("select * from login;")
for row in rows:
    for field in row:
        print("{}\t".format(field), end="")
    print()
conn.close()
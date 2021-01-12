import sqlite3
conn = sqlite3.connect("db.sqlite3")
print ('Opened database successfully')

cursor = conn.execute("select username,account,password  from login")

for row in cursor:
    print ('username = '), row[0]
    print ('account = '), row[1]
    print ('password = '), row[2] 

print ('Opened database successfully')

conn.close()
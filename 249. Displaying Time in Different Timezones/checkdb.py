import sqlite3

db = sqlite3.connect("accounts.sqlite")

for row in db.execute("SELECT * FROM history"):
    # print(row)
    local_time = row[0]
    print("{}\t{}".format(local_time, type(local_time)))

db.close()

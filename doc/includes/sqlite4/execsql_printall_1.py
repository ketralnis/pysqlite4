from pysqlite4 import dbapi2 as sqlite4

# Create a connection to the database file "mydb":
con = sqlite4.connect("mydb")

# Get a Cursor object that operates in the context of Connection con:
cur = con.cursor()

# Execute the SELECT statement:
cur.execute("select * from people order by age")

# Retrieve all rows as a sequence and print that sequence:
print cur.fetchall()

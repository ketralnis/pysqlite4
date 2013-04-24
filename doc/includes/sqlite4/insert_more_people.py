from pysqlite4 import dbapi2 as sqlite4

con = sqlite4.connect("mydb")

cur = con.cursor()

newPeople = (
    ('Lebed'       , 53),
    ('Zhirinovsky' , 57),
  )

for person in newPeople:
    cur.execute("insert into people (name_last, age) values (?, ?)", person)

# The changes will not be saved unless the transaction is committed explicitly:
con.commit()

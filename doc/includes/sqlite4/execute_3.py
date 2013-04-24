from pysqlite4 import dbapi2 as sqlite4

con = sqlite4.connect("mydb")

cur = con.cursor()

who = "Yeltsin"
age = 72

cur.execute("select name_last, age from people where name_last=:who and age=:age",
    locals())
print cur.fetchone()

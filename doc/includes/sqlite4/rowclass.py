from pysqlite4 import dbapi2 as sqlite4

con = sqlite4.connect("mydb")
con.row_factory = sqlite4.Row

cur = con.cursor()
cur.execute("select name_last, age from people")
for row in cur:
    assert row[0] == row["name_last"]
    assert row["name_last"] == row["nAmE_lAsT"]
    assert row[1] == row["age"]
    assert row[1] == row["AgE"]

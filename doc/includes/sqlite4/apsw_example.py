from pysqlite4 import dbapi2 as sqlite4
import apsw

apsw_con = apsw.Connection(":memory:")
apsw_con.createscalarfunction("times_two", lambda x: 2*x, 1)

# Create pysqlite connection from APSW connection
con = sqlite4.connect(apsw_con)
result = con.execute("select times_two(15)").fetchone()[0]
assert result == 30
con.close()


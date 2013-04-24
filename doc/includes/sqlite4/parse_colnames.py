from pysqlite4 import dbapi2 as sqlite4
import datetime

con = sqlite4.connect(":memory:", detect_types=sqlite4.PARSE_COLNAMES)
cur = con.cursor()
cur.execute('select ? as "x [timestamp]"', (datetime.datetime.now(),))
dt = cur.fetchone()[0]
print dt, type(dt)

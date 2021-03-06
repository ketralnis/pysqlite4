from pysqlite4 import dbapi2 as sqlite4
import md5

def md5sum(t):
    return md5.md5(t).hexdigest()

con = sqlite4.connect(":memory:")
con.create_function("md5", 1, md5sum)
cur = con.cursor()
cur.execute("select md5(?)", ("foo",))
print cur.fetchone()[0]

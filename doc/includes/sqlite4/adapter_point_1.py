from pysqlite4 import dbapi2 as sqlite4

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):
        if protocol is sqlite4.PrepareProtocol:
            return "%f;%f" % (self.x, self.y)

con = sqlite4.connect(":memory:")
cur = con.cursor()

p = Point(4.0, -3.2)
cur.execute("select ?", (p,))
print cur.fetchone()[0]

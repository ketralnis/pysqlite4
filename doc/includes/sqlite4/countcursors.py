from pysqlite4 import dbapi2 as sqlite4

class CountCursorsConnection(sqlite4.Connection):
    def __init__(self, *args, **kwargs):
        sqlite4.Connection.__init__(self, *args, **kwargs)
        self.numcursors = 0

    def cursor(self, *args, **kwargs):
        self.numcursors += 1
        return sqlite4.Connection.cursor(self, *args, **kwargs)

con = sqlite4.connect(":memory:", factory=CountCursorsConnection)
cur1 = con.cursor()
cur2 = con.cursor()
print con.numcursors

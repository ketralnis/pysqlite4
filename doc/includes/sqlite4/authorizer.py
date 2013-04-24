from pysqlite4 import dbapi2 as sqlite4

def authorizer_callback(action, arg1, arg2, dbname, source):
    if action != sqlite4.SQLITE4_SELECT:
        return sqlite4.SQLITE4_DENY
    if arg1 == "private_table":
        return sqlite4.SQLITE4_DENY
    return sqlite4.SQLITE4_OK

con = sqlite4.connect(":memory:")
con.executescript("""
    create table public_table(c1, c2);
    create table private_table(c1, c2);
    """)
con.set_authorizer(authorizer_callback)

try:
    con.execute("select * from private_table")
except sqlite4.DatabaseError, e:
    print "SELECT FROM private_table =>", e.args[0]     # access ... prohibited

try:
    con.execute("insert into public_table(c1, c2) values (1, 2)")
except sqlite4.DatabaseError, e:
    print "DML command =>", e.args[0]     # access ... prohibited


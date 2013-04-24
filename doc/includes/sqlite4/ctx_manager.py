from __future__ import with_statement
from pysqlite4 import dbapi2 as sqlite4

con = sqlite4.connect(":memory:")
con.execute("create table person (id integer primary key, firstname varchar unique)")

# Successful, con.commit() is called automatically afterwards
with con:
    con.execute("insert into person(firstname) values (?)", ("Joe",))

# con.rollback() is called after the with block finishes with an exception, the
# exception is still raised and must be catched
try:
    with con:
        con.execute("insert into person(firstname) values (?)", ("Joe",))
except sqlite4.IntegrityError:
    print "couldn't add Joe twice"



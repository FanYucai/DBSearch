import MySQLdb

db = MySQLdb.connect("localhost","root","12345678","labdb")

cursor = db.cursor()

sql = """insert into testtable(testCol1, testCol2) values (666, 666)""";

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()

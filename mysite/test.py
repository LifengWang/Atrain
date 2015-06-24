__author__ = 'root'
import MySQLdb

s = '"USDCNY=x",6.2083,"6/24/2015","4:55am"'

print s
print(s.split(','))


value = [1, '"USDCNY=x"', '6.2083', '"6/24/2015"', '"4:55am"']

conn = MySQLdb.connect(host='localhost', user='root', passwd='123456')
cursor = conn.cursor()

conn.select_db('currencies')

print value
cursor.execute("insert into quote values(%s,%s,%s,%s,%s)", value)

cursor.close()

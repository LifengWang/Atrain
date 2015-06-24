__author__ = 'root'
import MySQLdb

s = '"USDCNY=x",6.2083,"6/24/2015","10:09am"\n"'

content = s.split(",")
print content[3].split('\n')[0].strip('\"')

# value = [2, 'USDCNY=x', '6.2083', '6/24/2015', '4:55am']
#
# conn = MySQLdb.connect(host='localhost', user='root', passwd='123456')
# cursor = conn.cursor()
# conn.select_db('currencies')
# print value
# cursor.execute("insert into quote values(%s,%s,%s,%s,%s)", value)
# conn.commit()
# cursor.close()

#
# value = [1, "test"]
# cursor.execute("insert into test values(%s,%s)", value)
# conn.commit()
# # values = []
# # for i in range(20):
# #     values.append((i, 'Hello mysqldb, I am recoder ' + str(i)))
# # cursor.executemany("""insert into test values(%s,%s) """, values)
# cursor.close()

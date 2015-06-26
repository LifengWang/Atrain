import urllib2
import MySQLdb

fromCurrency = 'USD'
toCurrency = 'CNY'

url = 'http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s='+fromCurrency+toCurrency+'=x'

print url
# url = 'http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=USDCNY=x'

req = urllib2.Request(url)
req.add_header('Content-Type', "application/x-www-form-urlencoded")
resp = urllib2.urlopen(req)
result = resp.read()
content = result.split(",")
print content

# conn = MySQLdb.connect(host='localhost', user='root', passwd='123456')
# cursor = conn.cursor()
# conn.select_db('currencies')
# values = [4, content[0].strip('\"'), content[1].strip('\"'), content[2].strip('\"'), content[3].split('\n')[0].strip('\"')]
#
# print values
# cursor.execute("insert into quote values(%s,%s,%s,%s,%s)", values)
# conn.commit()
# cursor.close()

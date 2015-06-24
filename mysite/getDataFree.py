import urllib2
import MySQLdb

fromCurrency = 'USD'
toCurrency = 'CNY'

url = 'http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s='+fromCurrency+toCurrency+'=x'

# url = 'http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=USDCNY=x'

req = urllib2.Request(url)
req.add_header('Content-Type', "application/x-www-form-urlencoded")
resp = urllib2.urlopen(req)
content = resp.read()
print content

conn = MySQLdb.connect(host='localhost', user='root', passwd='123456')
cursor = conn.cursor()

value = [1, content]

print value
cursor.execute("insert into test values(%s,%s,%s,%s,%s)", value)

cursor.close()

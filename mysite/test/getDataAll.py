import urllib
import urllib2
import json

url = 'http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote'

req = urllib2.Request(url)
req.add_header('Content-Type', "application/x-www-form-urlencoded")
resp = urllib2.urlopen(req)
content = resp.read()
print(content)

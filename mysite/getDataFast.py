__author__ = 'root'
import sys, urllib, urllib2, json




url = 'http://apis.baidu.com/apistore/currencyservice/currency?fromCurrency=CNY&toCurrency=USD&amount=2'

req = urllib2.Request(url)

req.add_header("apikey", "b1efda1ac20be265ceff79a0b1bb46e4")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
#encoding=utf-8
import sys, urllib, urllib2, json

appkey = '6fe61698de1adb615017a70d892cd109' #您申请到的数据的APPKEY
url = 'http://web.juhe.cn:8080/finance/exchange/rmbquot' #数据API请求URL
paramsData = {'ip': "www.juhe.cn", 'key': '6fe61698de1adb615017a70d892cd109'} #需要传递的参数
params = urllib.urlencode(paramsData)

print(appkey)
req = urllib2.Request(url, params)
req.add_header('Content-Type', "application/x-www-form-urlencoded")
resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    result = json.loads(content, 'utf-8')
    error_code = result['error_code']
    if(error_code == 0):
        data = result['result'] #接口返回结果数据
        print(data)
    else:
        errorinfo = str(error_code)+":"+result['reason'] #返回不成功，错误码:原因
        print(errorinfo)
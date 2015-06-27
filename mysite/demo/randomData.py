# coding=utf8

import time
import random
import datetime
import sqlite3
import os

CUR_PATH = os.getcwd()

random.seed(time.time())
cx = sqlite3.connect(CUR_PATH+"\demo.db")


class fanice(object):
	def __init__(self, ts):
		self.from_currency  = ""
		self.to_currenct = ""
		self.ratio = 0.0
		self.t_when = ts

	def randData(self):
		self.from_currency = "USD"
		self.to_currenct = "CNY"
		self.ratio = round(6 + -1 + 2 * random.random(),3)
		pass

def randomData():
	_t = getStartT()

	cu = cx.cursor()
	count = 10000
	loop = 0
	for idx in xrange(0,count):
 		f = fanice(_t+idx)
 		f.randData()
 		sql = '''insert into demotest (from_currency, 
 			to_currenct, ratio, t_when) values (
 			'%s','%s',%f,%d) ''' % (f.from_currency, f.to_currenct, 
 			f.ratio, f.t_when)
 		cu.execute(sql)
 		loop+=1
 		if loop == 100:
 			loop = 0 
 			cx.commit()
 	cu.close()

def createDB():
	cu = cx.cursor()
	try:
		cu.execute('''create table demotest (id  integer PRIMARY KEY autoincrement,from_currency varchar(10),
			to_currenct varchar(10), ratio DOUBLE, t_when integer)''')
		cx.commit()
	except Exception,e:
		print e
	cu.close()

def dropDB():
	cu = cx.cursor()
	try:
		cu.execute('''
			drop table if exists demotest''')
	except Exception,e:
		print e
	cx.commit()

def getStartT():
	_d = datetime.datetime.strptime("2015-06-27 12:00:00",
			 "%Y-%m-%d %H:%M:%S")
	_t = int(time.mktime(_d.timetuple()))
	return _t

def getOneData(t_when):
	cu = cx.cursor()
	sql = '''select * from demotest 
		where t_when=%s ''' % (t_when)
	rs = cu.execute(sql)
	for r in rs:
		return  r
	cu.close()

def getDatas(start_when, end_when):
	result = []
	cu = cx.cursor()
	sql = '''select * from demotest 
		where t_when>=%d and t_when<=%d''' % (start_when, end_when)
	rs = cu.execute(sql)
	for r in rs:
		result.append(r) 
	cu.close()
	return result

def getResult():
	_t = getStartT()
	watch_list = []
	##初始化观察数组
	init_length = 20*5*60
	watch_list = getDatas(_t, _t+init_length)
	acc = init_length
	
	TURN_ON_FLAG = 0
	for idx in xrange(acc,10000):
		raw_data = getOneData(_t + idx)

		watch_list = watch_list[1:len(watch_list)]
		watch_list.append(raw_data)
		EMA5 = _getEMA(watch_list,5)
		EMA13 = _getEMA(watch_list,13)
		EMA20 = _getEMA(watch_list,20)
		if EMA5 > EMA13 and EMA5 > EMA20 and TURN_ON_FLAG==0:
			TURN_ON_FLAG = 1
			print 'BEGIN, BUY ACTION ON !', ts2dstr(raw_data[4])
		elif EMA5 <EMA13 and EMA5 < EMA20 and TURN_ON_FLAG ==1:
			TURN_ON_FLAG = 0
			print 'END  , BUY SHUT DOWN !', ts2dstr(raw_data[4])

def ts2dstr(ts):
	da = datetime.datetime.fromtimestamp(ts)
	return da.strftime("%Y-%m-%d %H:%M:%S")

def _getEMA(datas, ema_coffidence):
	total_ema = 0
	for idx in xrange(5):
		_tmp = datas[len(datas) - idx*ema_coffidence*60-1]
		total_ema += _tmp[3]
	return total_ema/5


if __name__ == '__main__':
	# dropDB()
	# createDB()
	# randomData()
	# cu = cx.cursor()
	# for r in  cu.execute('select count(*) from demotest'):
	# 	print 'data in db is ',r[0]
	getResult()

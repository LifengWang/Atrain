# coding = utf8

import sqlite3

cx = sqlite3.connect("demo.db")
if __name__ == '__main__':
	cu = cx.cursor()
	rs =  cu.execute('select count(*) from demotest')
	for r in rs:
		print r
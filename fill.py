#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from time import sleep
from random import choice
# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "12345678", "labdb", charset='utf8')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
for i in range(10):
	sleep(0.11238)
	slastName = ['赵','孙','李','周','吴','郑','王','陈','魏','沈','韩','杨','方','林','马','方']
	sfirstName1 = ['子','国','家','学','舒','小','嘉','志','泽','其']
	sfirstName2 = ['伟','豪','涵','萱','云','航','杰','峰','俊','勇','诚','琪']
	if(choice([1,2]) == 1):
		sname = choice(slastName)+choice(sfirstName2)
	else:
		sname = choice(slastName)+choice(sfirstName1)+choice(sfirstName2)

	ssex = choice(['男','女'])
	sage = choice([20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
	sdept = choice(['01', '02', '03', '04', '05', '06', '07', '08', '09'])
	saddr = choice(['吉林省长春市', '黑龙江省哈尔滨市', '辽宁省大连市', '山东省青岛市', \
	         '香港特别行政区', '内蒙古自治区呼兰浩特市', '北京市', '上海市',\
	          '四川省成都市', '福建省宁波市', '江苏省无锡市', '陕西省西安市'])
	sid = choice(['114', '115', '113', '116']) + \
			 choice(['031', '262', '032', '035', '042']) + \
			 choice(['01', '02', '03', '04', '05', '06', '07']) + \
			 choice(['10', '01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17', '18', '19'])

	sclass = sid[:8]

	# SQL 插入语句
	sql = "INSERT INTO Student(Sid, Sage, Ssex, Sdept, Sname, Saddr, Sclass) VALUES ('%s', %d, '%s', '%s', '%s', '%s', '%s')" % (sid, sage, ssex, sdept, sname, saddr, sclass)
	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

# 关闭数据库连接
db.close()
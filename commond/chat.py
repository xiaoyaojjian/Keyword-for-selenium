# -*- codeing:utf-8 -*-
import xmpp
import time
import datetime
import os
username = 'chenjiangpeng@xtpt.e-u.cn'
password = 'a1b2c3d4'
to = ['chenjiangpeng@xtpt.e-u.cn']
#to = ['chenjiangpeng@xtpt.e-u.cn','zhangyy@xtpt.e-u.cn','liujiao@xtpt.e-u.cn']
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
directory = '..\\result\\'
path = directory+day+"\\"

def sortfile(path):
	"""
	获取path目录下，最后更新的文件名称
	"""
	
	fl = os.listdir(path) #获取path目录文件列表
	#时间戳进行倒序排序
	fl.sort(key=lambda fn: os.path.getmtime(path + fn) if not os.path.isdir(path + fn) else 0)
	#date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象
	dt=datetime.datetime.fromtimestamp(os.path.getmtime(path + fl[-1]))
	#dt.strftime("%Y年%m月%d日 %H时%M分%S秒" 将date对象格式化显示
	print('最后改动的文件是: '+fl[-1]+"，时间："+dt.strftime("%Y年%m月%d日 %H时%M分%S秒"))
	msg = "自动化测试完成，点击下面链接查看测试结果：\n "+"http://192.168.200.8/result/"+day+"/"+fl[-1]
	return msg

def to_msg():
	msg = sortfile(path)
	client = xmpp.Client('xtpt.e-u.cn')
	client.connect(server = ('xtpt.e-u.cn', 5223))
	client.auth(username, password, 'botty')

	# client.sendInitPresence()
	# message = xmpp.Message(to, msg, typ = 'chat')
	# client.send(message)
	# time.sleep(0.2)

	for i in to:
		#print i
		client.sendInitPresence()
		message = xmpp.Message(i, msg, typ = 'chat')
		client.send(message)
		time.sleep(0.2)
	#print msg

if __name__=='__main__':
	to_msg()
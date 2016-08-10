#-*- coding: utf-8 -*-
__author__ = 'tsbc'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import paramiko
import os
import time

class Upload():
	"""
	上传每天生成的测试报告到Linux的web服务器
	/result/  下存放html文件
	/result/image  截图文件
	"""

	username = "root"
	password = "a1b2c3"
	hostname = "192.168.200.8"
	localdir = "..\\result\\"
	romotedir = "/opt/lampp/htdocs/result/"
	port = 22

	#日期格式 2014-12-17
	day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
	#获取当前时间格式 2014-12-12-10_39_58
	now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

	#定义shell创建目录命令：判断路径是否存在
	mkdir_day = "[ -d \"" + romotedir + day + "\" ] || mkdir " + romotedir + day + "; "
	mkdir_img = "[ -d \"" + romotedir + day + "/image\" ] || mkdir " + romotedir + day + "/image"
	# print mkdir_day
	# print mkdir_img
	"""
	SSH远程登录Linux主机
	"""
	#调用ssh客户端接口，进行登录
	s = paramiko.SSHClient()
	#s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s.connect(hostname=hostname, username=username, password=password)
	#使用Linux标准的输入、输出、报错，调用定义好的shell命令进行创建目录
	stdin,stdout,stderr=s.exec_command(mkdir_day + mkdir_img)
	#输出命令反馈
	print stdout.read()
	#关闭连接
	s.close()
	"""
	os.walk()输出为:
	([路径],[目录],[文件])
	('..\\result\\2014-12-18', ['image'], ['2014-12-18-10_42_43_result.html'])
	('..\\result\\2014-12-18\\image', [], ['2014-12-18-11_28_33_login.png', '2014-12-18-11_28_36_login.png'])

	"""
	path = localdir + day
	if os.path.exists(path):
		nested = os.walk(path)
		for i in nested:
			#print i
			tt = i[1]   #i[0] 是路径； i[1] 目录名称列表； i[2] 是文件列表
			if len(tt) > 0:  #当tt>0时，说明是根目录（入口目录）下，tt<0时，说明当前是叶子目录
				print u" = +当前目录 " + str(i[0]) + u" 下的文件有："
				ff = i[0].split('\\')#使用\进行路径分割
				ddir = ff[len(ff)-1]#获取末尾的文件目录名称
				for j in i[2]:
					localn = localdir + ddir + "\\" + j
					romoten = romotedir + ddir + "/" + j
					print j
					# print localn
					# print romoten
					try:
						#通过主机名、端口、用户名和密码连接远程主机。
						t = paramiko.Transport(hostname, port)
						t.connect(username=username, password=password)
						sftp =paramiko.SFTPClient.from_transport(t)
						#sftp的put表示把本地文件传送到远程机器上，get表示把远程文件传递到本地机器上。
						sftp.put(localn, romoten)
						#关闭连接
						t.close()
					except Exception, e:
						import traceback
						traceback.print_exc()
						try:
							t.close()
						except:
							pass
			elif len(tt) < 1:
				print u" = +当前目录 " + str(i[0]) + u" 下的文件有："
				ff = i[0].split('\\')#使用\进行路径分割
				fdir = ff[len(ff)-1]#获取末尾的文件目录名称
				for j in i[2]:
					localn = str(i[0]) + "\\" + j #str(i[0]) == localdir + fdir
					romoten = "/opt/lampp/htdocs/result/" + day +"/"+ fdir + "/" + j
					print j
					# print localn
					# print romoten
					#stdin,stdout,stderr=s.exec_command("mkdir /opt/lampp/htdocs/result/"+fdir)
					try:
						t = paramiko.Transport(hostname, port)
						t.connect(username=username, password=password)
						sftp =paramiko.SFTPClient.from_transport(t)
						#sftp的put表示把本地文件传送到远程机器上，get表示把远程文件传递到本地机器上。
						sftp.put(localn, romoten)
						t.close()
					except Exception, e:
						import traceback
						traceback.print_exc()
						try:
							t.close()
						except:
							pass
	else:
		print path+" 目录不存在,报告未能成功上传！"
if __name__ == "__main__":
	Upload()

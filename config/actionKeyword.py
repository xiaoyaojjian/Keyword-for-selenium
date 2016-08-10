# -*- coding:utf-8 -*-
__author__ = 'tsbc'

from selenium import webdriver
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from public import BasePage

class Actionkeywords(BasePage.Action):
	"""定义关键字方法"""

	def openBrowser(self):
		"""打开浏览器方法"""
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)

	def navigate(self, url):
		"""
		跳转Url地址
		"""
		self.driver.get(url)

	def closeBrowser(self):
		"""关闭浏览器"""
		self.driver.quit()

	#调用send_keys
	def input_Text(self, loc, text):
		"""文本框输入内容"""
		print loc,text
		self.send_keys(loc, text)
	#
	def Submit(self, submit_loc):
		"""提交表单"""
		self.saveScreenshot(self.driver, "submit")
		self.find_element(*submit_loc).click()

	def clickButton(self, button_loc):
		"""点击按钮"""
		#print self.find_element(*button_loc).text
		self.find_element(*button_loc).click()

	def clickElement_i(self, index, *element_loc):
		"""点击元素"""
		# print self.find_elements_i(i, *element_loc)
		self.find_elements_i(*element_loc, index=index).click()

	def verifyLogin(self, span_loc, userid_loc):
		"""登录校验"""
		spanTF = True
		try:
			#通过捕获异常，判断是否显示的出了Tip文本，显示为 True 否则为False
			self.find_element(*span_loc).text
			spanTF = True
		except:
			spanTF = False

		if spanTF:
			print self.find_element(*span_loc).text
		else:
			print self.driver.title
			self.checkTrue(self.driver.find_element(*userid_loc).text, u"登录失败")


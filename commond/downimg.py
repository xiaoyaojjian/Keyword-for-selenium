__author__ = 'tsbc'

import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(page):
	rs = r'src="(.*?\.jpg)".+?width'
	imgre = re.compile(rs)
	imglist = re.findall(imgre, page)
	x = 1
	for imgurl in imglist:
		urllib.urlretrieve(imgurl, "%s.jpg" % x)
		print x
		x = x + 1

page = getHtml("http://tieba.baidu.com/photo/g?kw=%E5%8A%A8%E6%BC%AB&ie=utf-8")
print page
print getImg(page)
# -*- coding:utf-8 -*-
__author__ = 'Ray'
def highlightElement(driver, element):
	"""
	元素高亮显示
	"""
        driver.execute_script("element = arguments[0];" +
             "original_style = element.getAttribute('style');" +
             "element.setAttribute('style', original_style + \";" +
             "background: yellow; border: 2px solid red;\");" +
             "setTimeout(function(){element.setAttribute('style', original_style);}, 1000);", element)
# -*- coding:utf-8 -*-
__author__ = 'tsbc'

import xlrd
b = xlrd.open_workbook('..\\dataEngine\\data.xls')

count = len(b.sheets())

print count

for sheet in b.sheets():
    print sheet.name #返回Sheet名称
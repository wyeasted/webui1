#!/usr/bin/env python
# -*-coding:utf-8-*-

import csv
import os
import  xlrd
import xml.dom.minidom

def readlists():
	lists=[
		['','',u'请您输入手机/邮箱/用户名'],
		['admin','',u'请您输入密码'],
		['','admin',u'请您输入手机/邮箱/用户名']]
	return lists

def readTxt():
	with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','log.txt'),'r') as f:
		return f.read().split('\n')

class Datahelper(object):

	def readCsv(self,value1,value2):
		rows=[]
		data_file=open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','csvtest.csv'))
		reader=csv.reader(data_file)
		next(reader,None)
		for row in reader:
			rows.append(row)
		return ''.join(rows[value1][value2]).decode('gb2312')

	@staticmethod
	def readExcel(value1, value2):
		book = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)),'data', 'exceltest.xlsx'))
		sheet = book.sheet_by_index(0)
		return sheet.cell_value(value1, value2)

	@staticmethod
	def readExcels():
		rows = []
		book = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data','exceltests.xlsx'))
		sheet = book.sheet_by_index(0)
		for row in range(1, sheet.nrows):
			rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
		return rows

	@staticmethod
	def getXmlData(self,value):
		dom = xml.dom.minidom.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data','xmltest.xml'))
		db = dom.documentElement
		name = db.getElementsByTagName(value)
		nameValue = name[0]
		return nameValue.firstChild.data

	def getXmlUser(self,parent, child):
		dom = xml.dom.minidom.parse(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data','xmltest.xml'))
		db = dom.documentElement
		itemlist = db.getElementsByTagName(parent)
		item = itemlist[0]
		return item.getAttribute(child)









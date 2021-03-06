#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
from page.init import *
from page.login import *
from utiles.data import *

class BaiduTestExcel(UiTestcase,Login):
	def test_login_username_passwd_null(self):
		'''登录：用户名和密码为空点击后的错误提示信息'''
		data = Datahelper()
		self.login(data.readCsv(1,0),data.readCsv(1,1))
		divText=self.getDivError
		self.assertEqual(divText,data.readCsv(1,2))

if __name__ == '__main__':
	unittest.main(verbosity=2)
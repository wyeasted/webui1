#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import ddt

from page.init import *
from page.login import *
from utiles.data import *

@ddt.ddt
class BaiduExcelTest(UiTestcase,Login):
	@ddt.data(*Datahelper.readExcels())
	@ddt.unpack
	def test_login_username_passwd_null(self, username, password, expected):
		self.login(username,password)
		self.assertEqual(self.getDivError,expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)




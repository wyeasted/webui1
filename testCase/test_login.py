#!/usr/bin/env python
#-*-coding:utf-8-*-

import ddt

from page.init import *
from page.login import *
from utiles import data

@ddt.ddt
class LoginTest(UiTestcase,Login):
	@ddt.data(*data.readlists())
	@ddt.unpack
	def test_login(self,username,password,expected):
		'''验证：对登陆表单的验证'''
		self.login(username,password)
		self.assertEqual(self.getDivError,expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)


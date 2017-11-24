#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium import webdriver
import unittest
from page.init import *
from page.login import *
from utiles.data import readTxt

class BaiduTestTxt(UiTestcase,Login):
	def test_username_pass_null(self):
		'''验证：用户名和密码为空后的错误提示信息'''
		self.login(readTxt()[0],readTxt()[1])
		divText=(self.getDivError).encode('utf-8')
		self.assertEqual(divText,readTxt()[2])

if __name__ == '__main__':
	unittest.main(verbosity=2)

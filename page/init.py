#!/usr/bin/env python
# -*-coding:utf-8-*-

import unittest
from selenium import webdriver

class UiTestcase(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('https://www.baidu.com')

	def tearDown(self):
		self.driver.quit()
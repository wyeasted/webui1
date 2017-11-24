#!/usr/bin/env python
# -*-coding:utf-8-*-

import time as t
from selenium import webdriver

class TestEcloud(object):
	def __init__(self,driver):
		self.driver=driver

	def findElement(self, *loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			print 'Error details :%s' %(e.args[0])

	def findsElement(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException as e:
			print 'Error details :%s' %(e.args[0])

	def wait(self):
		t.sleep(5)





















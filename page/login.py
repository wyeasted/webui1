#!/usr/bin/env python
# -*-coding:utf-8-*-

from selenium.webdriver.common.by import By
import sys
import os
from base.object import *

class Login(TestEcloud):
	clicklogin=(By.LINK_TEXT,u'登录')
	username = (By.ID, 'TANGRAM__PSP_10__userName')
	password = (By.ID, 'TANGRAM__PSP_10__password')
	login_button = (By.ID, 'TANGRAM__PSP_10__submit')
	div_loc = (By.ID, 'TANGRAM__PSP_10__error')


	def clickLogin(self):
		self.findElement(*self.clicklogin).click()

	def typeUsername(self, username):
		self.findElement(*self.username).send_keys(username)

	def typePassword(self, password):
		self.findElement(*self.password).send_keys(password)

	def loginbutton(self):
		self.findElement(*self.login_button).click()

	def login(self,username,password):
		self.clickLogin()
		self.typeUsername(username)
		self.typePassword(password)
		self.loginbutton()

	@property
	def getDivError(self):
		return self.findElement(*self.div_loc).text

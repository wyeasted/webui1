#!/usr/bin/env python
# -*-coding:utf-8-*-

#!/usr/bin/env python
#-*-coding:utf-8-*-

import  unittest
from page.login import *
from page.init import *
from utiles.data import Datahelper

class XmlTest(UiTestcase,Login,Datahelper):
	def test_xml_001(self,elementTag='nullText'):
		'''验证:用户名和密码为空返回的错误提示信息'''
		self.login('','')
		self.assertEqual(self.getDivError,self.getXmlData(self,elementTag))
	def test_xml_002(self,value='passwdNull'):
		'''验证:密码为空的错误提示信息'''
		self.login('aa','')
		self.assertEqual(self.getDivError,self.getXmlData(self,value))

if __name__ == '__main__':
	unittest.main(verbosity=2)
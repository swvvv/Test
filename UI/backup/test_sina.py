#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:linghui

import unittest
from page.pageLogin import *
from selenium import webdriver
import time as t

class SinaTest(unitest.TestCase, Sina):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get('http://126.')

	def tearDown(self):
		self.driver.quit()

	def test_sinaLogin_001(self):
		'''登陆业务：账号密码为空验证'''
		self.login('','')
		self.assertEqual(self.getLoginError,'请输入邮箱名')

	def test_sinaLogin_002(self):
		'''登陆业务：输入不规范的邮箱名'''
		self.login('wuya1303','asd888')
		self.assertEqual(self.getLoginError, '您输入的邮箱名格式不正确')

if __name__ == '__main__':
	unittest.main(verbosity = 2)